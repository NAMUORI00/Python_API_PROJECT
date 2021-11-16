from dbfread import DBF
import pickle


#도로정보DBF 파일에서 xml_list에 있는 범위 내의 도로만 추출합니다
def dbf2dump(file_path, dump_path, xmlmin, xmlmax):
    temp_list = list()
    readdbf = DBF(file_path, encoding='cp949')

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


def listOFdic_search(name, lista):
    for p in lista:
        if p['LINK_ID'] == name:
            return p


# xmlist, dbflist
def filter_dbfdata_list(xmllist, dbflist):
    temp_list = list()
    for i in range(0, len(xmllist)):
        a = listOFdic_search(xmllist[i]['LINKID'], dbflist)
        if a is not None:
            temp_list.append(a)
    return temp_list


