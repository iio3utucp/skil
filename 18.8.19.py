print('How many tickets do you want to buy?', end='\t')
cnt = int(input())
age = 0
sum = 0
sale = False
if cnt > 3:
    sale = True
for i in range(cnt):
    print('How old is the room visitor', i+1, '?', end=' ')
    age = int(input())
    if age < 18:
        pass
    else:
        if (age == 18) or (age < 25):
            sum += 990
        else: sum += 1390
if sale == True:
    print(sum * 0.9)
else: print(sum)