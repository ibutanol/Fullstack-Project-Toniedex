from crawler_2 import crawl
from db_tables import Session,Tonies

with Session() as session:
    for i in crawl():
        existing_tonie = session.query(Tonies).filter(Tonies.title == i.title).one_or_none()
        if existing_tonie:
            i.tonie_id = existing_tonie.tonie_id
            for title in i.titles:
                title.tonie_id, title.title_id = existing_tonie.tonie_id, next((t.title_id for t in existing_tonie.titles if t.titles == title.titles), None)
            session.merge(i)
        else:
            session.add(i)

    session.commit()
