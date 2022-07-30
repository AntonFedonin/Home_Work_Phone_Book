from secrets import choice
import import_contact as ic
import user_interface as ui
import find_contact as fc


def start():
    choice = ui.greetings()
    if choice == 1:
        conatct = ic.new_contact()
        ui.report(conatct)
    elif choice ==2:
        find=ui.find_contact()
        contact= fc.find_contact()
        ui.report(contact)    
