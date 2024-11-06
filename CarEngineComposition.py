# Define the Engine class
class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.type_of_engine} engine is now running.")
        else:
            print(f"{self.type_of_engine} engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.type_of_engine} engine is now stopped.")
        else:
            print(f"{self.type_of_engine} engine is already stopped.")


# Define the Car class that contains an Engine instance
class Car:
    def __init__(self, make, model, engine_type):
        self.make = make
        self.model = model
        self.engine = Engine(engine_type)  # Composition: Car has an instance of Engine

    def start_car(self):
        print(f"Starting the {self.make} {self.model}...")
        self.engine.start()  # Calling Engine's start method

    def stop_car(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()  # Calling Engine's stop method


# Create an instance of Car with a specific engine
my_car = Car("Toyota", "Corolla", "V6")

# Start and stop the car
my_car.start_car()
my_car.stop_car()
