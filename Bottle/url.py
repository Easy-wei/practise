from bottle import run, static_file, template, route


@route("/object/<id:int>")
def callback(id):
    assert isinstance(id, int)


@route("show/<name:re:[a-z]+>")
def callback(name):
    assert name.isalpha()


@route("/static/<path:path>")
def callback(path):
    return static_file(path, ...)
