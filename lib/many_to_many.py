class Book:
    _instances = []

    def __init__(self, title):
        self.title = title
        self._instances.append(self)
        self.contracts = []

    def __str__(self):
        return f"{self.title}"

    def contracts(self):
        return self.contracts

    def authors(self):
        return [contract.author for contract in self.contracts]

    @staticmethod
    def all():
        return Book._instances

class Author:
    _instances = []

    def __init__(self, name):
        self.name = name
        self._instances.append(self)
        self.contracts = []

    def __str__(self):
        return f"{self.name}"

    def contracts(self):
        return self.contracts

    def books(self):
        return [c.book for c in self.contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts)

    @staticmethod
    def all():
        return Author._instances

class Contract:
    _instances = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(date, str):
            raise Exception('Date must be a string')
        if not isinstance(royalties, int):
            raise Exception('Royalties must be an integer')
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.author.contracts.append(self)
        self.book.contracts.append(self)
        Contract._instances.append(self)

    def __str__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date='{self.date}', royalties={self.royalties})"

    @classmethod
    def all(cls):
        return cls._instances

    @classmethod
    def contracts_by_date(cls, date):
        matching_contracts = [contract for contract in cls._instances if contract.date == date]
        return sorted(matching_contracts, key=lambda x: x.author.name)