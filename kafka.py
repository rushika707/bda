sudo apt-get update
sudo apt install default-jdk -y
java -version
sudo apt-get install openssh-server openssh-client -y
sudo service ssh restart
ssh localhost
cd ~
wget https://archive.apache.org/dist/kafka/3.2.1/kafka_2.12-3.2.1.tgz
tar -xzf kafka_2.12-3.2.1.tgz
sudo mv kafka_2.12-3.2.1 /home/
ln -s /home/kafka_2.12-3.2.1 ~/kafka
cd ~/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
#Keep this terminal OPEN
#Start Kafka Server (New Terminal)
cd ~/kafka
bin/kafka-server-start.sh config/server.properties
#Keep this also OPEN
#Create Topic (New Terminal)
cd ~/kafka
bin/kafka-topics.sh --create \
--topic test-topic \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
#start procedure
cd ~/kafka
bin/kafka-console-producer.sh \
--topic test-topic \
--bootstrap-server localhost:9092
#Now type message:
Hello Kafka
#Start Consumer (New Terminal)
cd ~/kafka
bin/kafka-console-consumer.sh \
--topic test-topic \
--from-beginning \
--bootstrap-server localhost:9092
