from flake8 import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Delavigne CI app!"
