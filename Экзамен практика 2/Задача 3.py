# 3.	Напишите программу, демонстрирующую работу try\except\finally.
Ed = {'a': 3, 'abc': 4,  'b':5}
try:
    value = Ed ['c']
except KeyError:
    print('Произошла ошибка KeyError!')
finally:
    print('finally выполнен':)
