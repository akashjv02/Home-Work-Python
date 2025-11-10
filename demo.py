
# # # # class Point:
# # # #     def __init__(self, x=0, y=0):
# # # #         self.x = x
# # # #         self.y = y

# # # #     def __str__(self):
# # # #         return "({0},{1})".format(self.x, self.y)

# # # #     def __add__(self, other):
# # # #         x = self.x + other.x
# # # #         y = self.y + other.y
# # # #         return Point(x, y)


# # # # p1 = Point(1, 2)
# # # # p2 = Point(2, 3)

# # # # print(p1+p2)


# # # # from abc import ABC, abstractmethod 
  
# # # # class Polygon(ABC): 
  
# # # #     # abstract method 
# # # #     def noofsides(self): 
# # # #        pass
  
# # # # class Triangle(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("Triangle have 3 sides") 
  
# # # # class Pentagon(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("Pentagon have 5 sides") 
  
# # # # class Hexagon(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("Hexagon have 6 sides") 
  
# # # # class Quadrilateral(Polygon): 
  
# # # #     # overriding abstract method 
# # # #     def noofsides(self): 
# # # #         print("Quadrilateral have 4 sides") 
  
# # # # # Driver code 
# # # # R = Triangle() 
# # # # R.noofsides() 
  
# # # # K = Quadrilateral() 
# # # # K.noofsides() 
  
# # # # R = Pentagon() 
# # # # R.noofsides() 
  
# # # # K = Hexagon() 
# # # # K.noofsides() 

# # # # p = Polygon()
# # # # p.noofsides()


# # # class Geeks: 
# # #      def __init__(self): 
# # #           self._age = 0
       
# # #      # function to get value of _age 
# # #      def get_age(self): 
# # #          print("getter method called") 
# # #          return self._age 
       
# # #      # function to set value of _age 
# # #      def set_age(self, a): 
# # #          print("setter method called") 
# # #          self._age = a 
  
# # #      # function to delete _age attribute 
# # #      def del_age(self): 
# # #          del self._age 
     
# # #      age = property(get_age, set_age, del_age)  
  
# # # mark = Geeks() 
  
# # # mark.age = 10
  
# # # print(mark.age) 
# # # del mark._age
# # # print(mark._age)
# # # mark.set_age(1000000000000000000000000000)


# # a = 50
# # def test():
# #   print(a)
# #   test()

# # print(a)


# from datetime import datetime

# timestamp = 1591014926
# date_time = datetime.fromtimestamp(timestamp)

# print("Date time object:", date_time)

# d = date_time.strftime("%Y/%m/%d, %H:%M:%S")
# print("Output 2:", d)	

# d = date_time.strftime("%d %b, %Y")
# print("Output 3:", d)

# d = date_time.strftime("%d %B, %Y")
# print("Output 4:", d)

# d = date_time.strftime("%I%p")
# print("Output 5:", d)


def reverse(string): 
    string = string[::-1] 
    return string 
  
s = "Python is Awesome."
  
print ("The original string  is : ",s) 
print ("The reversed string(using extended slice syntax) is : ",reverse(s)) 
