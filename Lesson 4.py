# 1.
# class Transport:
#
#   def __init__(self, model: str, capacity: int, speed: float, is_electric: bool):
#
#     self.model = model
#     self.capacity = capacity
#     self.speed = speed
#     self.is_electric = is_electric
#
#   def get_info(self):
#
#     electric_type = "Electric" if self.is_electric else "Non-electric"
#     return (f"Model: {self.model}\n"
#             f"Capacity: {self.capacity}\n"
#             f"Average Speed: {self.speed} units/hour\n"
#             f"Type: {electric_type}")
#
#
# car = Transport("Tesla Model S", 5, 200, True)
# bus = Transport("City Bus 3000", 50, 60, False)
#
# print(car.get_info())
# print(bus.get_info())

# 2.
# class Transport:
#
#   def __init__(self, model, speed, capacity, color):
#     self.model = model
#     self.speed = speed
#     self.capacity = capacity
#     self.color = color
#
#   @staticmethod
#   def calculate_travel_time(distance, speed):
#
#     if speed <= 0:
#       return float('inf')
#     else:
#       return distance / speed
#
# # Example usage
# transport = Transport("Truck", 80, 15, "Red")
# distance = 500
# travel_time = transport.calculate_travel_time(distance, transport.speed)
#
# print(f"The {transport.model} will take approximately {travel_time:.2f} hours to travel {distance} km.")
#
# class Transport:
#
#   def __init__(self, make, model, year, color, capacity=None):
#     self.make = make
#     self.model = model
#     self.year = year
#     self.color = color
#     self.capacity = capacity
#
#   @staticmethod
#   def calculate_age(year):
#
#     current_year = 2024
#     return current_year - year
#
#   def get_full_name(self):
#
#     return f"{self.make} {self.model}"
#
#   def get_info(self):
#
#     capacity_info = f" (capacity: {self.capacity})" if self.capacity else ""
#     return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}{capacity_info}"
#
#
# car = Transport("Toyota", "Camry", 2020, "Silver")
# truck = Transport("Ford", "F-150", 2018, "Red", 3700)
#
# print(f"The car is a {car.get_full_name()} and is {Transport.calculate_age(car.year)} years old.")
# print(car.get_info())
# print(truck.get_info())


# 4.
# class Transport:
#
#     def __init__(self, name, speed, capacity, fuel_type, distance=0):
#         self.name = name
#         self.speed = speed
#         self.capacity = capacity
#         self.fuel_type = fuel_type
#         self.distance = distance
#
#     @staticmethod
#     def calculate_travel_time(distance, speed):
#
#         if speed <= 0:
#             raise ValueError("Speed cannot be zero or negative.")
#         return distance / speed
#
#     def get_transport_info(self):
#
#         return f"{self.name} (speed: {self.speed} km/h, capacity: {self.capacity}, fuel type: {self.fuel_type})"
#
#     def travel(self, distance):
#
#         if distance < 0:
#             raise ValueError("Travel distance cannot be negative.")
#         self.distance += distance


# car = Transport("Car", 80, 5, "Gasoline")
# bus = Transport("Bus", 60, 50, "Diesel")
# train = Transport("Train", 200, 1000, "Electricity", 100)  # Train has already traveled 100 km
#
#
# print(car.get_transport_info())
# print(bus.get_transport_info())
# print(train.get_transport_info())
#
# distance = 200
# travel_time_car = Transport.calculate_travel_time(distance, car.speed)
# print(f"Travel time for car over {distance} km: {travel_time_car:.2f} hours")
#
# car.travel(distance)
# print(f"Car traveled distance: {car.distance} km")


# 6.

# class Transport:
#
#     @staticmethod
#     def calculate_distance(speed, time):
#         return speed * time
#
#
#     @classmethod
#     def get_transport_types(cls):
#         return ["Car", "Truck", "Train", "Airplane"]
#
#     def __init__(self, model, capacity, speed, is_electric=False):
#         self.model = model
#         self.capacity = capacity
#         self.speed = speed
#         self.is_electric = is_electric
#
#     def travel(self, duration):
#         distance = Transport.calculate_distance(self.speed, duration)
#         print(f"The {self.model} travelled {distance:.2f} km.")
#
#     def get_info(self):
#         info = f"Model: {self.model}\nCapacity: {self.capacity}\n"
#         info += f"Speed: {self.speed} km/h\n"
#         info += "Electric" if self.is_electric else "Non-electric"
#         return info
#
#     def __repr__(self):
#         return f"Transport(model='{self.model}', capacity={self.capacity}, speed={self.speed}, is_electric={self.is_electric})"
#
#
# car = Transport("Tesla Model S", 5, 250, True)
# truck = Transport("Volvo FH16", 30000, 90)
# train = Transport("Bullet Train", 500, 300)
#
#
# car.travel(2)
# print(truck.get_info())
# print(train)

# 7.
# class Transport:
#
#     def __init__(self, model, speed, capacity, color):
#         self.model = model
#         self.speed = speed
#         self.capacity = capacity
#         self.color = color
#
#     def calculate_travel_time(distance, speed):
#
#         if speed <= 0:
#             raise ValueError("Speed cannot be zero or negative.")
#         return distance / speed
#
#     def move(self, destination):
#
#         print(f"The {self.color} {self.model} is moving to {destination}.")
#
#     def get_info(self):
#
#         return f"{self.model} ({self.color}) - Max Speed: {self.speed} km/h, Capacity: {self.capacity} passengers"
#
#     def __repr__(self):
#
#         return f"Transport(model='{self.model}', speed={self.speed}, capacity={self.capacity}, color='{self.color}')"
#
#
# car = Transport("Tesla Model S", 250, 5, "red")
# bus = Transport("Volvo 9700", 100, 70, "yellow")
# train = Transport("Shinkansen E5", 320, 800, "white")
# airplane = Transport("Boeing 787", 900, 350, "blue")
# ship = Transport("Queen Mary 2", 30, 2500, "white")
#
# travel_time = Transport.calculate_travel_time(500, car.speed)
# print(f"Travel time for car to destination: {travel_time:.2f} hours")
# car.move("Los Angeles")
# bus.move("New York")
#
# print(train.get_info())
# print(ship)
