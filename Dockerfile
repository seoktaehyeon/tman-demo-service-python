FROM bxwill/python:3.8-flask
LABEL maintainer="v.stone@163.com"

WORKDIR /workspace
COPY . .

RUN pip install -r requirements.txt

CMD ./launch.sh
EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=5s --retries=3 CMD ./health_check.sh
