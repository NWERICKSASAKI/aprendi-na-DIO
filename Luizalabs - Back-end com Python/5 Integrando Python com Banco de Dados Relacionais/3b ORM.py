from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False) # não permite valor nulo
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Visualizando nomes das tabelas
inspetor_engine = inspect(engine)
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    juliana = User(
        name='juliana',
        fullname='Juliana Mascarenhas',
        address=[Address(email_address='julianam@email.com')]
    )
    
    sandy = User(
        name='sandy',
        fullname='Sandy Cardoso',
        address=[Address(email_address='sandyc@email.br'),
                 Address(email_address='sandyc@email.org')]
    )

    patrick = User(
        name='patrick',
        fullname='Patrick Cardoso'
    )

    # Enviando para o banco de dados (persistência de dados)
    session.add_all([juliana, sandy, patrick])
    session.commit()

stmt = select(User).where(User.name.in_(['juliana','sandy']))
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
    print(address)

# SELECT FROM User BY
stmt_order = select(User).order_by(User.fullname.desc())
print(stmt_order)
for result in session.scalars(stmt_order):
    print(result)

# JOIN

# -- via SCALAR não dá certo porque só pega o primeiro resultado 
# stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
# print(stmt_join)
# for result in session.scalars(stmt_join):
#    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print('\n',stmt_join)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("Executando statemente a partir da connection")
for result in results:
    print(result)

# COUNT
print('Total de instâncias em User')
stmt_count = select(func.count('*')).select_from(User)
print(stmt_count)
for result in session.scalars(stmt_count):
    print(result)

