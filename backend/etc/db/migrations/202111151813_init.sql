-- migrate:up

CREATE TABLE callback_data (
    id serial PRIMARY KEY,
    data_jsonb jsonb,
    ctime timestamp
);


-- migrate:down