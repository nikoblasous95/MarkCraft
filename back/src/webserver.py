from flask import Flask, request
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import re
from src.domain.email_sender import Email
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
        print(all_stores)
        return object_to_json(all_stores)

    @app.route("/api/storeModify/<id>", methods=["PUT"])
    def modify_store(id):
        data = request.json
        print(data)
        store = StoreSeller(**data)
        repositories["stores"].modify_store(id, store)
        return "hello", 200

    @app.route("/api/stores/<id>", methods=["GET"])
    def get_store_by_id(id):
        stores_by_id = repositories["stores"].get_store_by_store_id(id)
        return object_to_json(stores_by_id)

    @app.route("/api/items/<item_id>", methods=["GET"])
    def get_item_by_id(item_id):
        item_by_id = repositories["items"].get_items_by_id(item_id)
        return object_to_json(item_by_id)

    @app.route("/api/adminLogin", methods=["POST"])
    def login():
        data = request.json
        response = repositories["stores"].validate_login(data)
        result = {}
        result["store_id"] = response
        return result, 200

    @app.route("/api/buyingItems", methods=["POST"])
    def getting_seller_info():
        data = request.json
        allItems = data["allItems"]
        email = data["email"]
        regular_expression = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        if re.match(regular_expression, email) is not None:
            good_email = email
        else:
            return "El email proporcionado no es valido", 500
        result = []
        for item in allItems:
            item_id = item["item_id"]
            item_name = item["item_name"]
            seller_info = repositories["stores"].get_seller_info_for_buyer(item_id)
            seller_info.update({"item_id": item_id})
            seller_info.update({"item_name": item_name})
            email = Email
            sending_email = email.send_email(seller_info)
            print(seller_info)
            result.append(seller_info)
        return "", 200

        # for element in result:
        #     email_subject = "Informacion para su compra"
        #     sender_email_address = "marrkcraft@gmail.com"
        #     receiver_email_address = good_email
        #     email_smtp = "smtp.gmail.com"
        #     email_password = "pruebaemail95"
        #     message = EmailMessage()
        #     message["Subject"] = email_subject
        #     message["From"] = sender_email_address
        #     message["To"] = receiver_email_address

        #     seller_name = element["seller_name"]
        #     seller_email = element["seller_email"]
        #     seller_phone = element["seller_phone"]
        #     item_name_for_email = element["item_name"]
        #     item_id_for_email = element["item_id"]
        #     body = f"""
        #     Le enviamos los datos y la informacion del vendedor:
        #         Nombre del vendedor: {seller_name}
        #         Telefono del vendedor: {seller_phone}
        #         Email del vendedor: {seller_email}
        #         Nombre del item: {item_name_for_email}
        #         Id del item: {item_id_for_email}
        #     """
        #     message.set_content(body)
        #     server = smtplib.SMTP(email_smtp, "587")
        #     server.ehlo()
        #     server.login(sender_email_address, email_password)
        #     server.send_message(message)
        #     server.quit()
        # return "", 200

    return app
