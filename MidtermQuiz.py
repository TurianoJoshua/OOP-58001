class conversion:
  def __init__(self,meter):
    self.__meter = meter

  def display(self):
    print(f"The conversion of meter", self.__meter,"in centimeter is",(self.__meter*100))
    print(f"The conversion of meter", self.__meter,"in kilometer is", (self.__meter/1000))
    print(f"The conversion of meter", self.__meter,"in inches is", (self.__meter*39.37))

class metertocenti(conversion):
  pass
class metertokilo(conversion):
  pass
class metertoinches(conversion):
  pass

meter = conversion(float(input("Enter the meter: ")))
meter.display()
meter = conversion(float(input("Enter the meter: ")))
meter.display()
meter = conversion(float(input("Enter the meter: ")))
meter.display()