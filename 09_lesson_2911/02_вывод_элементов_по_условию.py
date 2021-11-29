fridge = {
    'milk': 2.62,
    'cheese': 9.99,
    'cucumber': 4.52,
    'melon': 12.94
}

# я хочу вывести те продукты, стоимость которых больше 7
for key, value in fridge.items():
    if value > 7:
        print(f'{key} costs ${value}.')
