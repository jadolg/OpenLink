FROM python:3.6.0-alpine

ADD . /home/
WORKDIR /home/
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "run.sh"]
