from itertools import *

def comprehensions():
    list1 = []
    list1 = [x for x in range(10) if x < 5]
    return print(list1)
    # for calling it, use comprehensions()

def lambda_function(y):  #anonymous functions
    x = lambda listx: [x*y for x in range(10) for y in range (5)] + listx
    return x(y) # calling the x lambda function
    # for calling it, use "print (lambda_function([1000]))"

def map_function():
    z = range(2)
    y = list(map (lambda x: (x*2), z))  # it calls a function for a sequence of parameters
    return y
    # for calling it, use "print (map_function())"

def filer_function():
    z = range(10)
    y = list (filter(lambda z: z > 5, z))  # it can filter z
    # for calling it, use "print (map_function())"
    return y
def iter_function ():
    z = range(10)
    my_iter = iter(z)  #it uses less memory than a for loop because you can only
                       # access the next element of you sequence and there is no
                       # neet to keep all the elements
    return next(my_iter), next(my_iter), next(my_iter), next(my_iter)

def generator_function(x,y):
    for i in range(x):
        print('i is %d' % i)   # generator can control the behavior of a loop, it can suspend the operation and then return
        print('y is %d' % y)   # it later.
        yield i * y            # in opposite a regular funtions returns all the iterated values
def generator_expression():
    gen_exp = (x for x in range(5))
    return next(gen_exp), next(gen_exp)

def chain_function():
    list1 = [1,2,3,'t', 'u']
    list2 = [5,9,7, 'd', 'u']
    for i in chain(list1, list2):
        print (i)

def count_function():  #     it increments a count using a start point and a value of incrementation
    for i in count(10,2.5):
        if i < 50:
            print (i)
        else:
            break

def slices():
    list1 = list(range(10))
    list2 = list1 [5:10:2]
    print (list2)

    list2 = list(islice(range(10), 5,10,2))
    print (list2)

def my_decorator(target_function):
    def function_wrapper():
        return print("Python is such a " + target_function() + " language!")
    return function_wrapper()

@my_decorator
def target_function():
    return "cool"


if '__main__' == __name__:
   #print (lambda_function([1000]))
   #print (map_function())
   #print(filer_function())
   #print (iter_function())

   #my_object = generator_function(10,5)
   #print (next(my_object), next(my_object), next(my_object))

   #print(generator_expression())

   #chain_function()

   #count_function()

   #slices()

   target_function()
