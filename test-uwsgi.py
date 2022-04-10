# -*-coding:utf-8-*-

# 测试uwsgi
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 启动uwsgi
# uwsgi --http :9001 --wsgi-file test-uwsgi.py --callable application
