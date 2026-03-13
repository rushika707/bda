# Start Hadoop services
start-all.sh

# Check Hadoop processes
jps

# Check local directory files
ls

# Create HDFS directory
hdfs dfs -mkdir /bda

# Create empty file in HDFS
hdfs dfs -touchz /bda/handsome.txt

# Write data into HDFS file
echo "Hello World!" | hdfs dfs -put - /bda/handsome.txt

# List HDFS directories
hdfs dfs -ls /

# Display file contents
hdfs dfs -cat /bda/handsome.txt

Open HDFS Web UI

Open Firefox in Ubuntu and search:

http://localhost:9870

Then:

Go to Utilities

Click Browse the File System

Open /bda

Click handsome.txt

Download the file