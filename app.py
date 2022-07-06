from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Welcome to Cloudstakes<h1>"

@app.route('/post', methods = ['POST', 'GET'])
def post():
    print(request.get_json())
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run()
