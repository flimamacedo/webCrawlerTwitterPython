FROM python:3

WORKDIR /usr/src/app

COPY ./conf/webCrawlerTwitter/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./conf/webCrawlerTwitter/getTweet.py" ]
