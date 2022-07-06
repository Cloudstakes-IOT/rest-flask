from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Welcome to Cloudstakes<h1>"

@app.route('/post', methods = ['POST', 'GET'])
def post():
    params = {
        'thing1': request.values.get('thing1')
    }
    return json.dumps(params)

if __name__ == '__main__':
    app.run()
