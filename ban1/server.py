# coding: utf-8

import socket

import urllib.parse
from utils import log
from routes import route_dict


class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query ={}
        self.body=''

    # 解析body的form参数
    def form(self):
        body =  urllib.parse.unquote(self.body)
        args = body.split('&')
        f={}
        for arg in args:
            k,v=arg.split('=')
            f[k]=v
        return f

# 全局的request
request=Request()

def error():
  header='HTTP/1.1 404 OK\r\n Content-Type: text/html\r\n'
  body='<h1>404</h1>'
  r=header + '\r\n' +body
  return r.encode(encoding='utf-8')

def parse_path(path):
    # ?message=hello&author=gua
    # k可能有可能没用find，确定有用split
    index=path.find('?')
    if index == -1:
        return path,{}
    else:
        path,query_string=path.split('?',1)
        args=query_string.split('&')
        query={}
        for arg in args:
            k,v =arg.split('=')
            query[k]=v
        return path,query

def response_for_path(path):
    path,query=parse_path(path)
    request.path=path
    request.query=query

    r={
        # '/static':route_static
    }

    r.update(route_dict)

    response =r.get(path,error)
    return response()

def run(host='', port=3000):
  # 启动服务器
  # with语句在Python中是一个非常有用的语法,它的主要作用是自动管理上下文资源,比如文件、网络连接和锁等。
  # with工作流程:

  # 执行context_expr,它返回一个上下文管理器context;
  # 调用上下文管理器的__enter__()方法;
  # 将__enter__()方法的返回值赋给var;
  # 执行with代码块;
  # 不管是否有异常,都会调用上下文管理器的__exit__()方法进行清理;
  # with结束。
  log('start at', '{}:{}'.format(host, port))
  with socket.socket() as s:
    s.bind((host,port))
    while True:
#       .listen(5)这行代码的作用是设置套接字s的最大连接数量,listen()是socket的一个方法,用于设置TCP服务端可以接受的最大连接数量。

# s.listen(5)中的5表示最大允许有5个连接排队,如果连接数达到5个,后续新的连接将被拒绝直到前面排队的连接被处理完释放资源后才会继续接受新连接。
# 套接字(Socket)是网络编程中的一个非常重要的概念,它提供了不同主机之间的进程或线程之间的通信机制
        s.listen(5)
        connection, address=s.accept()
        request=connection.recv(1024)
        log('原始请求, ', request)
        # 在socket网络编程中,recv()方法接收到的数据都是字节类型的bytes。但是我们通常需要使用str字符串类型来处理文本数据。解码后还可以正确打印日志,因为print本质上是输出str。
        request =request.decode('utf-8')
        # 代码中和字符串变量中永远是\n,打印输出时解释器会把它解释成换行,只有使用repr()和IDE查看变量值时才能直接看到转义字符\n。
        log('ip request, {}\n{}'.format(address,request))


        if len(request.split()) < 2:
            continue
        # 通过request.split()可以将请求行按空格拆分成一个列表。
        path=request.split()[1]
        response=response_for_path(path)
        connection.sendall(response)

        connection.close()


def main():
  config=dict(
    host='',
    port=3000,
  )

  run(**config)

# 1.__name__是一个内置变量,它表示当前模块的名字。
# 2.如果是直接执行这个.py文件,比如在命令行中运行,那么__name__ == 'main'。
# 3.如果是import进另一个文件,那么__name__ == 当前文件名(不含.py后缀)。
# 4.所以if name == 'main' 表示如果是直接执行,就调用main()函数,作为程序入口。
# 5.如果是导入,那么就不会调用main(),只执行定义的函数,供其他模块调用。
# 6.main()函数通常用来包含需要直接执行的代码。
# 7.这样既可以把文件作为模块导入,又可以直接执行,这是一种很好的编程实践。
if __name__ == '__main__':
  main()


