class Payment:
    def __init__(self, method, currency, company_bank_account, payment_status, time_purchase, transaction_id):#, payment_data_list):
        self.__method = method
        self.__currency = currency
        self.__company_bank_account = company_bank_account
        self.__payment_status = payment_status
        self.__time_purchase = time_purchase
        self.__transaction_id = transaction_id
        # self.__payment_data_list = payment_data_list
    
    def process_payment():
        pass

    def check_payment_status():
        pass

    def update_payment_detail():
        pass

    def apply_coupon():
        pass

    def proceed_payment():
        pass

class PaymentCollection:
    def __init__(self, payment):
        self.__payment_list = []
        for attr in payment:
            if isinstance(attr, Payment):
                self.__payment_list.append(attr)
    
    def get_payment_status(self, index):
        return self.__payment_list[index]._Payment__payment_status
    
    def check_payment_status(self, transaction_id):
        for index in range(0, 3):
            if transaction_id == self.__payment_list[index]._Payment__transaction_id:
                return index
        

payment1 = Payment('InternetBanking', 'THB', 'SCB', 'Need Payment', '18:20', '3001')
payment2 = Payment('Paypal', 'THB', 'SCB', 'Payment Completed', '14:07', '3002')
payment3 = Payment('CreditCard', 'THB', 'SCB', 'Payment Completed', '02:23', '3003')

payment_list = PaymentCollection([payment1, payment2, payment3])
