# a, b= float(input("Digite um valor para a: ")), float(input("Digite um valor para b: "))
a = 1
b = 2

temp = a
b = 1

print(f'temp: {temp}, a: {a}, b: {b}')


a, b = b, a

print(f'temp: {temp}, a: {a}, b: {b}')

L = [1,2,3,4,5,6,7,8]
print(L[::-1])

