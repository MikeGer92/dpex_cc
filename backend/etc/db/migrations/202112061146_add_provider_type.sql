-- migrate:up

CREATE TYPE provider_t_enum AS ENUM ('mercuryo', 'grow');


ALTER TABLE callback_data 
    ADD COLUMN provider provider_t_enum DEFAULT 'mercuryo';

CREATE INDEX callback_data_data_idx ON callback_data (data_jsonb);


-- migrate:down


ALTER TABLE callback_data
    DROP COLUMN provider;

DROP TYPE provider_t_enum;