from classes import Request, Shop, Store


if __name__ == '__main__':
    shop = Shop()
    store = Store()

    store.add('собачки', 5)
    store.add('яблоко', 2)
    store.add('машинки', 8)

    print('на складе есть:')
    print(store.get_items())

    user_answer = input('введите строчку такого типа: "Доставить 3 собачки из склад в магазин"')
    data_request = Request(user_answer)

    result_store = store.remove(data_request.product, data_request.amount)
    if result_store:
        print(f'Курьер забрал {data_request.amount} {data_request.product} со склад')
        print(f'курьер везет {data_request.amount} {data_request.product} со склад в магазин')
        result_shop = shop.add(data_request.product, data_request.amount)
        if not result_shop:
            store.add(data_request.product, data_request.amount)
        else:
            print(f'курьер доставил {data_request.amount} {data_request.product} в магазин')

    print('на складе есть:')
    print(store.get_items())

    print('в магазине есть:')
    print(store.get_items())





