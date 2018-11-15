from flask import Flask
from flask import jsonify
from flask import request


customers = [
    {"id": 1, "name": "Google"},
    {"id": 2, "name": "Duck Duck GO"},
    {"id": 3, "name": "Yandex"},
    {"id": 4, "name": "Bing"},
    {"id": 5, "name": "Yahoo"},
    {"id": 6, "name": "Baidu"},
    {"id": 7, "name": "AOL"},
]


def make_app():
    app = Flask(__name__)

    @app.route("/")
    def welcome():
        return "Welcome to Qmatch Dummy REST!"

    @app.route("/customers", methods=["GET", "POST"])
    def customer_endpoint():

        if request.method == "GET":
            # -- List all customers
            return jsonify(customers), 200

        if request.method == "POST":
            # -- Create customers
            return "", 200

    @app.route("/customers/<int:customer_id>", methods=["GET"])
    def customer_detail_endpoint(customer_id):
        if request.method == "GET":
            # -- Get customer detail
            customer = next(
                (customer for customer in customers if customer["id"] == customer_id),
                None,
            )

            if not customer:
                return "", 404

            return jsonify(customer), 200

    return app


if __name__ == "__main__":
    app = make_app()
    app.run(port=800)
