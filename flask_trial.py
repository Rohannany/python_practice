from flask import Flask
app = Flask(__name__)


#useful when we want to log the requests
@app.before_request
def before():
    print("This is executed before each request")

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hey %s!'% name

@app.route('/home/')
def home():
    return 'Homepage'

@app.route('/contact')
def contact():
    return 'contact page'

@app.route('/teapot/')
def teapot():
    return "Teapot"
if __name__ == '__main__':
    app.run(debug = True)
