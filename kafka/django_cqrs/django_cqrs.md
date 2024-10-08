** Django CQRS 구현하기

- read >> mongoDB와 연동한 읽기전용 서버
- write >> mariaDB와 연동한 삽입전용 서버

- kafka를 활용하여 read에서는 table의 select만 수행
