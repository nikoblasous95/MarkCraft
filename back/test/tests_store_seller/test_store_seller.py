from email import header
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.store_seller import StoreSellerRepository, StoreSeller
from src.domain.items import Items, ItemsRepository


def set_up():

    stores_repository = StoreSellerRepository(temp_file(), ItemsRepository)
    app = create_app(repositories={"stores": stores_repository})
    client = app.test_client()
    return client


def test_should_return_empty_list_of_stores():
    client = set_up()
    response = client.get("/api/stores")

    assert response.json == []


def test_should_return_store_in_database():
    items_repository = ItemsRepository(temp_file())
    store_seller_repository = StoreSellerRepository(temp_file(), items_repository)
    app = create_app(
        repositories={"stores": store_seller_repository, "items": items_repository}
    )
    client = app.test_client()

    item_txiflo = Items(
        item_id="item-1",
        item_name="Pelotas de perro",
        item_description="Esto es una pelota para perros de la ostia",
        item_category="Pelotas",
    )

    tienda_de_txiflo = StoreSeller(
        store_id="store-5",
        store_name="Txiflo",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos para perros",
        seller_name="Txiflito",
        store_category="Perrunas",
        seller_email="txiflo@gmail.com",
        seller_phone="66786755",
    )
    items_repository.save_items(item_txiflo)

    store_seller_repository.save_store_seller(tienda_de_txiflo)

    items_repository.save_store_seller_items(
        tienda_de_txiflo.store_id, [item_txiflo.item_id]
    )

    response = client.get("/api/stores")

    assert response.json == [
        {
            "store_id": "store-5",
            "store_name": "Txiflo",
            "store_description": "Tienda de venta de diseños y ediciones de videos y fotos para perros",
            "store_category": "Perrunas",
            "seller_name": "Txiflito",
            "seller_email": "txiflo@gmail.com",
            "seller_phone": "66786755",
            "store_images": [],
            "items": [
                {
                    "item_id": "item-1",
                    "item_name": "Pelotas de perro",
                    "item_description": "Esto es una pelota para perros de la ostia",
                    "item_category": "Pelotas",
                }
            ],
        }
    ]


def test_should_return_just_1_store_when_we_find_them_by_id():
    temp = temp_file()
    items_repository = ItemsRepository(temp)
    store_seller_repository = StoreSellerRepository(temp, items_repository)
    app = create_app(
        repositories={"stores": store_seller_repository, "items": items_repository}
    )
    client = app.test_client()

    item_txiflo = Items(
        item_id="item-1",
        item_name="Pelotas de perro",
        item_description="Esto es una pelota para perros de la ostia",
        item_category="Pelotas",
    )

    tienda_de_txiflo = StoreSeller(
        store_id="store-5",
        store_name="Txiflo",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos para perros",
        seller_name="Txiflito",
        store_category="Perrunas",
        seller_email="txiflo@gmail.com",
        seller_phone="66786755",
        store_images=[],
        items=[],
    )
    items_repository.save_items(item_txiflo)

    store_seller_repository.save_store_seller(tienda_de_txiflo)
    items_repository.save_store_seller_items(
        tienda_de_txiflo.store_id, [item_txiflo.item_id]
    )

    response = client.get("/api/stores/store-5")

    assert response.json == {
        "store_id": "store-5",
        "store_name": "Txiflo",
        "store_description": "Tienda de venta de diseños y ediciones de videos y fotos para perros",
        "store_category": "Perrunas",
        "seller_name": "Txiflito",
        "seller_email": "txiflo@gmail.com",
        "store_images": [],
        "seller_phone": "66786755",
        "items": [
            {
                "item_id": "item-1",
                "item_name": "Pelotas de perro",
                "item_description": "Esto es una pelota para perros de la ostia",
                "item_category": "Pelotas",
            }
        ],
    }


def test_validate_admin():
    temp = temp_file()
    items_repository = ItemsRepository(temp)
    store_seller_repository = StoreSellerRepository(temp, items_repository)
    app = create_app(
        repositories={"stores": store_seller_repository, "items": items_repository}
    )
    client = app.test_client()

    body = {"email": "txiflo@gmail.com", "phone": "66786755"}

    tienda_de_txiflo = StoreSeller(
        store_id="store-5",
        store_name="Txiflo",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos para perros",
        seller_name="Txiflito",
        store_category="Perrunas",
        seller_email="txiflo@gmail.com",
        seller_phone="66786755",
    )
    store_seller_repository.save_store_seller(tienda_de_txiflo)

    response = client.post("/api/adminLogin", json=body)

    assert response.status_code == 200
    assert response.data == b'{"store_id":"store-5"}\n'
