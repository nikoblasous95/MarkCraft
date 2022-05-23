import sqlite3

from src.domain.items import ItemsRepository

# database_path = "data/database.db"


class StoreSeller:
    def __init__(
        self,
        store_id,
        store_name,
        store_description,
        store_category,
        seller_name,
        seller_email,
        seller_phone,
        store_images=None,
        items=None,
    ):
        self.store_id = store_id
        self.store_name = store_name
        self.store_description = store_description
        self.store_category = store_category
        self.seller_name = seller_name
        self.seller_email = seller_email
        self.seller_phone = seller_phone
        self.items = items
        self.store_images = store_images

    def to_dict(self):
        return {
            "store_id": self.store_id,
            "store_name": self.store_name,
            "store_description": self.store_description,
            "store_category": self.store_category,
            "seller_name": self.seller_name,
            "seller_email": self.seller_email,
            "seller_phone": self.seller_phone,
            "store_images": self.store_images if self.store_images else [],
            "items": self.items if self.items else [],
        }


class StoreSellerRepository:
    def __init__(self, database_path, items_repository):
        self.datababase_path = database_path
        self.items_repository = items_repository
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.datababase_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
                CREATE TABLE if not EXISTS "storeSeller" (
	"store_id"	TEXT,
	"store_name"	TEXT,
	"store_description"	TEXT,
	"store_category"	TEXT,
	"seller_name"	TEXT,
	"seller_email"	TEXT,
	"seller_phone"	TEXT,
    "store_images"	BLOB,
	"items"	TEXT,
	PRIMARY KEY("store_id")
);
        """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close

    def get_stores(self):
        sql = """SELECT * FROM storeSeller"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        result = []
        for item in data:
            store_seller = StoreSeller(**item)
            store_id = store_seller.store_id
            store_seller.items = self.items_repository.get_items_by_store_seller_id(
                store_id
            )
            result.append(store_seller)
        return result

    def save_store_seller(self, store):
        sql = """insert into storeSeller (store_id,store_name,store_description,seller_name,seller_email,seller_phone,store_category) 
        values (:store_id,:store_name, :store_description, :seller_name, :seller_email, :seller_phone,  :store_category)"""

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, store.to_dict())
        conn.commit()
        return ""

    def get_store_by_store_id(self, store_id):
        sql = """SELECT * FROM storeSeller where store_id=:store_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"store_id": store_id})
        data = cursor.fetchone()
        if dict(data):
            store_seller = StoreSeller(**data)
            store_seller.items = self.items_repository.get_items_by_store_seller_id(
                store_id
            )
        return store_seller
