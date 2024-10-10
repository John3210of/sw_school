package com.example.kafka;

import java.io.IOException;

import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;


@Service
public class KafkaConsumer {
   private final Logger log = LoggerFactory.getLogger(getClass());
   //exam-topic에 들어오는 메시지를 읽어내는 메서드: 비동기적으로 백그라운드에서 수행
   //토픽이 들어오면 자동으로 호출
   @KafkaListener(topics = "exam-topic", groupId = "example")
   public void consume(String message) throws IOException {
       log.info("Consumed message : {}", message);
       JSONObject messageObj = new JSONObject(message);
       log.info(messageObj.getString("name"));
       log.info(messageObj.getInt("age") + "");
   }
}
