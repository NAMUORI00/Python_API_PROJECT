import dbf_func
import list_func
import xml_func
import API_REQUEST

if __name__ == '__main__':
    xml_tree = API_REQUEST.api_request()  # API 리퀘스트 후, XML 반환 데이터를 xml_tree 에 담기
    xml_func.xmllistdump('dump_file/xml_tree_nodlink.txt') # xml 트리에서 유효한 LINK_ID 만 리스트로 모아서 덤프파일 생성
#   dbf_func.dbf2dump('MOCT_LINK.dbf')  # DBF 파일을 딕셔너리 리스트로 만든후 덤프파일 생성
    xml_list = xml_func.xmldumpopen('dump_file/xml_tree_nodlink.txt')
    dbf_list = dbf_func.opendbfdump('dump_file/dump.txt')    # dump.txt 파일 list 로 반환
    list_func.make_data_list(xml_list, dbf_list)
