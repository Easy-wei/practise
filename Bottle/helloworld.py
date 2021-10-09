import bottle as bt

@bt.route('/hello/<name>')

def index(name):
    return bt.template('<b>hello {{name}}</b>!',name = name )

bt.run(host = "localhost",port= 8080)

#运行本文件后在在浏览器访问http://localhost:8080/hello/(任意)
