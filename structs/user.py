from structs.wallet import Wallet


class User:
    def __init__(self, chat_id: int, wallet: Wallet=None):
        self.chat_id: int = chat_id
        if not wallet:
            wallet = Wallet()
        self.wallet: Wallet = wallet

    def reprJSON(self):
        return dict(chat_id=self.chat_id, wallet=self.wallet.reprJSON())

    def info(self):
        return f'''
            Ваш кошелек: {self.wallet.id}\nВаш баланс: {self.wallet.balance} GNG
            '''

    @staticmethod
    def from_json(json):
        chat_id = json.get('chat_id')
        wallet = Wallet.from_json(json.get('wallet'))
        if not chat_id or not wallet:
            return None
        return User(chat_id=chat_id, wallet=wallet)
