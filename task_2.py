profit_1q = int(input('Введите доход за первый квартал: '))
profit_2q = int(input('Введите доход за второй квартал: '))
profit_3q = int(input('Введите доход за третий квартал: '))
profit_4q = int(input('Введите доход за четвертый квартал: '))
sum_half_1 = profit_1q + profit_2q
sum_half_2 = profit_3q + profit_4q
dinamic = sum_half_1 / sum_half_2
print('Динамика изменения дохода:', dinamic)