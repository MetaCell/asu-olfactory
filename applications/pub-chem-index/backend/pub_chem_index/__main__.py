#!/usr/bin/env python3
import flask
import connexion

from pub_chem_index import encoder


def main():
    www_path = "static"
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'PubChemIndex'},
                pythonic_params=True)

    @app.route('/', methods=['GET'])
    def index():
        return flask.send_from_directory(www_path, 'index.html')

    @app.route('/<path:path>', methods=['GET'])
    def send_webapp(path):
        return flask.send_from_directory(www_path, path)

    app.run(port=8080)


if __name__ == '__main__':
    main()
