

def calculate_sum(*args):
    print(*args)   #*args=(10,20,30)
    return sum(*args)


result=calculate_sum((10,20,30))
print("your result is:",result)


