




'''
my_list=[1, 2, 3, 4, 5]
other_list=[2, 4, 6, 8, 10, 12, 14]

def fizzBuzz(list):
    for num in list:
        if num%2 == 1:
            print("buzz")
        else:
            print("fizz")

fizzBuzz(other_list)
'''



def fizzbuzz(num):
    s=""
    if num%3 == 0:
        s+="fizz"
    if num%5 == 0:
        s+="buzz"
    else:
        print(num)
    print(s)
    
fizzbuzz(15)

'''
num=0
my_list=[1, 1]

def fizzbuzz(list):
    num=sum(list)
    if num%2 == 1:
        print("fizz")
    else:
        print("buzz")
    
fizzbuzz(my_list)
'''

