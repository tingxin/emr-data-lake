# emr-data-lake
## 文件结构
```bash
---- datasource     # 创建workshop所需的数据表和模拟数据
  ---- write_db.py  # 往模拟订单表写模拟数据
  ---- init.sql     # 初始化样例数据表
  ---- setting.py   # 测试db 链接信息

---- flink          # 运行flink 程序所需的依赖和脚本
  ---- run_flink.sh # 启动flink session
  ---- set_libs.sh  # 下载本次flnk workshop 的依赖

---- spark          # 运行 spark 程序所需的依赖和脚本
  ---- set_libs.sh  # 下载本次spark workshop 的依赖
  ---- spark-scala-examples-1.0-SNAPSHOT # demo spark 程序

---- airflow        # airflow 样例dag    
  ---- order_dws_etl.py 样例 dag

---- screen         # 用来做模拟数据大屏的 脚本
```