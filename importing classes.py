from classes import calc

a = int(input("Insira um numero: "))
b = int(input("Insira outro numero: "))
obj = calc(a,b)

print(obj.sum())
print(obj.subtract())
print(obj.mult())
print(obj.divide())
print(obj.power())
