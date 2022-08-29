from cloudharness.utils.server import init_flask
import flask, os
from pub_chem_index import encoder

app = init_flask(title="Olphactory pubchem index API", webapp=False)

@app.route("/", defaults={"file": "index.html"})
def index(file):
    return flask.send_from_directory("www", "index.html")

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
