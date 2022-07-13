from abc import abstractmethod


class Storage:
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        if self.get_free_space() > 0:
            if self.get_free_space() >= count:
                print(f'Товар {name} добавлен')
                if name in self.items.keys():
                    self.items[name] = self.items[name] + count
                else:
                    self.items[name] = count
                return True
            else:
                print('не хватает места, нужно уменьшить')
        else:
            print('нет свободного места')
        return False

    def remove(self, name, count):
        if name in self.items.keys():
            if self.items[name] >= count:
                print('есть нужное кол-во')
                self.items[name] = self.items[name] - count
                return True
            else:
                print('нет такого кол-ва')
        else:
            print('такого товара нет')
            return False
        return False

    def get_free_space(self):
        count = 0

        for item in self.items.values():
            count += item

        return self.capacity - count

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        self.items = {}
        self.capacity = 20
        self.limit = 5

    def add(self, name, count):
        if self.get_unique_items_count() < 5:
            super().add(name, count)
            return True
        else:
            print('не хватает места, нужно уменьшить')
            return False


class Request:
    def __init__(self, str_input):
        data = str_input.split(' ')

        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]

    def __rep__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
