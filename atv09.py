hora1= int(input("Hora 1:"))
min1= int(input("min1:"))
hora2= int(input("hora2:"))
min2= int(input("min2:"))

total_min= (min1+min2)
total_hora= hora1=hora2
if total_min>=60:
        total_hora+=1
        total_min-=60
if total_hora>=24:
    total_hora-=24
else:
    total_hora-=12
    print(total_hora, total_min)