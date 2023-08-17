from flask import Flask, request
from calculator import calculate
from prometheus_flask_exporter import PrometheusMetrics

def create_server():
    app = Flask(__name__)
    metrics = PrometheusMetrics(app)
    @app.route('/', methods=['GET'])
    def calc():
        parameter = request.args.get('expr')
        if parameter is None:
            return 'This server is calculator.<br>' \
                   'To calculate your expression use GET request with parameter expr.'
        return calculate(parameter)
    return app
