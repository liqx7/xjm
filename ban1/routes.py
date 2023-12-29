# coding utf-8
def route_index():
  # 组装http
  header='HTTP/1.1 200 OK\r\n Content-Type: text/html\r\n'
  body='<h1>Hello</h1><img src="/doge.gif" />'
  r=header+'\r\n'+body
  return r.encode(encoding='utf-8')

def route_image():
    # 在Python中,'rb'表示以二进制格式打开一个文件用于读:
    #
    # r表示以只读方式打开文件。
    # b表示以二进制模式打开,而不是文本模式
    with open('doge.gif','rb') as f:
        header=b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n'
        img =header+b'\r\n'+f.read()
        return img

def page(name):
    with open(name,encoding='utf-8') as f:
        return f.read()

def route_msg():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body=page('html_basic.html')
    r=header+'\r\n'+body
    return r.encode(encoding='utf-8')

def route_static():
    """
        静态资源的处理函数, 读取图片并生成响应返回
        <img src="/static?file=doge.gif"/>
        GET /static?file=doge.gif
        path, query = response_for_path('/static?file=doge.gif')
        path  '/static'
        query = {
            'file', 'doge.gif',
        }
        """
    
    return ''


route_dict={
    '/':route_index,
    '/doge.gif':route_image,
    '/msg':route_msg,
    '/static':route_static()
}