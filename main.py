
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('mysql+pymysql://centre_user:Password1!@localhost/community_centre')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
