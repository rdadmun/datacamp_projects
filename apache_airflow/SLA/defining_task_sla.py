# Import the timedelta object
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta

test_dag = DAG('test_workflow', start_date=datetime(2024,1,20), schedule_interval=None)

# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla=timedelta(hours=3),
                     bash_command='initialize_data.sh',
                     dag=test_dag)