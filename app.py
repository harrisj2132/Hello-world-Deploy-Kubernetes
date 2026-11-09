from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello test world'

@app.route('/new')
def new():
    return 'I am running my first ci pipeline'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)