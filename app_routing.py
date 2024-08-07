from flask import Flask

app = Flask(__name__)

# @app.route("/hello/<name>")
def hello(name):
    return f"Welcome {name}"

# @app.route("/")
# def homepage():
#     return "Homepage"

app.add_url_rule("")

if __name__ == "__main__":
    app.run(debug=True)


