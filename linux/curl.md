# curl
用来发送`http`请求的

## -s参数 静默模式
`--silent        Silent mode`

## -v 详细模式
`--verbose       Make the operation more talkative`

## -o参数 输出到文件
```
-o, --output <file> Write to file instead of stdout

curl -s https://www.baidu.com -o baidu.html
```

## -H参数 header
```
-H <header/@file> Pass custom header(s) to server

curl -v https://www.baidu.com -H "Content-Type: application/json"
```

## -X参数 请求方法
```
--request <command> Specify request command to use

curl -v https://www.baidu.com -X POST
```

## -d参数 body内容
```
-d, --data <data>   HTTP POST data

curl -v https://www.baidu.com -d "hahaha"
```
