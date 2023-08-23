CREATE SCHEMA titanic;

CREATE TABLE titanic.passenger(
    id int,
    survived boolean,
    pclass int,
    name varchar,
    sex varchar,
    age float,
    sibssp int,
    parch int,
    ticket varchar,
    fare float,
    cabin varchar,
    embarked varchar,
    PRIMARY KEY (id)
);
COPY titanic.passenger
FROM '/seed-data/titanic.csv' 
DELIMITER ',' 
CSV HEADER;