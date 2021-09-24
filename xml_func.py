import pickle
import API_REQUEST


# xml 트리를 이용해 유효한 LINK_ID 값만 추려서 xml_tree_nodlink.txt 파일에 저장
def xmllistdump(file_path):
    xml_tree = API_REQUEST.api_request()  # API 리퀘스트 후, XML 반환 데이터를 xml_tree 에 담기
    temp_list = list()
    for child in xml_tree.iter('LINK_ID'):
        temp_list.append(child)
    with open(file_path, 'wb') as file:
        pickle.dump(temp_list, file)
    file.close()
    return 1


# xml list 덤프파일 읽어와서 리스트 생성후 리턴해주는 함수
def xmldumpopen(file_path):
    with open(file_path, 'rb') as file:
        temp_list = pickle.load(file)
    file.close()
    return temp_list
