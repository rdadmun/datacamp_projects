from airflow.operators.bash import BashOperator

# Define a new pull_sales task
pull_sales = BashOperator(
    task_id='pullsales_task',
    bash_command = 'wget https://salestracking/latestinfo?json'
)

# Set pull_sales to run prior to cleanup
pull_sales >> cleanup

# Configure consolidate to run after cleanup
cleanup >> consolidate

# Set push_data to run last
consolidate >> push_data