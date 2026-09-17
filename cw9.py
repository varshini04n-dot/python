class vehicle:
    def __init__(self,vehicle_id,base_rate):
        self._vehicle_id=vehicle_id
        self._base_rate=base_rate
    def display_details(self):
        return "Vehicle ID: {}\nBase Rate: {}".format(self._vehicle_id,self._base_rate)
    def rental_charge(self):
        return  0.0
class car(vehicle):
    def __init__(self,num_seats,vehicle_id,base_rate):
        self.num_seats=num_seats
        super().__init__(vehicle_id,base_rate)
    def rental_charge(self):
        return self._base_rate*self.num_seats
class bike(vehicle):
    def __init__(self,bike_type,vehicle_id,base_rate):
        self.bike_type=bike_type
        super().__init__(vehicle_id,base_rate)
    def rental_charge(self):
        return self._base_rate*0.5
def calculate_rental(vehicle):
    return vehicle.rental_charge()
obj1=car(4,"CAR001",100)
obj2=bike("Scooter","BIKE001",50)
print(obj1.display_details())
print("Rental Charge:", calculate_rental(obj1))
print(obj2.display_details())
print("Rental Charge:", calculate_rental(obj2))

        