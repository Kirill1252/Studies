def index(m, h):
    if h <= 0 or m <= 0:
        raise ValueError('Вы ввели отрицательное значение или значение которое равняется нулю')
    h = h / 100
    index_mass = m / h ** 2
    index_mass = round(index_mass, 2)
    mess = f'Индекс тела равен: {index_mass} кг/м² и у Вас'
    if index_mass < 16:
        print(f'{mess} выраженный дефицит массы тела')
        return index_mass

    elif index_mass >= 16 and index_mass <= 18.5:
        print(f'{mess} Недостаточный (дефицит) массы тела')
        return index_mass

    elif index_mass >= 18.5 and index_mass <= 24.99:
        print(f'{mess} норма')
        return index_mass

    elif index_mass >= 25 and index_mass <= 30:
        print(f'{mess} избыточная масса тела (предожирение)')
        return index_mass

    elif index_mass >= 30 and index_mass <= 35:
        print(f'{mess} ожирение')
        return index_mass

    elif index_mass >= 35 and index_mass <= 40:
        print(f'{mess} резкое ожирение')
        return index_mass

    elif index_mass >= 40:
        print(f'{mess} очень резкое ожирение!')
        return index_mass
