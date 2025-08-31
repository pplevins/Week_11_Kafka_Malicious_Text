@REM Creating Kafka docker container
docker run -d -p 9092:9092 --name broker apache/kafka:latest

@REM To see all massages sent to kafka container:
docker exec -it broker /bin/bash
cd /opt/kafka/bin
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic raw_tweets_not_antisemitic --from-beginning
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic raw_tweets_antisemitic --from-beginning

@REM Running local MongoDB for persister and data retriever
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server

@REM getting all the requirements
pip freeze > requirements.txt

@REM composing the service stack
docker compose -f compose.yaml up -d

@REM Building and pushing images to DockerHub
docker tag malicious-text-retriever:latest pplevins/malicious-text-retriever:latest
docker push pplevins/malicious-text-retriever:latest
docker tag malicious-text-preprocessor:latest pplevins/malicious-text-preprocessor:latest
docker push pplevins/malicious-text-preprocessor:latest
docker tag malicious-text-enricher:latest pplevins/malicious-text-enricher:latest
docker push pplevins/malicious-text-enricher:latest
docker tag malicious-text-persister:latest pplevins/malicious-text-persister:latest
docker push pplevins/malicious-text-persister:latest
docker tag malicious-text-data-retrieval:latest pplevins/malicious-text-data-retrieval:latest
docker push pplevins/malicious-text-data-retrieval:latest

@REM ---- OpenShift ----
oc login --token=<my-api-token> --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
oc apply -f iran-tweets-secret.yaml
oc apply -f retrieval-tweets-secret.yaml