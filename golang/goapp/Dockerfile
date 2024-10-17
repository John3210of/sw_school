# multi stage
FROM golang:1.15-alpine3.12 AS gobuilder-stage
WORKDIR /goapp
COPY . /goapp
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /goapp/local/bin/gostart

FROM scratch AS runtime-stage
COPY --from=gobuilder-stage /goapp/local/bin/gostart /goapp/local/bin/gostart
CMD ["/goapp/local/bin/gostart"]

# single stage
FROM golang:1.15-alpine3.12

WORKDIR /goapp
COPY . /goapp

# 빌드 명령을 그대로 실행하여 Go 바이너리를 생성
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /goapp/local/bin/gostart

# 최종 실행 명령
CMD ["/goapp/local/bin/gostart"]
