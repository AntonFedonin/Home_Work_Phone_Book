import logger as lg


def new_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    contact = [name, surname, phone, discription]
    lg.write_contact(contact)
    return contact
