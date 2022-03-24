
from flask import Flask, jsonify

app = Flask(__name__)

book = [
    {"id" : 1, "name" : "1"},
    {"id" : 2, "name" : "2"}
]
#只从服务器获取数据：GET请求
#前端需要把数据发送给服务器：POST请求


#url动态传参

@app.route("/book/<int:book_id>", methods = ["GET"])
def book_detail(book_id):
    print(book_id)
    return "Success"


@app.route('/book/list', methods = ["GET", "POST"])
def book_list():
    return jsonify(book)

@app.route('/', )
def hello_world():
    return "Hello World"

if __name__ == "__main__":

    app.run()


