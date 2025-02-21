# Import the BashOperator
from airflow.operators.bash import BashOperator
from airflow import DAG

with DAG(dag_id="test_dag", default_args={"start_date": "2024-01-01"}) as analytics_dag:
  # Define the BashOperator 
  cleanup = BashOperator(
      task_id='cleanup_task',
      # Define the bash_command
      bash_command='cleanup.sh',
  )
