# databases/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self, url: str):
        self.engine = create_engine(url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()