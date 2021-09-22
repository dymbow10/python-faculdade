n=int(input("Digite seu numero "))
i=2
primos = 0

while primos < n:
    primo=True

    for j in range(2,i):
        if i % j==0:
            primo=False
            break
    if primo:
        primos+=1
        print (i),
    i+=1
