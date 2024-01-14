from flask import Flask
#request object, Response object


app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello to batch4"

@app.route('/')
def hello_world():
    return 'hello world!!'
if __name__=="__main__":
    app.run(debug=True)
