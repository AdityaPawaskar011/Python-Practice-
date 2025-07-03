from records import car_records
class Car:

    def __init__(self,car_brand,car_model,car_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_year = car_year

    def rec(self):
        print(f"Car brand :{self.car_brand} Car Model: {self.car_model} Car Year: {self.car_year}")


for car in car_records:
    car=Car(car["brand"],car["model"],car["year"])
    car.rec()


