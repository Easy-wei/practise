from bottle import run, route, template, abort


@route('/hello')
def hell0():
    return "hello world!"


@route('/')
@route('/hello/<name>')
def greet(name="Stranger"):
    return template('<b> Hello {{name}},how are you?</b>', name=name)


@route("/restricted")
def restricted():
    abort(401, "Sorry, access denied.")
# 生成错误页面


run(host="localhost", port=1000, debug=True)

# 测试一个py中绑定多个url，同时表明多个url可以返回同一个函数，绑定动态url
