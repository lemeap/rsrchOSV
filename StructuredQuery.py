import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy as sa
import psycopg2 as pg2
import io

class StructuredQuery:
    def __init__(self):
        print("Construct connection string and update")
        print("SQL_OSV is successfully started.")

    def connect(self, host, dbname, user, port, password):
        """
        Database 연결
        """
        db_engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(user,password,host,port,dbname))
        conn = pg2.connect(database = dbname, host = host, user = user, password = password)
        return (conn, db_engine)

    def read_sql(self, query, db_engine):
        """
        PostgreSQL에서 테이블 읽어오기
        """
        copy_sql = "COPY ({query}) TO STDOUT WITH CSV {head}".format(
            query=query, head="HEADER"
        )
        conn = db_engine.raw_connection()
        cur = conn.cursor()
        store = io.StringIO()
        cur.copy_expert(copy_sql, store)
        store.seek(0)
        df = pd.read_csv(store)
        return df

    def write_sql(self, df, table_name, db_engine):
        """
        파이썬에서 생성된 데이터프레임을 PostgreSQL로 쓰기
        """
        df.head(0).to_sql(table_name, db_engine, if_exists='replace', index=True)  # truncates the table
        conn = db_engine.raw_connection()
        cur = conn.cursor()
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=True)
        output.seek(0)
        contents = output.getvalue()
        cur.copy_from(output, table_name, null="")  # null values become ''
        conn.commit()
        return print("Write_sql is succeeded in recording {} table. ".format(table_name))








