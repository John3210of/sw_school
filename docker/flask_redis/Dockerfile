FROM python:3.11-alpine
RUN apk update && apk add --no-cache bash
RUN apk add --update build-base python3-dev py-pip

ENV FLASK_APP=app
ENV FLASK_ENV=dev

EXPOSE 9000
WORKDIR /app

COPY /flask_redis /app/
RUN pip install -r requirements.txt
CMD ["python","app.py"]