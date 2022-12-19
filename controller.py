import check as ch
import create as cr
import delete as de
import find as fd
import read as rd
import update as up
import interface as ie

def start():
    ie.hello()
    while True:
        ie.main_menu()
        n = ie.menu_item()
        if n == 1:
            cr.record_in_book()
        elif n == 2:
            result = fd.search_contact_by_surname()
            ie.top_line()
            print(result)
        elif n == 5:
            ie.result_read()
            rd.Read_csvfile('data.csv')
        elif n == 6:
            update = True
            while update == True:
                ie.menu_item_options()
                option = ie.menu_item()
                if option == 1:
                    surname = str(fd.search_contact_by_surname()).lstrip("['") # возвращаем строку с искомой фамилией
                    surname = surname.rstrip("']")
                    ie.result_search()
                    ie.top_line()
                    print(surname)
                    up.function_update(surname, name_data_list = 'data.csv')
                elif option == 2:
                    name = str(fd.search_contact_by_name()).lstrip("['")
                    name = name.rstrip("']")
                    ie.result_search()
                    ie.top_line()
                    print(name)
                    up.function_update(name, name_data_list = 'data.csv')
                elif option == 3:
                    tel_num = str(fd.search_contact_by_phone_num()).lstrip("['")
                    tel_num = tel_num.rstrip("']")
                    ie.result_search()
                    ie.top_line()
                    print(tel_num)
                    up.function_update(tel_num, name_data_list = 'data.csv')
                elif option == 4: 
                    update = False
                else:
                    ie.error_menu_item()
        elif n == 7:
            delete = True
            while delete == True:
                ie.menu_item_options()
                option = ie.menu_item()
                if option == 1:
                    surname = ie.get_surname()
                    de.delete_contact(surname,name_data_list="data.csv")
                elif option == 2:
                    name = ie.get_name()
                    de.delete_contact(name,name_data_list="data.csv")
                elif option == 3:
                    tel_num = ie.get_tel_num()
                    de.delete_contact(tel_num,name_data_list="data.csv")
                elif option == 4: 
                    delete= False
                else:
                    ie.error_menu_item()
        elif n == 8:
            ie.bye()
            break
        else:
            ie.error_menu_item()