import dbf_func
import list_func
import xml_func


def makexmllist():
    # API 지원중단이 되어서 기존에 다운로드한 dump 파일을 기준으로 프로젝트를 진행합니다.
    # xml response 데이터 호출.
    xml_func.xmllistdump('dump_file/xml_tree_nodlink.txt')  # xml 트리에서 유효한 LINK_ID 만 리스트로 모아서 덤프파일 생성
    xml_list = xml_func.xmldumpopen('dump_file/xml_tree_nodlink.txt')
    return xml_list


def makeDBFlist(xml_list):
    # XML의 최소/최대값을 가진 2칸짜리 리스트
    xmlmetadata = xml_func.minmaxlinkid(xml_list)
    # DBF 파일을 딕셔너리 리스트로 만든후 덤프파일 생성
    # XML에 있는 LINKID 범위만을 추출해서 덤프파일의 크기감소
    dbf_func.dbf2dump('dump_file/MOCT_LINK.dbf', 'dump_file/dbf_dump.txt', xmlmetadata[0], xmlmetadata[1])
    dbf_list = dbf_func.opendbfdump('dump_file/dbf_dump.txt')   # dump.txt 파일 list 로 반환
    p = dbf_func.filter_dbfdata_list(xml_list, dbf_list)    # dbf_dump 파일 xml 리스트에 맞추어서 최종 필터링
    return p


if __name__ == '__main__':
    xml_list = makexmllist()   # xml 딕셔너리 리스트 변수
    print(xml_list)
    print('==================================================')
    dbf_list = makeDBFlist(xml_list)   # dbf 딕셔너리 리스트 변수
    print(dbf_list)

