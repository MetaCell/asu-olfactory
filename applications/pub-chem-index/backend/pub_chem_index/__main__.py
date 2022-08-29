from cloudharness.utils.server import init_flask
import flask, os
from pub_chem_index import encoder

app = init_flask(title="Olphactory pubchem index API", webapp=False)

def main():
    www_path = "static"

    @app.route('/', methods=['GET'])
    def index():
        return flask.send_from_directory(www_path, 'index.html')

    @app.route('/<path:path>', methods=['GET'])
    def send_webapp(path):
        return flask.send_from_directory(www_path, path)

    app.run(host='0.0.0.0', port=os.getenv('PORT', 5001))

if __name__ == '__main__':
    main()
