#Hello from Ihor!!!
fio = 'Metlitskiy Victor Borisovich'
length_fio = len(fio)
print(f'Длина ФИО: {length_fio} символов.')
lst_fio = fio.split()
name, fam, otch = lst_fio[1], lst_fio[0], lst_fio[2]
print(name, fam, otch)
count_o = fio.count('o')
print(f'Количество букв "o" в ФИО равно {count_o}.')
count_e = fio.count('e')
print(f'Количество букв "e" в ФИО равно {count_e}.')
fio_s = f'{fam}\n{name}\t{otch}'
print(fio_s)

