mysql -h database-1.cqshokmqgqfv.ap-northeast-1.rds.amazonaws.com -P 3306 -u demo -p business < init.sql

spark.sql("select user_mail,goods_id,COUNT(order_id) as order_count,SUM(good_count) as good_count from flink_hudi_order group by user_mail, goods_id").show()