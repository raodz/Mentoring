class Order:
    def __init__(self, idx: int, name: str, price: float):
        self.id = idx
        self.name = name
        self.price = price

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: PLN {self.price}'


class Manager:
    def __init__(self, orders):
        self.orders = orders

    def add_order(self, order: Order):
        self.orders[order] = self.orders.get(order, 0) + 1

    def sell_product(self, product_id: int):
        for order in self.orders:
            if order.id == product_id:
                self.orders[order] -= 1
                return

    def __str__(self):
        return f'Current orders: {self.orders}'


def main():
    table = Order(200, 'Table', 260)
    chair = Order(201, 'Chair', 140)
    bed = Order(202, 'Bed', 500)
    desk = Order(203, 'Desk', 180)
    some_manager = Manager({table: 2, chair: 8, bed: 1})
    print(some_manager)
    some_manager.add_order(bed)
    print(some_manager)
    some_manager.add_order(desk)
    print(some_manager)
    some_manager.sell_product(201)
    print(some_manager)


if __name__ == '__main__':
    main()
