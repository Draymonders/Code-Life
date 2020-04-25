# nginx
首先先安装`nginx`,网上搜各种教程吧
- [openresty下载安装](https://openresty.org/cn/installation.html)

## location
先看如下配置
```conf
location = /a {
  echo "=/a";
}   
    
location ^~ /a/b {
  echo "^~ /a/b";
}

location ^~ /a {
  echo "^~ /a";
}

location ~ /\w {
  echo "~ /\w";
}

location / { 
  echo "=/";
} 
```
总体上 location有四个级别 按照优先级分别是 `=`, `^~`, `~`, `/`, 分别是 `精确匹配`, `优先前缀匹配`, `正则匹配`, `普通前缀匹配`
如果同一级别多个匹配命中,那么走匹配长度最长的那个
如果匹配长度相同, 那么走匹配规则写在前面的那一个

## proxy_pass
反向代理
这里访问 `localhost`就会跳转到`https://www.baidu.com`
```conf
location / {
  proxy_pass https://www.baidu.com;
}
```

### 一个有趣的trick
```conf
location = /a {
  proxy_pass https://www.baidu.com/         
}
```
此时访问 `localhost/a` 就会跳转到 `https://www.baidu.com/a`

**如何使得我们访问 `localhost/a`跳转到`baidu.com/`,而不是`baidu.com/a`呢?**

> 用如下方法 (末尾加`/`)
- 请求地址末尾由`/a` => `/a/`
- 请求url有`baidu.com` => `baidu.com/`

```conf
location = /a/ {
  proxy_pass https://www.baidu.com/;
}
```

反向代理小节
```
location /a {
  proxy_pass http://ip;
}

location /b/ {
  proxy_pass http://ip;
}

上述配置会导致:
/a/x => http://ip/a/x
/b/x => http://ip/x
```


## upstream
用来实现负载均衡
```
upstream group1 {
  server 192.168.0.1:80 weight 1;
  server 192.168.0.1:81 weight 1;
}

location / {
  proxy_pass http://group1;
}
```

## autoindex
- [autoindex的问题](https://stackoverflow.com/questions/44801064/nginx-error-404-when-using-autoindex)
- [root和alias](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)