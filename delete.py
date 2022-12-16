from log import create_log

def get_list_of_contacts(name_data_list : str ="data.csv") -> list:
    """ не моя функция - считывает с файла и возвращает список контактов
    """
    data_list=[]
    with open(name_data_list, "r", encoding='UTF-8') as data_file:
        for line in data_file.readlines():
            data_list.append(line)
    data_file.close()
    return data_list



data_list =['имя|фамилия|номер телефона|комментарий',
'1имя|фамилия1|номер телефона|комментарий',
'2имя|фамилия2|номер телефона|комментарий',
'3имя|фамилия3|номер телефона|комментарий',
'4имя|фамилия4|номер телефона|комментарий',
'5имя|фамилия5|номер телефона|комментарий',
'6имя|фамилия6|номер телефона|комментарий',
'7имя|фамилия7|номер телефона|комментарий',
'8имя|фамилия8|номер телефона|комментарий']


def delete_contact(data_list: list,name_data_list: str="data.csv", id_delete_contact: int = 5):
    """ принимает список контактов , название файла с данными и номер строки с контактом для удаления (отсчет с 0 )
    Arguments:
             (list)data_list список контактов где 1 элемент это 'имя|фамилия|номер телефона|комментарий'
             (str)name_data_list- название файла с контактами 
             (int) id_delete_contact - номер записи в файле для удаления (нумерация с 0 строки)
       
    """
    new_data_list = data_list[:id_delete_contact]+data_list[id_delete_contact+1:]
    delete_contact_item = []
    delete_contact_item.append(data_list[id_delete_contact].split('|'))
    #print(f' delete {delete_contact_item}')
    create_log(delete_contact_item)
    with open(name_data_list, "w", encoding='UTF-8') as data_file:
        for i in range(len(new_data_list)):
            data_file.write(f'{new_data_list[i]}\n')
    data_file.close()

def print_contact(data_list: list,name_data_list: str="data.csv"):
    """ функция для проверки , удалить после сборки     
    """
    
    with open(name_data_list, "w", encoding='UTF-8') as data_file:
        for i in range(len(data_list)):
            data_file.write(data_list[i])
    data_file.close()    


print_contact(data_list )
print(get_list_of_contacts())
print('\n\n')
delete_contact(data_list,)
print(get_list_of_contacts())