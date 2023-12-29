# coding: utf-8
import socket
import ssl

def log(*args,**kwargs):
    print('log, ',*args,**kwargs)

def parsed_url(url):
    protocol='http'
    if url[:7]=='http://':
        u=url.split('://')[1]
    elif url[:8]=='https://':
        protocol='https'
        u=url.split('://')[1]
    else:
        u=url
        # https://g.cn:1234/hello
        # g.cn:1234/hello
    i=u.find('/')
    if i==-1:
        host=u
        path='/'
    else:
        host=u[:i]
        path=u[i:]

    port_dict={
        'http':80,
        'https':443
    }
    port =port_dict[protocol]
    if ':' in host:
        h=host.split(':')
        host=h[0]
        port=int(h[1])

    return protocol, host,port,path

def socket_by_protocol(protocol):
    #     根据协议返回一个 socket 实例
    if protocol == 'http':
        s=socket.socket()
    else:
        s=ssl.wrap_socket(socket.socket())

    return  s

def response_by_socket(s):
    #       参数是一个 socket 实例
    #     返回这个 socket 读取的所有数据
    response=b''
    buffer_size =1024
    while True:
        r=s.recv(buffer_size)
        # 如果当前缓冲区的数据已读取完,s.recv()会返回一个空字节字符串。
        if len(r)==0:
            break
        response+=r
    return response

def parsed_response(r):
    # 1表示只拆分一次,将r拆分成两个部分
    header,body=r.split('\r\n\r\n',1)
    h=header.split('\r\n')
    status_code=h[0].split()[1]
    status_code=int(status_code)

    headers={}
    for line in h[1:]:
        k, v = line.split(': ')
        headers[k]=v
    return status_code,headers,body


def get(url):
    #     解析url
    protocol,host,port,path=parsed_url(url)
    s=socket_by_protocol(protocol)
    s.connect((host,port))

    request='GET {} HTTP/1.1\r\nHost:{}\r\nConnection: close\r\n\r\n'.format(path,host)
    ecoding='utf-8'
    s.send(request.encode(ecoding))

    response=response_by_socket(s)
    # log('get response, ', response)
    r=response.decode(ecoding)

    status_code,headers,body=parsed_response(r)

    if status_code in [301,302]:
        url=headers['Location']
        return get(url)

    return status_code,headers,body

def test_parsed_url():
    http='http'
    https='https'
    host='g.cn'
    path='/'
    test_items=[
        ('http://g.cn', (http, host, 80, path)),
        ('http://g.cn/', (http, host, 80, path)),
        ('http://g.cn:90', (http, host, 90, path)),
        ('http://g.cn:90/', (http, host, 90, path)),
        #
        ('https://g.cn', (https, host, 443, path)),
        ('https://g.cn:233/', (https, host, 233, path)),
    ]

    for t in test_items:
        url, expected=t
        u=parsed_url(url)

        e='parsed_url ERROR, ({}) ({}) ({})'.format(url,u,expected)
        # 在Python中，return a, b和a, b = function()中的a, b实际上是元组。
        assert u==expected,e

def test_parsed_response():
    response = 'HTTP/1.1 301 Moved Permanently\r\n' \
               'Content-Type: text/html\r\n' \
               'Location: https://movie.douban.com/top250\r\n' \
               'Content-Length: 178\r\n\r\n' \
               'test body'
    status_code,header,body=parsed_response(response)
    assert status_code==301
    # 在Python字典中，可以使用.keys()方法获取字典中所有的键。这个方法返回一个包含所有键的迭代器对象。
    # 由于迭代器对象不能直接计算长度，所以需要将其转换为列表。通过调用list()函数，我们可以将迭代器对象转换为一个列表。
    assert len(list(header.keys()))==3
    assert body == 'test body'

def test_get():
    urls = [
        'http://movie.douban.com/top250',
        'https://movie.douban.com/top250',
    ]
    for u in urls:
        get(u)

def test():
    # test_parsed_url()
    # test_parsed_response()
    test_get()

def main():
    url = 'http://movie.douban.com/top250'
    status_code,headers,body=get(url)
    log('main',status_code)

if __name__ == '__main__':
    # test()
    main()