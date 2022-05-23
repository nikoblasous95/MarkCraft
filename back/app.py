import sqlite3

from src.webserver import create_app
from src.domain.store_seller import StoreSellerRepository

from src.domain.items import ItemsRepository


database_path = "data/database.db"

repositories = {
    "stores": StoreSellerRepository(database_path, ItemsRepository(database_path)),
    "items": ItemsRepository(database_path),
}


app = create_app(repositories)


app.run(debug=False, host="0.0.0.0", port="5000")
