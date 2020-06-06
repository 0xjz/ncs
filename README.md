# netcat + ssl
Thanks to chpie
```bash
➜  ./ncs.py naver.com 443
GET / HTTP/1.1
Host: naver.com
Connection: close

HTTP/1.1 301 Moved Permanently
Server: NWS
Date: Mon, 03 Feb 2020 05:40:50 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: close
Location: http://www.naver.com/
Vary: Accept-Encoding,User-Agent
Referrer-Policy: unsafe-url

a2
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center> NWS </center>
</body>
</html>

0
```

