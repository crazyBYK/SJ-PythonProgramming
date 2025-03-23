
# week3. 파이썬 제어문과 함수


def ex1():
    cond = True
    if cond:
        print('Excute')
        
        
def ex2():
    var = 10
    if 0 < var:
        print('big')
    else: 
        print('small')

def ex3():
    var = int(input('Enter a number : '))
    if 10 < var:
        print('bigger than 10')
    elif 5 < var:
        print('bigger than 5')
    elif 0 < var:
        print('bigger than 0')
    else:
        print('too small')

def ex4():
    x, y = 10, 20
    if 0 < x and y < 30:
        print("good")
    else:
        print('bad')
        
def ex5():
    var = [1,2,3]
    print(1 in var)
    
    var = ['chris', 'tommy', 'harry']
    print('tommy' in var)
    

def ex6():
    var = int(input("Enter a number: "))
    var = 'big' if 10 < var else 'small'
    print(var)
    
    
def ex7():
    cond = 0
    while cond < 10:
        cond += 1
        if cond % 3 == 0:
            continue
        if cond % 5 == 0:
            break
        print(cond)

def ex8():
    var = [(1,2,), (2,2), (3,3)]
    for (first, second) in var:
        print(first, second)
        
        
def add(x, y):
    print(x)
    print(y)
    return x + y


def sum(*values):
    result = 0
    for value in values:
        result += value
    return result


def calc(a, b):
    return a + b, a-b


val = 0

def processing(data):
    global val
    val = data
    data = data * 10
    return data * data


def processing(refData):
    refData[0] = 100
    


if __name__ == '__main__':
    value_x, value_y = 1, 2
    print('week3')
    print(add(y= value_y, x=value_x))
    x, y = calc(1,3)
    var = [1, 2, 3]
    processing(var)
    print(var)
    

    
    