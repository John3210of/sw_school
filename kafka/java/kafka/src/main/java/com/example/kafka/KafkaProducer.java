package com.example.kafka;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;


//서비스 클래스 라는 것을 명시하고 인스턴스를 자동으로 생성해달라고 하는 어노테이션
@Service
//자동 주입되는 인스턴스를 대입받는 생성자를 만들어 달라는 어노테이션
@RequiredArgsConstructor
public class KafkaProducer {
   //토픽 이름 설정
   private static final String TOPIC = "exam-topic";


   //의존성 주입을 받기 위한 어노테이션
   @Autowired
   private  KafkaTemplate<String, String> kafkaTemplate;
   //로그 출력하기 위한 인스턴스를 생성
   private final Logger log = LoggerFactory.getLogger(getClass());
  
   //메시지 전송하는 메서드
   public void sendMessage(String name, int age) {
       log.info("Produce message : {}{}", name, age);
       //System.out.println("전송된 메시지:" +  name + age);
       String message = "{\"name\":" + "\"" + name + "\"" + ", \"age\":" + age + "}";
       //실제 메시지 전송
       this.kafkaTemplate.send(TOPIC, message);
   }
}

    