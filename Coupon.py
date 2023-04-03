class Coupon:
    def __init__(self, code, discount, description, promo_period, travel_period):
        self.code = code
        self.discount = discount
        self.description = description
        self.promo_period = promo_period
        self.travel_period = travel_period
    
    def update_payment_coupon():
        pass

class CouponCollection:
    def __init__(self, coupon_detail):
        self._coupon_detail = []
        # Collect Object from Coupon in CouponCollection
        for attr in coupon_detail:
            if isinstance(attr, Coupon):
                self._coupon_detail.append(attr)

    # Show All Available Promo Codes on Webpage
    def coupon_home(self, index):
        return [self._coupon_detail[index].discount, self._coupon_detail[index].promo_period, self._coupon_detail[index].travel_period]
    
    # Show More Details
    def descript_coupon_detail(self, index):
        return [self._coupon_detail[index].code, self._coupon_detail[index].discount, self._coupon_detail[index].description, self._coupon_detail[index].promo_period, self._coupon_detail[index].travel_period]


# ------------------------------------- Instances for Test 0 ----------------------
# Create 2 Objects from Coupon
coupon1 = Coupon('dc10', 10, 'new user', '31-12-2023', ['01-01-2024', '31-01-2024'])
coupon2 = Coupon('dc20', 20, 'premium user', '31-07-2023', ['01-01-2023', '31-12-2024'])

# Collect 2 Objects from Coupon in CouponCollection
coupon_list = CouponCollection([coupon1, coupon2])

# --------------------------- UI -----------------------------------------
# Show All Available Promo Codes
print('All Promo Codes:')
print('-' * 40)
for index in range(0, 2):
    print(f'Code ({index+1})')
    for attr in coupon_list.coupon_home(index):
        print(attr)
    print('-' * 40)

# Click for More Details
selected_promo_index = int(input('Select Promo Code for More Details:\n(1)  (2)\n'))

# Return Promo Code Detail to User
print('-' * 40)
list_index = 0
for attr in coupon_list.descript_coupon_detail(selected_promo_index-1):
    attr_name = ['Code', 'Discount', 'Description', 'Promo Period', 'Travel Period']
    print(f'{attr_name[list_index]}: {attr}')
    list_index+=1
print('-' * 40)
