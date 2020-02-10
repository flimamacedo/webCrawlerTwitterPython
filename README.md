# Web Crawler Twitter

<h2>a. Documentação do projeto</h2>

![Image description](http://caseitau.fastsolutionsoncloud.com.br/media/media/planodetrabalho.png)

<h2>b. Documentação das APIs</h2>

![Image description](http://caseitau.fastsolutionsoncloud.com.br/media/media/api2.png)
![Image description](http://caseitau.fastsolutionsoncloud.com.br/media/media/api1.png)

<h2>c. Documentação de arquitetura</h2>

<h2>d. Como subir uma cópia deste ambiente localmente</h2>

<h3>Installation - Requirements</h3>

<ul>
  <li>Access API Twitter</li>
  <li>docker</li>
  <li>docker-compose</li>
  <li>filebeat</li>
</ul>

```
git clone https://github.com/flimamacedo/webCrawlerTwitterPython.git
cd webCrawlerTwitterPython
docker-compose build
docker-compose up -d
yum install filebeat
```
/etc/filebeat/filebeat.yml :

```
paths:
    - /logs_nginx/*.log
setup.kibana:
  host: "localhost:5601"
output.elasticsearch:
  hosts: ["localhost:9200"]
  username: "elastic"
  password: "changeme"  
```
```
/bin/systemctl start filebeat
```
<h2>e. Prints dos Logs(item 8) e os 3 Dashboards(item 9)</h2>

![Image description](http://caseitau.fastsolutionsoncloud.com.br/media/media/dash1.png)
![Image description](http://caseitau.fastsolutionsoncloud.com.br/media/media/dash2.png)
