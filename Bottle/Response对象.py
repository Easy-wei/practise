"""
HTTP状态码，HTTP响应头，用户cookie等元数据都保存在response 的对象里。
接着被传输给浏览器。你可直接操作这些元数据或使用一些更方便的函数。
在API章节可查到所有相关API(详见 Response )，这里主要介绍一些常用方法
"""

import re
from bottle import debug, request, response, run, route, error, template, redirect

"""
HTTP状态码 控制着浏览器的行为，默认为 200 OK 。
多数情况下，你不必手动修改 Response.status 的值，
可使用 abort() 函数或return一个 HTTPResponse 实例(带有合适的状态码)。
虽然所有整数都可当作状态码返回，但浏览器不知道如何处理 HTTP标准 中定义的那些状态码之外的数字，
你也破坏了大家约定的标准
"""


# 响应头
@route("/wiki/<page>")
def wiki(page):
    response.set_header("Content_language", "en")

# Cookie，如下访问


@route("/hello")
def hello_again():
    if request.get_cookie("visited"):
        return "welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return 'Hello there! Nice to meet you!'

# 测试效果：第一次打开网页"http://localhost:8080/hello",显示hello there... ，然后刷新网页，即可得到 welcomeback


@route('/login')
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        response.set_cookie("account", username, secret="some-secret-key")
        return template("<p> Welcome {{name}}! You are now logged in.</p>")
    else:
        return "<p> Login failed.</p>"


@route("/restricted")
def restricted_area():
    username = request.get_cookie("account", secret="some-secret-key")
    if username:
        return template("hello {{name}},welcome back!", name=username)
    else:
        return "<p>You are not logged in. Access denied</p>"


run(host='localhost', port=8080, debug=True)
