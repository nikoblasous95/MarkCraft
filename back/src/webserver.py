from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.store_seller import StoreSeller, StoreSellerRepository


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/stores", methods=["GET"])
    def stores_get():
        all_stores = repositories["stores"].get_stores()
        return object_to_json(all_stores)

    @app.route("/api/stores/<id>", methods=["GET"])
    def get_store_by_id(id):
        stores_by_id = repositories["stores"].get_store_by_store_id(id)
        return object_to_json(stores_by_id)

    @app.route("/api/items/<item_id>", methods=["GET"])
    def get_item_by_id(item_id):
        item_by_id = repositories["items"].get_items_by_id(item_id)
        return object_to_json(item_by_id)

    return app
