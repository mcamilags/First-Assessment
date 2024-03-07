
class Finances:
    def __init__(self):
        self.accounts = {}

    def open_account(self, user):
        self.accounts[user.get_id()] = {'money': 0, 'transactions': []}

    def make_payment(self, user, amount):
        user_id = user.get_id()
        if user_id in self.accounts:
            if self.accounts[user_id]['money'] >= amount:
                self.accounts[user_id]['money'] -= amount
                self.accounts[user_id]['transactions'].append({'type': 'payment', 'amount': amount})
                return f"A payment of ${amount} was made. Current balance: ${self.accounts[user_id]['money']}."
            else:
                return "Insufficient funds."
        else:
            return "You need to open an account to make a payment."

    def add_funds(self, user, amount):
        self.accounts[user.get_id()]['money'] += amount
        return f"Funds of ${amount} were added. Current balance: ${self.accounts[user.get_id()]['money']}."


