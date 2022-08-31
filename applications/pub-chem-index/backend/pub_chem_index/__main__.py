from cloudharness.utils.server import init_flask
import flask, os
from flask import redirect
from pub_chem_index import encoder

app = init_flask(title="Olphactory pubchem index API", webapp=False)

@app.route("/", defaults={"file": "index.html"})
def index(file):
    root_dir = os.path.dirname(os.getcwd())
    return flask.send_from_directory(os.path.join(root_dir, 'static', "index.html")

@app.route("/test1", defaults={"file": "index.html"})
def index(file):
    root_dir = os.path.dirname(os.getcwd())
    return flask.send_from_directory(os.path.join(root_dir, 'static', "index.html")

@app.route("/test2", defaults={"file": "index.html"})
def index(file):
    root_dir = os.path.dirname(os.getcwd())
    return flask.send_from_directory(os.path.join(root_dir, 'www', "index.html")

@app.route("/metacell")
def nn():
    return flask.send_from_directory("www", "index.html")

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
