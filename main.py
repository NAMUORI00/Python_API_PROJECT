import dbf_func
import list_func
import xml_func
import API_REQUEST

if __name__ == '__main__':
#   xml_tree = API_REQUEST.api_request()  # API 리퀘스트 후, XML 반환 데이터를 xml_tree 에 담기 #HK : 해당 코드는 이 문서에서 사용되지 않음
    xml_func.xmllistdump('dump_file/xml_tree_nodlink.txt') # xml 트리에서 유효한 LINK_ID 만 리스트로 모아서 덤프파일 생성
    xml_list = xml_func.xmldumpopen('dump_file/xml_tree_nodlink.txt')
    xmlmetadata = xml_func.minmaxlinkid(xml_list) #XML의 최소/최대값을 가진 2칸짜리 리스트
    dbf_func.dbf2dump('dump_file/MOCT_LINK.dbf', 'dump_file/dump.txt', xmlmetadata[0], xmlmetadata[1])  # DBF 파일을 딕셔너리 리스트로 만든후 덤프파일 생성
    dbf_list = dbf_func.opendbfdump('dump_file/dump.txt')    # dump.txt 파일 list 로 반환  # XML에 있는 LINKID 만을 추출해서 덤프파일의 크기가 줄었습니다
    list_func.make_data_list(xml_list, dbf_list) # 이 함수를 실행하기 전에 두 리스트를 오름차순 정렬하는 것이 효율적일듯 합니다. 방법을 생각해 두겠습니다
