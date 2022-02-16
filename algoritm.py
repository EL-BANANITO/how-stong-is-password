password = 'some password'

symbols = ['!', '@', '#', '$','%','^','&','*','(',')','-','_','=','+', '1', '2','3','4','5','6','7','8','9','0']

if password == 'qwerty' or password =='password' or password =='1234':
    point = -10
else:
    point = 0

x = len(password)
y = 0
if password.isdecimal() == True:
    while y < x or y == x:
        y += 1
        z1 = password[x - y]
        z2 = password[x - (y + 1)]
        if int(z2) + 1 == int(z1):
            print(z1, z2)
            point -= 1
        else:
            point = point

if len(password) > 7:
    point+=10
else:
    point-=5

while y < len(symbols):
    if symbols[y] in password:
        point+=1
    y+=1

print(f'your password is{point}')
