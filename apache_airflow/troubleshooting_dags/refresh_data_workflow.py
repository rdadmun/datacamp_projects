from airflow import DAG

default_args = {
  'owner': 'jdoe',
  'email': 'jdoe@datacamp.com'
}
with DAG( 'refresh_data', 
          default_args=default_args 
        ):
    pass