import sqlite3


def connect_to_db(path):
    con = sqlite3.connect(path)
    return con


def create_table(con):
    query = (
        "CREATE TABLE IF NOT EXISTS History(id INTEGER PRIMARY KEY, txt TEXT "
        "NOT NULL, shift INTEGER, direction TEXT, shifted_txt TEXT NOT NULL, "
        "time_of_crypting DATETIME);"
    )
    con.execute(query)
    con.commit()


def add_to_history(
    db_name: str, txt: str, shift: str, direction: str, shifted_txt: str
):
    con = connect_to_db(db_name)
    # jak zrobić, żeby dbs były we właściwym folderze?
    # f'dbs//{db_name}' nie działa
    create_table(con)
    query = (
        f"INSERT INTO History(txt, shift, direction, shifted_txt, time_of_crypting) "
        f"VALUES({txt}, {shift}, {direction}, {shifted_txt}, CURRENT_TIMESTAMP)"
    )
    con.execute(query)
    con.commit()
