import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files.get("file")
    name = request.form.get("name")
    if file:
        file.save("file/" + name)
    else:
        return "file is none"
    return "ok"


@app.route("/delete", methods=['POST'])
def delete():
    name = request.form.get("name")
    if os.path.exists("file/" + name):
        os.remove("file/" + name)
    else:
        return "file is not exist"
    return "ok"


@app.route("/query", methods=['POST'])
def quary():
    file_list = os.listdir("file/")
    return str(file_list)
