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

# Class representing a Credit Card
class CreditCard:
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = cvv

    def give_bank_details(self, *args):
        # Serialize the CreditCard instance to JSON
        return json.dumps(self, default=lambda o: bank_info.__dict__)

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        # Hash the CVV using MD5 before setting it
        encode = hashlib.md5(cvv.encode())
        cvv = encode.hexdigest()
        self._cvv = cvv

# Class representing Bank Information
class BankInfo:
    def __init__(self, bank_name, holder_name, credit_card: CreditCard):
        # Extract relevant information from the CreditCard instance
        self.account_number = credit_card.account_number
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = []
        self.credit_history = []

    def transaction_list(self):
        # Record the account number in the transaction list
        return self.accounts_number.append(self.account_number)

# Class representing a Bank Customer
class BankCustomer:
    def __init__(self, credit_card, personal_info=PersonalInfo):
        # Initialize with a credit card and optional personal information
        self.credit_card = credit_card
        self._personal_info = personal_info

    def give_bank_details(self, *args):
        # Deserialize the JSON representation of the CreditCard instance
        return json.loads(credit_card.give_bank_details())

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, _personal_info: PersonalInfo):
        if isinstance(_personal_info, PersonalInfo):
            self._personal_info = PersonalInfo
        else:
            raise AttributeError(f"personal_info object must be of class PersonalInfo")

# Function to print bank details of a BankCustomer
def client_code(bank_customer: "BankCustomer"):
    print(bank_customer.give_bank_details())

# Create a CreditCard instance
credit_card = CreditCard("Mark", 535, 2772, 7277, 736)

# Create a BankInfo instance with the CreditCard
bank_info = BankInfo("Hilton Bank", "Robertson Patricio", credit_card=credit_card)
bank_info.transaction_list()

# Create a BankCustomer instance with the CreditCard
bank_customer = BankCustomer(credit_card=credit_card)

# Serialize the CreditCard details to JSON and print
info = json.dumps(credit_card.give_bank_details())
client_code(bank_customer=bank_customer)
