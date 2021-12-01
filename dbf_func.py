from dbfread import DBF
import pickle

#도로정보DBF 파일에서 xml_list에 있는 범위 내의 도로만 추출합니다
def dbf2dump(file_path, dump_path, xmlmin, xmlmax):
    linkdic = dict()
    readdbf = DBF(file_path, encoding='cp949')

    for record in readdbf:
        if int(record['LINK_ID']) > xmlmin and int(record['LINK_ID']) < xmlmax:
            nodedic = dict()
            nodedic['ROAD_NAME'] = record['ROAD_NAME']
            nodedic['MAX_SPD'] = int(record['MAX_SPD'])
            nodedic['LENGTH'] = float(record['LENGTH'])

            linkdic[int(record['LINK_ID'])] = nodedic

    with open(dump_path, 'wb') as dump_file:
        pickle.dump(linkdic, dump_file)
    dump_file.close()
    return 1


def opendbfdump(file_path):
    with open(file_path, 'rb') as temp_file:
        temp_list = pickle.load(temp_file)
    temp_file.close()
    return temp_list


