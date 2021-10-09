from bottle import run, route, template


@route('/hello')
def hell0():
    return "hello world!"


@route('/')
@route('/hello/<name>')
def greet(name="Stranger"):
    return template('hello {{name}},how are you?', name=name)


run(host="localhost", port=1000, debug=True)

#测试一个py中绑定多个url，同时表明多个url可以返回同一个函数，绑定动态url
