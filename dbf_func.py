from dbfread import DBF
import pickle

#도로정보DBF 파일에서 xml_list에 있는 범위 내의 도로만 추출합니다
def dbf2dump(file_path, dump_path, xmlmin, xmlmax):
    temp_list = list()
    readdbf = DBF(file_path, encoding='windows-1252')

    for record in readdbf:
        if int(record['LINK_ID']) > xmlmin and int(record['LINK_ID']) < xmlmax:
            temp_list.append(record)

    with open(dump_path, 'wb') as dump_file:
        pickle.dump(temp_list, dump_file)
    dump_file.close()
    return 1


def opendbfdump(file_path):
    with open(file_path, 'rb') as temp_file:
        temp_list = pickle.load(temp_file)
    temp_file.close()
    return temp_list


