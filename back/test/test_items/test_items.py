from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.items import Items, ItemsRepository


def set_up():
    items_repository = ItemsRepository(temp_file())
    app = create_app(repositories={"items": items_repository})
    client = app.test_client()
    return client


def test_get_item_by_id():
    items_repository = ItemsRepository(temp_file())
    app = create_app(repositories={"items": items_repository})
    client = app.test_client()

    item_txiflo = Items(
        item_id="item-1",
        item_name="Pelotas de perro",
        item_description="Esto es una pelota para perros de la ostia",
        item_category="Pelotas",
    )
    items_repository.save_items(item_txiflo)
    response = client.get("/api/items/item-1")

    assert response.json == {
        "item_id": "item-1",
        "item_name": "Pelotas de perro",
        "item_description": "Esto es una pelota para perros de la ostia",
        "item_category": "Pelotas",
    }
