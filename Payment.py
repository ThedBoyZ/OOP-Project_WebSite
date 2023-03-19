class Payment:
    def __init__(self, method, currency, company_bank_account, payment_status, time_purchase, transaction_id, payment_data_list):
        self.__method = method
        self.__currency = currency
        self.__company_bank_account = company_bank_account
        self.__payment_status = payment_status
        self.__time_purchase = time_purchase
        self.__transaction_id = transaction_id
        self.__payment_data_list = payment_data_list

    def process_payment():
        pass

    def check_booking_status():
        pass

    def update_payment_detail():
        pass

    def apply_coupon():
        pass

    def proceed_payment():
        pass

class PaymentCollection:
    def __init__(self, payment_detail, payment_method, method_detail):
        self._payment_detail = payment_detail
        self._payment_method = payment_method
        self._method_detail = method_detail
    
    def get_payment_method():
        pass 
    
    def get_method_detail():
        pass

class InternetBankingTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card
    
class OverTheCounterTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class EWalletTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class CreditCARDTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class DebitCardTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card

class PayPalTransaction:
    def __init__(self, logo, name__on_card):
        self.__logo = logo
        self.__name_on_card = name__on_card