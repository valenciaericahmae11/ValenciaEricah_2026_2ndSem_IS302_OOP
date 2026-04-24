class Payment_EIV:
    def pay_EIV(self_EIV):
        print("Processing payment")

class CashPayment_EIV(Payment_EIV):
    def pay_EIV(self_EIV):
        print("Payment made using cash")

class CardPayment_EIV(Payment_EIV):
    def pay_EIV(self_EIV):
        print("Payment made using credit card")

payments_EIV = [CashPayment_EIV(), CardPayment_EIV()]
for p_EIV in payments_EIV:
    p_EIV.pay_EIV()
