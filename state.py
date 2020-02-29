class Account:
    def __init__(self):
        self._state = Silver(self)
        self.balance = 100

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def get_balance(self):
        return self._state.credit()

    def set_money(self, money):
        self._state.set_money(money)

    def get_money(self, money):
        self._state.get_money(money)


class Gold:
    def __init__(self, account):
        self._credit = 10
        self._account = account

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._acount = value

    def credit(self):
        return self._credit + self.account.balance

    def get_money(self, money):
        self._account.balance = self._account.balance - money
        self.state_control()

    def set_money(self, money):
        self._account.balance = self._account.balance + money
        self.state_control()

    def state_control(self):
        if self._account.balance < 25:
            self._account.state = Bronz(self._account)
        elif self._account.balance < 100:
            self._account.state = Silver(self._account)

class Silver:
    def __init__(self, account):
        self._credit = 5
        self._account = account

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    def credit(self):
        return self._credit + self.account.balance

    def get_money(self, money):
        self._account.balance = self._account.balance - money
        self.state_control()

    def set_money(self, money):
        self._account.balance = self._account.balance + money
        self.state_control()

    def state_control(self):
        if self._account.balance < 25:
            self._account.state = Bronz(self._account)
        elif self._account.balance >= 100:
            self._account.state =Gold(self._account)


class Bronz:
    def __init__(self, account):
        self._credit = 1
        self._account = account

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._acount = value

    def credit(self):
        return self._credit + self.account.balance

    def get_money(self, money):
        self._account.balance = self._account.balance - money
        self.state_control()

    def set_money(self, money):
        self._account.balance = self._account.balance + money
        self.state_control()

    def state_control(self):
        if self._account.balance > 100:
            self._account.state = Gold(self._account)
        elif self._account.balance >= 25:
            self._account.state =Silver(self._account)


account = Account()


account.get_money(90)
print(account.state.__class__.__name__) # Bronz
account.set_money(30)
print(account.state.__class__.__name__) # Silver
account.set_money(300)
print(account.state.__class__.__name__) # Gold
