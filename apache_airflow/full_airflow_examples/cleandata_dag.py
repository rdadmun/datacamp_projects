from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2023, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Create a templated command to execute
# 'bash cleandata.sh datestring'


# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command='bash cleandata.sh datestring',
                          dag=cleandata_dag)
