import re


def get_only_date(txt: str):
    txt_date_only = re.sub(r':\s\d\d\.\d', '', txt)
    return txt_date_only


print(get_only_date("2019-03-11: 23.5, 19/03/12: 12.7, "
                    "2019.03.13: 11.1, 2019-marzec-14: 14.3"))
