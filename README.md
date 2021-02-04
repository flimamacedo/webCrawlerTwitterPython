##  Web Crawler Twitter on Docker
##  URLs

* API REST: http://caseitau.fastsolutionsoncloud.com.br/apiRest/tweets/</li>
* SARG: http://caseitau.fastsolutionsoncloud.com.br</li>
* Kibana: http://caseitau.fastsolutionsoncloud.com.br:5601</li>


##  Authentication

* SARG: admin/admin
* Kibana: elastic/changeme


## a. Work Plan

![Work Plan](https://github.com/flimamacedo/webCrawlerTwitterPython/blob/master/imgs/workPlan.PNG)


## b. APIs Documentation 

![Image description](https://github.com/flimamacedo/webCrawlerTwitterPython/blob/master/imgs/api2.PNG)
![Image description](https://github.com/flimamacedo/webCrawlerTwitterPython/blob/master/imgs/api1.PNG)

## c. Archiecture Documentation

Obs.:V1
![Image description](http://caseitau.fastsolutionsoncloud.com.br/media/media/image005.png)

## d. Steps to run this project locally</h2>

Based on the official Docker images:

* [Nginx](https://hub.docker.com/_/nginx)
* [MySQL](https://hub.docker.com/_/mysql)
* [Python](https://hub.docker.com/_/python)


### Contents

1. [Requirements](#requirements)
   * [Twitter](#twitter)
   * [Host setup](#host-setup)
   * [Packages installed localy on host](#packages-installed-localy-on-host)
   * [Python Libraries](#python-libraries)   
   
2. [Usage](#usage)
   * [Bringing up the stack](#bringing-up-the-stack)
   * [Cleanup](#cleanup)
   * [Initial setup](#initial-setup)
     * [Setting up user SARG Admin](#setting-up-user-sarg-admin)
     * [Injecting data](#injecting-data)

### Requirements

#### Twitter

* Access to API Twitter - https://developer.twitter.com/en/docs

> :information_source: Twitter sometimes takes a long time to send access keys

#### Host setup

* [Docker Engine](https://docs.docker.com/install/) 
* [Docker Compose](https://docs.docker.com/compose/install/)
* 2 Gi of RAM
* 2 vCPUs 

By default, the stack exposes the following ports:
* 3306: Mysql TCP
* 80: Nginx HTTP

#### Packages installed localy on host

* filebeat

#### Python Libraries

* tweepy
* pymongo
* mysql-connector-python
* python-dateutil

### Usage

#### Bringing up the stack

Clone this repository onto the Docker host that will run the stack, then start services locally using Docker Compose:

```console
$ git clone https://github.com/flimamacedo/webCrawlerTwitterPython.git
$ cd webCrawlerTwitterPython
$ docker-compose build
$ docker-compose up
```
You can also run all services in the background (detached mode) by adding the `-d` flag to the above command.

> :information_source: You must run `docker-compose build` first whenever you switch branch or update a base image.

If you are starting the stack for the very first time, please read the section below attentively.

#### Cleanup

MySQL data is persisted inside a volume by default.

In order to entirely shutdown the stack and remove all persisted data, use the following Docker Compose command:

```console
$ docker-compose down -v
```

### Initial setup

#### Setting up user SARG Admin

```console
$ sudo docker exec -it sarg sh
python manage.py createsuperuser 
```

#### Injecting data

Give webcrawlertwitter about a minute to initialize, then access the SARG web UI by hitting
[http://localhost](http://localhost) with a web browser and use the credentials created previusly  to log in:


## e. Logs prints(item 8) and three Dashboards(item 9)

![Image description](https://github.com/flimamacedo/webCrawlerTwitterPython/blob/master/imgs/dash1.png)
![Image description](https://github.com/flimamacedo/webCrawlerTwitterPython/blob/master/imgs/dash2.png)
