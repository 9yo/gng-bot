import uuid


class Wallet:
    def __init__(self, id: str=uuid.uuid4().hex, balance: float=0):
        self.id: str = id
        self.balance = balance

    def reprJSON(self):
        return dict(id=self.id, balance=self.balance)

    @staticmethod
    def from_json(json):
        id = json.get('id', None)
        balance = json.get('balance', None)
        if None in [id, balance]:
            return None
        return Wallet(id, balance)
