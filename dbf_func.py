from dbfread import DBF
import pickle


def dbf2dump(file_path):
    temp_list = list()

    for record in DBF(file_path, encoding='windows-1252'):
        temp_list.append(record)

    with open(file_path, 'wb') as dump_file:
        pickle.dump(temp_list, dump_file)
    dump_file.close()
    return 1


def opendbfdump(file_path):
    with open(file_path, 'rb') as temp_file:
        temp_list = pickle.load(temp_file)
    temp_file.close()
    return temp_list


