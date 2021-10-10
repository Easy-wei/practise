from bottle import run, route, template, abort, error, redirect, request, response


@route("/")
@route("/hello/")
@route('/hello/<name>')
def greet(name="Stranger"):
    return template("<b> Hello {{name}},how are you? </b>", name=name)


@error(404)
def error404(error):
    return "Nothing here,sorry"
# 上述网页错误


@route("/right/url")
def hello(filename):
    return "Hello world!"

    # http错误和重定向


@route("/restricted")
def restricted():
    abort(401, "Sorry,access denied.")
# 生成错误页面

def restricted_area():
    username = request.get_cookie("account", secret="some-secret-key")
    if username:
        return template("hello {{name}},welcome back!", name=username)
    else:
        return "<p>You are not logged in. Access denied</p>"



@route("/wrong/url")
def wrong():
    redirect("/right/url")
# 重定向


@route("/hello")
def hello_again():
    if request.get_cookie("visited"):
        return "welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return 'Hello there! Nice to meet you!'

# 测试效果：第一次打开网页"http://localhost:8080/hello",显示hello there... ，然后刷新网页，即可得到 welcomeback


run(host="localhost", port=2000, debug=True)
