from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1> Welcome to Cloudstakes<h1>"

@app.route('/post', methods = ["POST"])
def postJsonHandler():
    content = request.get_json()
    print (content)
    return 'JSON posted'

if __name__ == '__main__':
    app.run()
