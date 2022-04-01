import asyncpg
import json
from typing import Union
import fastapi


Connection = asyncpg.Connection


async def init(config: dict) -> asyncpg.Pool:
    dsn = config.get('dsn')
    if not dsn:
        raise RuntimeError('DB connection parameters not defined')
    return await asyncpg.create_pool(
        dsn, 
        init=init_connection,
        **{k: v for k, v in config.items() if k != 'dsn'}
    )


async def init_connection(conn):
    await conn.set_type_codec(
        'jsonb',
        encoder=json.dumps,
        decoder=json.loads,
        schema='pg_catalog'
    )
    return conn


async def close(db: Union[asyncpg.Pool, asyncpg.Connection]):
    await db.close()


async def get(request: fastapi.Request) -> Connection:
    try:
        pool = request.app.state.db_pool
    except AttributeError:
        raise RuntimeError('Application state has no db pool')
    else:
        async with pool.acquire() as conn:
            yield conn