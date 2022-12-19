import log as lg
import interface as ie

def function_update(upd_item, name_data_list = 'data.csv'):
    new_name = ie.get_new_name()
    new_surname = ie.get_new_surname()
    new_number = ie.get_new_tel_num()
    new_comment = ie.get_new_comment()
    new_line = f'{new_surname}|{new_name}|{new_number}|{new_comment}' # меняем в строке старые данные на новые
    with open(name_data_list, 'r',encoding='UTF8') as file:
        init_list = [] 
        for i in file:
            init_list.append(i.rstrip('\n'))
        new_contact_list = []
        for i in range(0, len(init_list)):
            if(init_list[i] != upd_item):
                new_contact_list.append(init_list[i])
            else:
                new_contact_list.append(new_line)
    with open(name_data_list, "w", encoding='UTF-8') as data_file:
            for i in range(len(new_contact_list)):
                data_file.write(f'{new_contact_list[i]}\n')
    lg.create_log(new_line,name_log_file = "log.txt", log_massage = 'Update contact')
    ie.update_success()