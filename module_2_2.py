first = int(input('пожалуйста, введите первое целое число '))
second = int(input('пожалуйста, введите второе целое число '))
third = int(input('пожалуйста, введите третье целое число '))
#print(first, second, third) proverka
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else: print(0)
