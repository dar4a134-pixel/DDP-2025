#soal no 1
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print(celcius_ke_fahrenheit(0))    # Output: 32.0
print(celcius_ke_fahrenheit(100))  # Output: 212.0


#soal no 2
print()
def is_genap(n):
    return n % 2 == 0

print(is_genap(2))


#soal no 3
print()
def nilai(n = 0):
    if n <= 60:
        print(f"nilai {n} tidak lulus")
    elif n > 60 and n <= 100:
        print(f"nilai {n} lulus")
    else:
        print(f"nilai {n} tidak diketahui")

nilai(80)
nilai()
        

#soal no 4
print()
def bilangan(angka):
    for i in range(1,angka+1):
        if i % 2 != 0:
            print(i, end=", ")

bilangan(20)            