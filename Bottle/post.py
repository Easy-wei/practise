import re
from bottle import post, get, request, route


@get("/login")  # or @route("/login")
def login():
    return <form action = "/login" method = "post"
           username: < input name = "username" type = "text"/>
           password: < input  name = "password" type = "password"/>
           <input value = "login" type = "submit" / >
           </form >
"""
aaa
"""

@post("/login") #or @route("/login",method = "POST")
def do_login():
    username = request.forms.get("username")
    password = request.forms.get('password')
    if check_login (username,password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    