from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_ctring = "postgresql://postgres:123@localhost:5432/maksimT"


def test_insert():
    db = create_engine(db_connection_ctring)
    sql = text("insert into teacher(\"email\") values (:new_email)")

    db.execute(sql, new_email = "maksim123@ferry.com")

def test_update():
    db = create_engine(db_connection_ctring)
    sql = text("update teacher set teacher_id = :id where email = :email")

    db.execute(sql, id = "22222", email = "maksim123@ferry.com")

def test_delete():
    db = create_engine(db_connection_ctring)
    sql = text("delete from teacher where email = :email")

    db.execute(sql, email = "maksim123@ferry.com")