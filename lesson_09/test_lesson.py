from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pytest

@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine("postgresql://postgres:123@localhost:5432/maksimT")
    yield engine
    engine.dispose() 

def test_insert(db_engine):
    with db_engine.connect() as conn:
        with conn.begin():
            sql = text("insert into teacher(\"email\") values (:new_email)")
            conn.execute(sql, new_email="maksim123@ferry.com")

        result = conn.execute(
            text("select email from teacher where email = :email"),
            email="maksim123@ferry.com"
        ).fetchone()
        assert result is not None
        assert result[0] == "maksim123@ferry.com"

def test_update(db_engine):
    with db_engine.connect() as conn:
        with conn.begin():
            sql = text("update teacher set teacher_id = :id where email = :email")
            conn.execute(sql, id="123123", email="maksim123@ferry.com")

        result = conn.execute(
            text("SELECT teacher_id FROM teacher WHERE email = :email"),
            email="maksim123@ferry.com"
        ).fetchone()

        assert result is not None
        assert result == '123123'

def test_delete(db_engine):
    with db_engine.connect() as conn:
        with conn.begin():
            sql = text("DELETE FROM teacher WHERE email = :email")
            conn.execute(sql, email="maksim123@ferry.com")

        result = conn.execute(
            text("select email from teacher where email = :email"),
            email="maksim123@ferry.com"
        ).fetchone()

        assert result is None