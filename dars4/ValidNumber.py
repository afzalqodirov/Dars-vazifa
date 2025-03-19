import os
os.system('cls')

class ValidFullNameDescriptor:
    def __init__(self, fullname):
        self.fullname = fullname


    def __get__(self, instance, owner):
        if instance is None:
            return self.fullname
        try:return instance.name.split()
        except:pass
        
    def __set__(self, instance, value):
        if isinstance(value, str):
            names = value.split()
            if len(names) == 2:
                instance.name = names
            else:
                raise ValueError('Full name should contain exactly two names.')
        else:
            raise TypeError('Full name should be a string.')
        
        
class MyClass:
    fname = ValidFullNameDescriptor("Temirov Elbek")

f1 = MyClass()
print(f1.fname ) 
print(MyClass.fname)
f1.fname = "Ism Familiya"
print(f1.fname ) 


            
