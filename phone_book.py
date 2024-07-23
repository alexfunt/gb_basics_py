from csv import DictWriter, DictReader
from os.path import exists


filename = 'phone.csv'
filename1 = 'newphone.csv'

class  NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_data():
    flag = False
    while not flag:
        try:
            first_name  = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("слишком котроткое имя")
            last_name  = input("Введите фамилию: ")
            if len(first_name) < 2:
                raise NameError("слишком котроткая фамилия")
            phone  = input("Введите номер: ")
            if len(first_name) < 6:
                raise NameError("слишком котроткий номер")
        except NameError as err: 
            print(err)
        else:
            flag = True
    return[first_name, last_name, phone]

def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as Data:
        f_w = DictWriter(Data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as Data:
        f_r = DictReader(Data)
        return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон':lst[2]}
    res.append(obj)
    standart_write(filename, res)

def row_search(filename):
    last_name = input("Введите Фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            # print(row)
            return row
    return("Запись не найдена")

def delete_row(filename):
    row_number = input("Введите номер строки: ")
    res = read_file(filename)
    res.pop(row_number-1)
    standart_write(filename, res)
    
def standart_write(filename,res):
    with open(filename, 'w', encoding='utf-8') as Data:
        f_w = DictWriter(Data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def new_write(filename1,row):
    with open(filename1, 'w', encoding='utf-8') as Data:
        f_w = DictWriter(Data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        if Data.tell() == 0:
            f_w.writeheader()
        f_w.writerow(row)


def change_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    data = get_data()
    res[row_number-1]["Имя"] = data[0]
    res[row_number-1]["Фамилия"] = data[1]
    res[row_number-1]["Телефон"] = data[2]
    standart_write(filename,res)

def copy_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    if row_number > 0 and row_number <= len(res):
        row = res[row_number-1]
    create_file(filename1)
    new_write(filename1,row)




def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(filename):
                create_file(filename)
            write_file(filename,get_data())
        elif command == 'r':
            if not exists(filename):
                print("Файл не сушествует")
                continue
            print(read_file(filename))
        elif command == 'f':
            if not exists(filename):
                print("Файл не сушествует")
                continue
            print(row_search(filename))
        elif command == 'd':
            if not exists(filename):
                print("Файл не сушествует")
                continue
            delete_row(filename)
        elif command == 'c':
            if not exists(filename):
                print("Файл не сушествует")
                continue
            change_row(filename)
        elif command == 'p':
            if not exists(filename):
                print("Файл не сушествует")
                continue
            copy_row(filename)

main()

