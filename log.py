from datetime import datetime

def create_log(data_contact: list,name_log_file: str="log.txt", log_massage:str = 'Delete contact'):
    """ Функция создания лога, принимает список данных о контакте ['имя','фамилия','номер телефона','комментарий'] , название файла логов (по умолчанию log.txt)
     и сообщение о действие с записью. Записывает дату, действие и контакт, над которым произведено дейсвтие в файл логов
    Arguments:
             (list)data_contact - список ['имя','фамилия','номер телефона','комментарий']
             (str)name_log_file - название файла с логами
             (str)log_massage - сообщение о действиии, по умолчанию 'Delete contact'
       
    """
    current_datetime = str(datetime.now())   
    log_item = current_datetime+' '+str(data_contact)+' '+log_massage+'\n'
    #print(log_item)
    with open(name_log_file, "a", encoding='UTF-8') as data_file:        
        data_file.write(log_item)
    data_file.close()    

data_contact = ['имя','фамилия','номер телефона','комментарий']
create_log(data_contact)