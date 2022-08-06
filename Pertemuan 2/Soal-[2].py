import math

x = math.pi

value = int(input('Masukkan nilai jari - jari lingkaran : '))

result = x*value**2
result = '{:.2f}'.format(result)

print(f"Luas lingkaran dengan jari-jari {value} cm adalah {result} cm\u00b2 .")