# netstat
查找对应端口的pid
```
sudo netstat -autnp | grep port # 必须加sudo,不然很多程序没法获得pid
```
