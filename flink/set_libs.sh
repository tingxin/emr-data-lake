target=/usr/lib/flink/lib/
# 下载hudi flink bundle jar, 这个是我针对EMR6.4.0编译好的，用这个就可以
wget https://dxs9dnjebzm6y.cloudfront.net/tmp/hudi-flink-bundle_2.12-0.10.1.jar
sudo mv hudi-flink-bundle_2.12-0.10.1.jar /usr/lib/flink/lib/
# kafka connector
wget https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka_2.12/1.13.1/flink-connector-kafka_2.12-1.13.1.jar
sudo mv flink-connector-kafka_2.12-1.13.1.jar  ${target}

# mysql cdc connector
wget https://repo1.maven.org/maven2/com/ververica/flink-sql-connector-mysql-cdc/2.2.1/flink-sql-connector-mysql-cdc-2.2.1.jar
sudo mv flink-sql-connector-mysql-cdc-2.2.1.jar  ${target}


# mongo cdc connector
wget https://repo1.maven.org/maven2/com/ververica/flink-sql-connector-mongodb-cdc/2.1.1/flink-sql-connector-mongodb-cdc-2.1.1.jar
sudo mv flink-sql-connector-mongodb-cdc-2.1.1.jar  ${target}

# mysql jdbc connector
wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-jdbc_2.11/1.13.1/flink-connector-jdbc_2.11-1.13.1.jar
sudo mv flink-connector-jdbc_2.11-1.13.1.jar ${target}

wget https://repo.maven.apache.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar
sudo mv mysql-connector-java-8.0.23.jar ${target}

# hudi新版本已经把hive-exec从bundle包抽出来了，这样做很好，对Metastore兼容性会更强，比如Glue，下面三个copy 当我们需要将hudi的表自动同步到Hive Metastore或者Glue Metastore是需要。 如果不需要实时自动同步，不用下面三个 包。
sudo cp /usr/lib/hive/lib/libthrift-0.9.3.jar ${target}
sudo cp /usr/lib/hive/lib/hive-exec.jar ${target}
sudo cp /usr/lib/hive/lib/commons-lang-2.6.jar ${target}
# glue catalog jar，使用这个jar实现的AWSGlueDataCatalogHiveClientFactory, 如果需要将数据同步到Glue Catalog需要这个Jar
sudo cp /usr/lib/hive/auxlib/aws-glue-datacatalog-hive3-client.jar ${target}
