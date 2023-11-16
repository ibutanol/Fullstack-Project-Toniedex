import db_tables as db_tables
from sqlalchemy.orm import sessionmaker
from crawler_2 import crawl 



Session = sessionmaker(bind=db_tables.engine)

crwl = crawl()


with Session() as session:

    for i in crwl:
        go = db_tables.Tonies(i)
        session.add(go)

    session.commit()