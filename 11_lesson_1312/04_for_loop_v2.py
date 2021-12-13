deposit = 1000  # сумма вклада
rate = 5 / 100  # процентная ставка
years = 10   # срок вклада

for i in range(1, years + 1):
    yrl = round(deposit * rate, 2)  # округлить до определенного количества символов после запятой
    print(f'Сумма процентов составила: {yrl}')
    deposit += yrl
    print(f'Итого на счету: {deposit}')

