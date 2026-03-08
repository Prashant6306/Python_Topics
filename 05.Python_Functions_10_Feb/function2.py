# x=10
# y=20
# z=30
# sum=x+y+z
# print(sum)


def sum_and_mul_of_three_numbers(a,b,c):
    sum=a+b+c
    mul=a*b*c
    return sum,mul

x=10
y=20
z=30
result1,result2=sum_and_mul_of_three_numbers(x,y,z)
print("returned value of summation from function is:",result1)
print("returned value of multiplication from function is:",result2)