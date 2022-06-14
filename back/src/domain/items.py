import sqlite3

from pytest import Item


class Items:
    def __init__(
        self,
        item_id,
        item_name,
        item_description,
        item_category,
    ):
        self.item_id = item_id
        self.item_name = item_name
        self.item_description = item_description
        self.item_category = item_category

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_description": self.item_description,
            "item_category": self.item_category,
        }


class ItemsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
        CREATE TABLE if not EXISTS "items" (
	"item_id"	TEXT,
	"item_name"	TEXT,
	"item_description"	TEXT,
	"item_category"	TEXT,
	PRIMARY KEY("item_id")
);

CREATE TABLE if not EXISTS "storeItems" (
	"store_id"	TEXT,
    "item_id"	TEXT,
	FOREIGN KEY("item_id") REFERENCES "items"("item_id"),
	FOREIGN KEY("store_id") REFERENCES "storeSeller"("store_id")
);

        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.executescript(sql)
        conn.commit()

    def get_items(self):
        sql = """SELECT * FROM items"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        all_items = [Items(**item) for item in data]
        return all_items

    def modify_item(self, item_id, item):
        sql = """
        UPDATE items
            SET item_name= :item_name, item_description= :item_description,item_category=:item_category
            WHERE item_id = :item_id 
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        params = item.to_dict()
        params["id"] = item_id
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def get_items_by_id(self, item_id):
        sql = """SELECT  * FROM items where item_id=:item_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"item_id": item_id})
        data = cursor.fetchone()
        item = Items(**data)

        return item

    def save_items(self, item):
        sql = """
        insert into items (item_id,item_name,item_description,item_category) values (:item_id, :item_name, :item_description, :item_category)
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, item.to_dict())
        conn.commit()

    def get_items_id_from_one_store(self, store_id):
        sql = """
        select item_id from storeItems where store_id =:store_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"store_id": store_id})
        items_id = cursor.fetchall()
        result = []
        for item in items_id:
            result.append(item[0])
        print(result)
        return result

    def get_items_by_store_seller_id(self, store_id):
        conn = self.create_conn()
        cursor = conn.cursor()
        sql_items = """select i.item_id, i.item_name , i.item_description, i.item_category
            from storeItems si, items i 
            where si.item_id=i.item_id and store_id=:store_id"""
        cursor.execute(sql_items, {"store_id": store_id})
        items = cursor.fetchall()
        items = [Items(**item).to_dict() for item in items]

        conn.close()
        return items

    def save_store_seller_items(self, store_id, items):
        sql = """
        DELETE FROM storeItems WHERE store_id = :store_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"store_id": store_id},
        )
        conn.commit()
        sql_store_items = (
            """INSERT INTO storeItems (item_id,store_id) VALUES (:item_id,:store_id)"""
        )

        for item in items:
            cursor.execute(sql_store_items, {"store_id": store_id, "item_id": item})
        conn.commit()
        conn.close()
