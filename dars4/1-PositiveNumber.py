class PositiveNumber:
    def __get__(self,inst,owner):
        try:return inst.num
        except:pass
    
    def __set__(self,inst,value:int):
            if type(value)==int and value>0:
                try:inst.num=value
                except:print('unexpected error occured...')
            else:raise ValueError('Only positive number expected')

    def __delete__(self,inst):
        try:del inst.num
        except:print('It\'s already removed or wasn\'t created at all')
    
class ToCheck:
    number=PositiveNumber()

positive=ToCheck()
print(positive.number)

positive.number=123
print(positive.number)

positive.number=-123