#--------parent class----------

class Car: 
    def __init__(self,brand,model,price):
       self.brand=brand
       self.__model=model
       self.price=price
    def enginetype(self):
     print(f"{self.brand} has liquid engine")
    def speed(self):
     print(f"{self.brand} has 40 km/h")
    def info(self):
       print(f"{self.brand}'s model {self.__model} which costs {self.price}")

   #---------child class-----------   
   
class Tata(Car):
   def __init__(self,brand,model,price):
      super().__init__(brand,model,price) 
   def enginetype(self):
          print(f"{self.brand} has v-type cylinder arrangement")
class Suzuki(Car):
      def __init__(self,brand,model,price):
       super().__init__(brand,model,price) 
      def speed(self):
        print(f"{self.brand} has 80 km/h")

automobile1=Tata("Tata","Nexon",965690) 
automobile2=Tata("Tata","safari",19064990)       
automobile3=Tata("Tata","Tigor",245790)
automobile4=Suzuki("suzuki","swift",689990)
automobile5=Suzuki("suzuki","ertiga",245890)

automobile1.info()
automobile2.info()
automobile3.info()
automobile1.enginetype()
automobile3.speed()
automobile4.speed()
automobile4.enginetype()


