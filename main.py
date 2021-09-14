import DBFtoDF
import API_REQUEST

if __name__ == '__main__':
    xml_tree = API_REQUEST.api_request()  # XML 반환 데이터를 tree에 담기
    dbf_table = DBFtoDF.DBF_2_DF('MOCT_LINK.dbf')  # DBF 파일을 테이블 형식으로 변환

    for child in xml_tree.iter('LINK_ID'):
        print(child.text)
    for child in xml_tree.iter('OCPY_RATE'):
        print(child.text)
