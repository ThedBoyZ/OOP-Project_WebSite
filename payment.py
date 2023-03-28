from datetime import datetime

class Payment:
    def __init__(self, method, currency, company_bank_account, status, time_purchase, transaction_id):
        self.__method = method
        self.__currency = currency
        self.__company_bank_account = company_bank_account
        self.__status = status
        self.__time_purchase = datetime(time_purchase)
        self.__transaction_id = transaction_id

class TransactionInfo:
    def __init__(self, name, logo, name__on_card):
        self.name = name
        self.logo = logo
        self.name_on_card = name__on_card

