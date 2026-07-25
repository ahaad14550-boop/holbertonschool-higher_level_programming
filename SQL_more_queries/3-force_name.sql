-- creates table force_name with id and a required name field, if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
