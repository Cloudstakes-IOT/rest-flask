from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Welcome to Cloudstakes<h1>"

@post('/esp')
def index():
    data = request.body.read()
    print(data) 

if __name__ == '__main__':
    app.run()
