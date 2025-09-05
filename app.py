from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>我的第一个网站上线了！</h1> <p>真是太简单了！</p>'

if __name__ == '__main__':
    app.run(debug=True)