#!/usr/bin/env python3

import connexion

from pub_chem_index import encoder

app = None

def main():
    global app
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'PubChemIndex'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
