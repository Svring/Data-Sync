//导入http
var http=require('http');
 
//创建
http.createServer(function (request,response) {
    response.writeHead(200,{'Content-type':'text/html;charset=utf-8'});
    if(request.url!=='/favicon.ico'){//清除二次访问
        console.log('访问');
        response.write('hello world');
        response.end("世界");//不写会没有协议尾部，但是写了会访问俩次
    }
}).listen(8000);
console.log('Server running at http://127.0.0.11:8000/')