FROM python:3.6-alpine3.7

ADD . /home/
WORKDIR /home/
RUN pip3 install -r requirements.txt --no-index --find-links="/home/libs/"

EXPOSE 8000

CMD ["/bin/sh", "run.sh"]
