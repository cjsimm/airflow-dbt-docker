Docker compose file that spins up a generic airflow installation along compatible with dbt.

By default, initializes an example postgres database container that is 
populated with the famous titanic dataset. saved in the dags folders are
two pipelines that SELECT ALL from the postgres db in order to check that dbt and airflow are working. 