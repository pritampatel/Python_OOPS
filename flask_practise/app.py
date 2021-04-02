from flask import Flask

app=Flask(__name__)

@app.route("/")
def greet():
    return "Hi There!"

@app.route('/store/<string:name>')
def store_name(name):
    return name

if __name__=="__main__":
    app.run(port=5000)