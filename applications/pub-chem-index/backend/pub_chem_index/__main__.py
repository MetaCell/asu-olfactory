from cloudharness.utils.server import init_flask
import flask, os
from flask import redirect
from pub_chem_index import encoder

app = init_flask(title="Olphactory pubchem index API", webapp=False)

def init_webapp_routes(app, www_path):
    @app.route('/test', methods=['GET'])
    def test():
        return 'routing ok'

    @app.route('/', methods=['GET'])
    def index():
        return flask.send_from_directory(www_path, 'index.html')

    @app.route('/<path:path>', methods=['GET'])
    def send_webapp(path):
        return flask.send_from_directory(www_path, path)

    @app.errorhandler(404)
    def page_not_found(error):
        # when a 404 is thrown send the "main" index page
        # unless the first segment of the path is in the exception list
        first_segment_path = flask.request.full_path.split('/')[1]
        if first_segment_path in ['api', 'static', 'test']:  # exception list
            return error
        return index()

    @app.route('/static/<path:path>', methods=['GET'])
    def send_static(path):
        return flask.send_from_directory(os.path.join(www_path, 'static'), path)

def main():
    www = os.path.dirname(os.path.abspath(__file__)) + "/www"
    with app.app_context():
        init_webapp_routes(app, www)
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
