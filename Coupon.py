class Coupon:
    def __init__(self, code, discount, description, promo_period, travel_period):
        self.code = code
        self.discount = discount
        self.description = description
        self.promo_period = promo_period
        self.travel_period = travel_period
    
class CouponCollection: 
    def __init__(self):
        self._coupon_detail = []

    def add_coupon(self, coupon):
        self._coupon_detail.append(coupon)

    def delete_coupon(self, coupon):
        self._coupon_detail.remove(coupon)
    
    def all_coupon(self):
        return self._coupon_detail

    # Show All Available Promo Codes on Webpage
    def coupon_home(self, index):
        return [self._coupon_detail[index].discount, self._coupon_detail[index].promo_period, self._coupon_detail[index].travel_period]
    
    # Show More Details
    def descript_coupon_detail(self, index):
        return [self._coupon_detail[index].code, self._coupon_detail[index].discount, self._coupon_detail[index].description, self._coupon_detail[index].promo_period, self._coupon_detail[index].travel_period]

# ------------------------------------- Instances ----------------------

# Collect 2 Objects from Coupon in CouponCollection
coupon_list = CouponCollection()
coupon_list.add_coupon(Coupon('APZKTC10', 10, 'Get 10% discount using promo code APZKTC10 with no minimum transactions for all airlines', '30-06-2023', ['01-04-2023', '31-12-2024']))
coupon_list.add_coupon(Coupon('APZKTC05', 5, 'Get 5% discount using promo code APZKTC05 with no minimum transaction for all airlines', '30-06-2023', ['01-04-2023', '31-01-2025']))
coupon_list.add_coupon(Coupon('APZFLIGHTTHB23', 2, 'Get 2% discount using promo code APZFLIGHTTHB23 with no minimum transaction for all airlines', '31-05-2023', ['01-05-2023', '31-12-2024']))
coupon_list.add_coupon(Coupon('APZFLIGHTTHB77', 7, 'Get 7% discount using promo code APZFLIGHTTHB77 with no minimum transaction for all airlines', '31-05-2023', ['01-05-2023', '31-12-2024']))
coupon_list.add_coupon(Coupon('APZFLIGHTTHB202', 20, 'Get 20% discount using promo code APZFLIGHTTHB202 with no minimum transaction for all airlines', '31-05-2023', ['01-05-2023', '31-12-2024']))

if __name__ == '__main__':
    
    # --------------------------- UI -----------------------------------------
    # Show All Available Promo Codes
    print('All Promo Codes:')
    print('-' * 40)
    # for index in range(0, 2):
    #     print(f'Code ({index+1})')
    #     for attr in coupon_list.coupon_home(index):
    #         print(attr)
    print(coupon_list.all_coupon())

    # Click for More Details
    selected_promo_index = int(input('Select Promo Code for More Details:\n(1)  (2)\n'))
    # Return Promo Code Detail to User
    print('-' * 40)
    print(coupon_list.all_coupon()[selected_promo_index - 1])
    print('-' * 40)
