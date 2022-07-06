from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Welcome to Cloudstakes<h1>"

@app.route('/post', methods = ['POST', 'GET'])
def post():
    data = json.loads(request.data)
    text = data.get("text",None)
    if text is None:
        return jsonify({"message":"text not found"})
    else:
        return jsonify(data)

if __name__ == '__main__':
    app.run()
