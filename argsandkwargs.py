def testargs(*args):
    return sum(args)

print(testargs(1,2,1,5,4,56,4,6,4,6,4,5))


def testkwargs(**kwargs): ## Key word arguments
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("i did not find any fruites here")

def myfunc(*args,**kwargs):
    print(f"i would like {args[0]} {kwargs['food']}")

testkwargs(fruit='apple',veggie='tomato')

myfunc(1,2,3,4,5,6,food='mago',choc='jelly')

listof=[1,2,3,45]

listof.append(56)
print(listof)