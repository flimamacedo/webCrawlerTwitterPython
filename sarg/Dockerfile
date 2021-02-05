FROM python:3.7.0
ENV PYTHONUNBUFFERED 1  
RUN mkdir /sarg
WORKDIR /sarg
ADD ./sarg/requirements.pip /sarg
RUN pip install --no-cache-dir -r requirements.pip
ADD ./sarg/app /sarg
