class Car:
  def __init__(self, make, model, numOfDoors):
    self.make = make
    self.model = model
    self.numOfDoors = numOfDoors
  def turningRight(self):
    print("The car is turning right.")
  def brake(self):
    print("The car is braking.")
  def accelerate(self):
    print("The car is accelerating.")

class Jaguar (Car):
  pass
j = Jaguar("Land Rover", "ABC", 4)
print(j.make)
print(j.model)
j.brake()
j.accelerate()