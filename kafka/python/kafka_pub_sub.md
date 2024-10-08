1)
docker-compose.yml 파일을 생성하고 작성
version: '2'
services:
  zookeeper:
	,,,
	volumes:
  	- /var/run/docker.sock:/var/run/docker.sock

2)터미널에서 명령을 수행 - 클러스터 1개를 가진 카프카 서버를 실행
docker-compose up -d

3)외부에서 사용할 수 있도록 설정 변경
=>터미널에서 도커 컨테이너 안으로 접속
docker exec -it kafka /bin/bash

=>설정 파일을 수정 - 내용을 추가
listeners=PLAINTEXT://:9092                                                   
delete.topic.enable=true                                                        
auto.create.topics.enable=true  

4)토픽 생성 과 조회 및 삭제
=>명령어를 사용하기 위해서 프롬프트 이동: bash# cd /opt/kafka/bin
=>첫번째 카프카 서버의 첫번째 영역에 토픽(exam-topic) 생성: bash# kafka-topics.sh --bootstrap-server localhost:9092 --list
=>토픽 삭제: bash# kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic exam-topic

5)메세지 전송 및 받기
터미널에서 docker exec -it kafka /bin/bash
bash# cd /opt/kafka/bin

◆ 메시지 전송
▪ bash-5.1# kafka-console-producer.sh --topic exam-topic --broker-list localhost:9092
◆ 메시지 확인 – 새로운 터미널 실행
▪ bash-5.1# kafka-console-consumer.sh --topic exam-topic --bootstrap-server localhost:9092 --from-beginning

