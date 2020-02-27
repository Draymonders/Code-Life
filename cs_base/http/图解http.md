# 图解http
粗略读了一下 <<图解http>>这本书  摘抄了部分内容

## 常用http方法
常用的http方法有 `get` `post` `put` `delete` `head` `options`
 - post 传输实体(参数)
 - put 传输文件
 - options 获取服务端接受的方法

## http 1.0
http1.0是**建立一个http就用一个tcp连接**

## http1.1
 - 持久连接的特点是，只要任意一端没有明确提出断开连接，则保持TCP连接状态
 - 管道化技术，就是发送请求不用等响应回来，就可以继续发送请求，异步的体现


## 多部分对象集合
有两种形式
 - multipart/form-data
 - multipart/byteranges
报文起始是 `--filekey`  终止是`--filekey--`
部分内容请求头
 - Range 0-1000

## 状态码
 - 200  ok
 - 204  no content
 - 206  partial content
 - 301  move permanently永久
 - 302  found 临时，保存的书签还是最原始的
 - 303  see other
 - 304  not modify 
 - 400  bad request
 - 401  unauthorized 未认证
 - 403  forbidden 资源有，没权限
 - 404  not found
 - 500  internal server error
 - 503  service unavailable

## header部分字段
header有四种，通用header，请求header，响应header，实体header

### cache-control 
 - no cache 客户端不要过期数据，但是代理服务器可以缓存，只是每次请求时候，代理服务器去检验一下自身缓存是否需要更新

### connection
 - 控制不在转发给代理的字段，减少传输数据
 - 管理持久连接

### accept
- 客户端能接收的文件类型

### host
确定是一台物理机中确定的那个虚拟服务器

### if-match
比较客户端和服务端的etag值(猜测是文件更新需要用到

### if-range
如果成功，返回分片，不成功，返回全部内容。

### accept-ranges
如果value 为bytes服务端可以接受分片

### server
服务端信息。

### location
跳转到value(url更新 状态码为30X redirect

## cookie
 - 服务端向客户端的响应报文的头部有set_cookie字段，客户端拿到后，存起来，下次发送的时候，就带上cookie字段

cookie 
 - 服务端set-cookie
 - 客户端cookie
 - httponly是指，js不能去读取cookie


## 安全
http双方没法确定对方身份，报文公开，存在篡改和泄漏的风险。

### https简单流程
 0. 服务端向第三方注册数字证书(证书对服务端的公钥做了加密)
 1. 非对称加密传送对称加密密钥
 2. 用对称加密密钥加密的内容传送。
 - 因为每次非对称加密耗时，不能过多使用。
 - 对称密钥直接发送存在泄漏的风险。

### 单纯非对称和对称混合的问题
存在的问题就是，服务器传送的非对称加密的公钥存在被篡改的情况，如何解决？
- 数字证书，里面携带有经过第三方认证的公钥。


## websocket
全双工，服务端不用等客户端就可以推送


## web攻击
 - 表单处本身是form，里面添加一些js，导致action地址转向攻击者
 - js去获取cookie并且发送
 - sql注入 and 1=1
 - 调用shell命令去获取一些权限并且发送
 - header改写
 - 重定向
