# Import the timedelta object
from airflow import DAG
from datetime import timedelta, datetime

# Create the dictionary entry
default_args = {
  'start_date': datetime(2024, 1, 20),
  'sla': timedelta(hours=0.5)
}

# Add to the DAG
test_dag = DAG('test_workflow', default_args=default_args, schedule_interval=None)