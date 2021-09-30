from airflow import DAG
from airflow.operators.dummy import DummyOperator

default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('test_dag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    task_1 = DummyOperator(
        task_id='task_1'
    )

    task_2 = DummyOperator(
        task_id='task_2'
    )

    task_3 = DummyOperator(
        task_id='task_3'
    )

    task_1 >> task_2 >> task_3