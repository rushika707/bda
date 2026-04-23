Start-all.sh
start-dfs.sh
start-yarn.sh
jps
rm -rf metastore_db
rm -f derby.log
schematool -dbType derby -initSchema
hive
CREATE TABLE temp_data (
  dt STRING,
  pincode INT,
  temp INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
quit;
nano temp.txt
# in temp file paste below code 
19-01-2024,500001,25
20-01-2024,500003,24
21-01-2024,500075,35
22-01-2024,500014,23
23-01-2024,500017,28
# file permission 
chmod 777 temp.txt
hive
LOAD DATA LOCAL INPATH '/home/hadoop/temp.txt'
INTO TABLE temp_data;
SELECT * FROM temp_data;
# another query 
SELECT dt, MAX(temp)
FROM temp_data
WHERE temp > 25
GROUP BY dt;
