def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Car:
    wheels = 4 #Class variable 
    def __init__(self,brand,color):#Instance Variable.
        self.brand = brand
        self.color = color
    @log_action    
    def show_details(self):
        print(f"This is a {self.color} {self.brand} car with {Car.wheels} wheels.")

    @log_action
    def drive(self):
        speed = 60  #Local Variable
        print(f"The {self.brand} is driving at {speed}km/h")

    @classmethod
    @log_action
    def change_wheels(cls,new_wheel_count):
        cls.wheels = new_wheel_count
        print(f"Wheel count is changed to {cls.change_wheels}")

    @staticmethod
    @log_action
    def Shekhar():
        print("Welcome to the car Showroom! ")

#Create Car object
Car1 = Car("Bolero","White")
Car2 = Car("Tata Curve", "Red")  

#Use Methods
Car.Shekhar()
Car1.show_details()
Car1.drive()
Car.change_wheels(6)
Car2.show_details