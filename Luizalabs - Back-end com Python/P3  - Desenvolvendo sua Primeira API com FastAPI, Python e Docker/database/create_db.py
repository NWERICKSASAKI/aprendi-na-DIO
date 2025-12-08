from sqlalchemy import create_engine
from sqlalchemy import MetaData
from models.atletas import get_atletas_table

def create_db():
    engine = create_engine('sqlite:///database/workout.db', echo=True)
    metadata = MetaData()
    get_atletas_table(metadata)
    metadata.create_all(engine)