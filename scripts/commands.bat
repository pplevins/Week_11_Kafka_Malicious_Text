@REM Creating Kafka docker container
docker run -d -p 9092:9092 --name broker apache/kafka:latest

@REM To see all massages sent to kafka container:
docker exec -it broker /bin/bash
cd /opt/kafka/bin
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic raw_tweets_not_antisemitic --from-beginning
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic raw_tweets_antisemitic --from-beginning

@REM Running local MongoDB for persister and data retriever
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server
