from log import create_log
from find import search_contact_return_number_line
from read import get_lines_list_of_contacts
from interface import error_delete, delete_success, delete_question

def delete_contact(data_contact,name_data_list: str="data.csv"):
    """ принимает название файла, вызывает функцию поиска по имени или фамилии, удаляет контакт если он найден
    Arguments:
             (str)name_data_list- название файла с контактами    
             (str)data_contact    
    """

    id_delete_contact=search_contact_return_number_line(data_contact)
   
    data_list=get_lines_list_of_contacts(name_data_list)
    
    
    if id_delete_contact>0: #защита от удаления оглавления - 0 строка с оглавлением
        new_data_list = data_list[:id_delete_contact]+data_list[id_delete_contact+1:]
        delete_contact_item = []
        delete_contact_item.append(data_list[id_delete_contact].split('|'))
        srt_delete_contact = ''. join(map(str,data_list[id_delete_contact]))
        srt_delete_contact = srt_delete_contact.replace("|"," ")          
        answer = delete_question(srt_delete_contact)
        if answer=='Y':
            create_log(delete_contact_item)
            with open(name_data_list, "w", encoding='UTF-8') as data_file:
                 for i in range(len(new_data_list)):
                    data_file.write(f'{new_data_list[i]}')
            data_file.close()
            delete_success()
        else: return 0  
    else:
        error_delete()
        return 0