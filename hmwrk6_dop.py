import random

def quest():
    num = list(range(3, 21))
    numbers = list(range(3, 21))
    lok = random.choice(numbers)
    return lok
def pass_(z):
    passdict = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746,
                11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968,
                15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089,
                18: 12151811724272163631545414513612711810,19: 118217316415514613712811910,
                20: 13141911923282183731746416515614713812911}
    code = passdict.get(z)
    return code

z = quest()
print('Шифр: ', z)
pair1 = list(range(1, z))
pair2 = list(range(1, z))
pairs = []
result = ''

for i in pair1:
    for j in pair2:
        if i >= j:
            continue
        else:
            if z % (i + j) == 0:
                pairs.append([i, j])
                result = result + str(i) + str(j)
print('Пары чисел', *pairs)
print('Введите пароль', result)
if int(result) == pass_(z):
    print('Пароль подошел')
