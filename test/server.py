# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
def application(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8080, application)
print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()