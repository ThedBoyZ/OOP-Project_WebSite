class Flight:
    def __init__(self, id, baggage, refund, reschedule, status, \
        departure_airport, departure_day , departure_time, arrival_airport , arrival_day , arrival_time , airline):
        self.id = id
        self.baggage = baggage
        self.refund = refund
        self.reschedule = reschedule
        self.status = status
        self.departure_airport = departure_airport
        self.departure_day = departure_day
        self.departure_time = departure_time
        self.arrival_airport = arrival_airport
        self.arrival_day = arrival_day
        self.arrival_time = arrival_time
        self.airline = airline
    
bkk_to_cnx = Flight('000001', 7, False, False, True, 'BKK', 'Sunday', '15:00', 'CNX', 'Sunday', '17:10', 'Thai Vietjet Air')
cnx_to_bkk = Flight('000002', 7, False, False, True, 'CNX', 'Monday', '10:00', 'BKK', 'Monday', '11:30', 'Nok Air')
dmk_to_cnx = Flight('000003', 15, False, False, True, 'DMK', 'Friday', '13:10', 'CNX', 'Friday', '15:30', 'Thai AirAsia')
