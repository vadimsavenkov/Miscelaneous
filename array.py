class Array:
def __init__(self, _size)
      
        self.size =_size
        self.aList =[]
    
      for i in range(_size):
        self.aList.append(0)
        

    def append(self, _element):
        self.aList.append(_element)
        
    def get(self, _index):
        return self.aList.index(_index)

class Matrix:
    pass

testobj1 = Array(5)
print(testobj1.aList)
print(testobj1.size)
testobj1.append(5)
print(testobj1.aList) 
print(testobj1.get(0))       

