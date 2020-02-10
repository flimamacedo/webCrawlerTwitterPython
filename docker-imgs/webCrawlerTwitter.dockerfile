FROM python:3

WORKDIR /usr/src/app

COPY ./conf/webCrawlerTwitter/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./conf/webCrawlerTwitter/streamingTwitters.py .
ADD ./conf/webCrawlerTwitter/streamingTwitters.py  /
#CMD [ "python", "./conf/webCrawlerTwitter/streamingTwitters.py" ]
CMD [ "python", "./streamingTwitters.py" ]
