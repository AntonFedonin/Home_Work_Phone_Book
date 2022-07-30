from datetime import datetime as dt


def write_contact(data):
    time = dt.now().strftime('%H:%H')
    contact = " ".join(data)
    with open('log.csv', 'a') as file:
        file.write('{}; Новый контакт создан в ;{}\n'.format(time, contact))
