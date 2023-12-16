import hashlib
import json
from dataclasses import dataclass

# Data class for personal information
@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str

# Base class for CreditCard
class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = cvv

    def give_bank_details(self, *args):
        return json.dumps(self, default=lambda o: bank_info.__dict__)

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        encode = hashlib.md5(cvv.encode())
        cvv = encode.hexdigest()
        self._cvv = cvv

    def order_card(self):
        pass

# CustomizedCard class inherits from CreditCard
class CustomizedCard(CreditCard):
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        super().__init__(client, account_number, credit_limit, grace_period, cvv)

    _credit_card: CreditCard = None

    @property
    def credit_card(self):
        return self._credit_card

    def order_card(self):
        return self._credit_card.order_card()

# GoldenCreditCard class inherits from CustomizedCard
class GoldenCreditCard(CustomizedCard):
    def order_card(self):
        return print(f"Golden credit card was issued")

# CorporateCreditCard class inherits from CustomizedCard
class CorporateCreditCard(CustomizedCard):
    def order_card(self):
        return print(f"Corporate credit card was issued")

# BankInfo class for storing bank-related information
class BankInfo:
    def __init__(self, bank_name, holder_name, credit_card: CreditCard):
        self.account_number = credit_card.account_number
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = []
        self.credit_history = []

    def transaction_list(self):
        return self.accounts_number.append(self.account_number)

# BankCustomer class representing a bank customer
class BankCustomer:
    def __init__(self, credit_card, personal_info=PersonalInfo):
        self.credit_card = credit_card
        self._personal_info = personal_info

    def give_bank_details(self, *args):
        return json.loads(credit_card.give_bank_details())

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, _personal_info: PersonalInfo):
        if isinstance(_personal_info, PersonalInfo):
            self._personal_info = PersonalInfo
        else:
            raise AttributeError(f"personal_info object must be of class Personal info")

# Function to print bank details of a BankCustomer
def client_code(bank_customer: "BankCustomer"):
    print(bank_customer.give_bank_details())

# Creating a CreditCard and BankInfo instances
credit_card = CreditCard("Mark", 535, 2772, 7277, 736)
bank_info = BankInfo("Hilton Bank", "Robertson Patricio", credit_card=credit_card)
bank_info.transaction_list()

# Creating a BankCustomer instance and printing bank details
bank_customer = BankCustomer(credit_card=credit_card)
info = json.dumps(credit_card.give_bank_details())
client_code(bank_customer=bank_customer)

# Creating instances of CustomizedCards and ordering them
gold_card = GoldenCreditCard("Mark", 535, 2772, 7277, 736)
corp_card = CorporateCreditCard("Mark", 535, 2772, 7277, 736)
gold_card.order_card()
corp_card.order_card()
