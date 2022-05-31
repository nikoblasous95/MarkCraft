from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.store_seller import StoreSellerRepository, StoreSeller
from src.domain.items import Items, ItemsRepository


def set_up():

    stores_repository = StoreSellerRepository(temp_file(), ItemsRepository)
    app = create_app(repositories={"stores": stores_repository})
    client = app.test_client()
    return client

def test_should_return_seller_info():
    tmp_db = temp_file()
    items_repository = ItemsRepository(tmp_db)
    stores_repository = StoreSellerRepository(tmp_db, items_repository)
    app = create_app(repositories={"stores": stores_repository,
                                    "items":items_repository})
    client = app.test_client()

    tienda_de_txiflo = StoreSeller(
        store_id="store-5",
        store_name="Txiflo",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos para perros",
        seller_name="Txiflito",
        store_category="Perrunas",
        seller_email="txiflo@gmail.com",
        seller_phone="66786755",
        items=[],
    )

    item_txiflo = Items(
        item_id="item-50",
        item_name="Pelotas de perro",
        item_description="Esto es una pelota para perros de la ostia",
        item_category="Pelotas",
    )


    stores_repository.save_store_seller(tienda_de_txiflo)
    items_repository.save_items(item_txiflo)
    items_repository.save_store_seller_items("store-5",["item-50"])
    response = stores_repository.get_seller_info_for_buyer("item-50")

    assert response == {
        "seller_name": "Txiflito",
        "seller_email": "txiflo@gmail.com",
        "seller_phone": "66786755"
    }


    