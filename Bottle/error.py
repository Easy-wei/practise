from unicodedata import name
from bottle import redirect, route, abort, error, run, template


@route("/")
@route("/hello")
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


@route("/wrong/url")
def wrong():
    redirect("/right/url")
# 重定向


run(host="localhost", port=2000, debug=True)
