from cloudharness.utils.server import init_flask
import flask, os
from flask import redirect
from pub_chem_index import encoder

app = init_flask(title="Olphactory pubchem index API", webapp=True)

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
