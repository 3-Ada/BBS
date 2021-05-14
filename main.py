import sympy
import time
start_time = time.time()
min_prime = 2
max_prime = 135151289579102590122951015151095793509390523095092371133523523523982375231245350223985238953582395238959115

p = sympy.randprime(min_prime, max_prime)              # межі генерування min and max prime number
q = sympy.randprime(min_prime, max_prime)

                # перевірка умов ББС
while p % 4 != 3:
    p = sympy.randprime(min_prime, max_prime)
while q % 4 != 3:
    q = sympy.randprime(min_prime, max_prime)

print("p = ", p, "\n q = ", q)
n = p*q
print("n = ", n)
x = sympy.randprime(min_prime, max_prime)
print("x = ", x)
x_bit = []
s = []
x_bit.insert(0, pow(x,2) % n)
s.insert(0, x_bit[0] % 2)
for i in range(1, 8):
    x_bit.insert(i, pow(x_bit[i-1], 2) % n)
    s.insert(i, x_bit[i] % 2)

for i in range(len(s)):
    print(i, x_bit[i], s[i])

print('-----------------')
print('The length of the min_prime is: \n')
print(len(str(min_prime)))
print('-----------------')
print('The length of the max_prime is: \n')
print(len(str(max_prime)))
print('The execution time is :')
print("--- %s seconds ---" % (time.time() - start_time))
