import dbf

def DBF_2_DF(file_path):
    dbf.input_decoding = "utf-8"
    table = dbf.Table(file_path)
    return table