from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Welcome to Cloudstakes<h1>"

@app.route('/post', methods = ['POST', 'GET'])
def post():

    print(request.data)
    return '' 

if __name__ == '__main__':
    app.run()
