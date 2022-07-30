import data_base as db


def new_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    contact = [name, surname, phone, discription]
    db.write_contact(contact)
    return contact
