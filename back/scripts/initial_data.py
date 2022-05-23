def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.store_seller import StoreSeller, StoreSellerRepository
    from src.domain.items import Items, ItemsRepository

    database_path = "data/database.db"

    store_seller_repository = StoreSellerRepository(database_path,ItemsRepository(database_path))
    items_repository = ItemsRepository(database_path)

    item_txiflo = Items(
        item_id="item-50",
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
        items=[],
    )

    item_paula = Items(
        item_id="item-40",
        item_name="Pulsera",
        item_description="Esta es una pulsera bien de wapa",
        item_category="Pulseras",
    )

    tienda_de_paula = StoreSeller(
        store_id="store-4",
        store_name="Paulis",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos pal insta",
        store_category="Bisuteria",
        seller_name="Paula Sista",
        seller_email="paula@gmail.com",
        seller_phone="68546755",
        items=[],
    )

    tienda_de_claudio = StoreSeller(
        store_id="store-3",
        store_name="Claudios",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos",
        seller_name="Claudio Clase",
        seller_email="claudio@gmail.com",
        seller_phone="685256755",
        store_category="Deportiva",
        items=[]
    )
    item_claudio = Items(
        item_id="item-30",
        item_name="Bicicleta montaña",
        item_description="Esta es una bicicleta todo de wapa",
        item_category="Bicis",
        
    )

    item_txiflo_2 = Items(
        item_id="item-51",
        item_name="Edit de fotos djh",
        item_description="Este es un edid de fotos super mega wapo",
        item_category="Ediciones de foto",
        
    )

    tienda_de_txomin = StoreSeller(
        store_id="store-2",
        store_name="Txomins",
        store_description="Tienda de venta de boletos de loteria",
        store_category="Boletos",
        seller_name="Txomin Ramirez",
        seller_email="txomingl@gmail.com",
        seller_phone="685254582",
        items = []
        
    )
   
    item_txomin = Items(
        item_id="item-20",
        item_name="boleto de euromillones",
        item_description="Boleto de euromillones",
        item_category = "Boleto"
    )
    tienda_de_flan = StoreSeller(
        store_id="store-1",
        store_name="Flanagans",
        store_description="Tienda de venta de diseños y ediciones de videos y fotos",
        store_category="Fotos ",
        seller_name="Lan Flanagan",
        seller_email="lanflan@gmail.com",
        seller_phone="6852545656",
        store_images="pexels-fox-3829227.jpg",
        items=[]
    )

    
    item_flan = Items(
        item_id="item-10",
        item_name="Puerto clasic",
        item_description="Esto es un edid de fotos de surf",
        item_category="Fotos de surf",
       
    )

    ## CATEGORIAS DE TIENDAS

    # CATEGORIAS DE ITEMS

    store_seller_repository.save_store_seller(tienda_de_txiflo)
    items_repository.save_items(item_txiflo)
    items_repository.save_items(item_txiflo_2)
    items_repository.save_store_seller_items("store-5", ["item-50","item-51"])
    
    store_seller_repository.save_store_seller(tienda_de_paula)
    items_repository.save_items(item_paula)
    items_repository.save_store_seller_items("store-4",["item-40"])

    store_seller_repository.save_store_seller(tienda_de_claudio)
    items_repository.save_items(item_claudio)
    items_repository.save_store_seller_items("store-3",["item-30"])

    store_seller_repository.save_store_seller(tienda_de_txomin)
    items_repository.save_items(item_txomin)
    items_repository.save_store_seller_items("store-2",["item-20"])

    store_seller_repository.save_store_seller(tienda_de_flan)
    items_repository.save_items(item_flan)
    items_repository.save_store_seller_items("store-1",["item-10"])

    # stores_repository.save_stores(tienda_de_flan)

    # items_repository.save_items(item_flan)
    # stores_repository.save_stores(tienda_de_txomin)

    # items_repository.save_items(item_txomin)
    # stores_repository.save_stores(tienda_de_claudio)

    # items_repository.save_items(item_claudio)


if __name__ == "__main__":
    main()
