from flask import Flask

last_sync = None


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            return {'status': 200, 'last_sync': last_sync, 'message': 'ok', 'data': 500}
        except Exception as e:
            return {'status': 400, 'message': str(e)}, 400
    return app
