from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func, MetaData, Table, text


engine = create_engine('sqlite:///:memory:')

metadata_obj = MetaData()

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False),
)

user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
)

for table in metadata_obj.sorted_tables: # recuperar as tabelas ordenadas
    print(table)




metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info',
    metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False),
)

print( financial_info.primary_key )


metadata_obj.create_all(engine)

with engine.connect() as conn:

    # criar entradas
    sql_insert = text("insert into user values(2, 'Maria', 'maria@email.com', 'Ma')")
    conn.execute(sql_insert)

    # visualizar dados
    sql = text('select * from user')
    result = conn.execute(sql)

    for row in result:
        print(row)

    # conn.commit()
