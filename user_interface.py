import controller as cont


def greetings():
    print('Привет! Это твоя телефонная книга!\nЗапишем новый контакт или найдём уже существующий?')
    print('Введите "1", чтобы добавить новый контакт\n\nВведите "2", чтобы найти существующий')
    return int(input())

def find_contact():
    print('Введите фрагмент для поиска')
    return input()    


def report(data):
    print(f'Новый контакт {data} успешно сохранён')
