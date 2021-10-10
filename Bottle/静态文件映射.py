from bottle import Route, static_file,run


@Route("//static/<filename>")
def server_static(filename):
    return static_file(filename, root="/path/to/your/static/files")

# 上述只能匹配一条路径，"/path/to/your/static/files",为了响应子目录下的文件请求，改为path过滤器的定义如下


@Route("//static/<filepath>")
def server_static(filepath):
    return static_file(filepath, root="/path/to/your/static/files")
# 使用 root='./static/files' 这样的相对路径的时候，请注意当前工作目录 (./) 不一定是项目文件夹。


# 静态文件返回

@Route("/images/<filename:re:.*\.png")
def send_image(filename):
    return static_file(filename, root="/path/to/image/files", mimetype="image/png")
# 上述采用直接路径，下述采用 path过滤器办法，static_file()


@Route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="/path/to/static/files")


"""
强制下载
大多数浏览器在知道MIME类型的时候，会尝试直接调用相关程序来打开文件(例如PDF文件)。
如果你不想这样，你可强制浏览器只是下载该文件，甚至提供文件名。
"""


@Route("/downlaod/<filename:path")
def download(filename):
    return static_file(filename, root="/path/to/static/files", download=filename)
