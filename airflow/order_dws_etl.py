from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from datetime import datetime, timedelta

###############################################
# Parameters
###############################################
spark_app_name = "Spark Hello World"
# 修改成你hadoop 工作目录
app_dir = "/home/hadoop/work/spark"
application = f"{app_dir}/spark-scala-examples-1.0-SNAPSHOT.jar"
dependencies = f"{app_dir}/hudi-spark3.1.2-bundle_2.12-0.10.1.jar,{app_dir}/spark-avro_2.12-3.1.2.jar"
main_class = f"com.tingxin.app.Demo"

###############################################
# DAG Definition
###############################################
now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    dag_id="spark-datalake-demo",
    description="This DAG runs a simple app.",
    default_args=default_args,
    schedule_interval=timedelta(1)
)

start = DummyOperator(task_id="start", dag=dag)


command_format = f"""
spark-submit \
    --deploy-mode cluster \
    --master yarn \
    --class com.tingxin.app.{{0}} \
    --jars {app_dir}/hudi-spark3.1.2-bundle_2.12-0.10.1.jar,{app_dir}/spark-avro_2.12-3.1.2.jar \
    --conf 'spark.serializer=org.apache.spark.serializer.KryoSerializer' \
    --conf 'spark.dynamicAllocation.enabled=false' \
    {app_dir}/spark-scala-examples-1.0-SNAPSHOT.jar
"""

ssh_hook = SSHHook(ssh_conn_id='ssh_default')


dws_command = command_format.format("Dws")
dws_job = SSHOperator(
    task_id='spark_hudi_order_dws',
    ssh_hook=ssh_hook,
    ssh_conn_id='ssh_default',
    command=dws_command,
    dag=dag
)

dws_check_command = command_format.format("CheckDws")
dws_check_job = SSHOperator(
    task_id='quality_check_dws',
    ssh_hook=ssh_hook,
    ssh_conn_id='ssh_default',
    command=dws_check_command,
    dag=dag
)

end = DummyOperator(task_id="end", dag=dag)

start >> dws_job >> dws_check_job >> end
