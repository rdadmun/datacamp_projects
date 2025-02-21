from airflow import DAG

default_args = {
  'owner': 'jdoe',
  'start_date': '2023-01-01'
}
with DAG("etl_update",
         default_args=default_args
        ):
    pass