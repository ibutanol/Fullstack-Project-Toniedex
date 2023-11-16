from db_tables import Tonies,Session
from fastapi import FastAPI
from db_tables import Tonies,Titles

app = FastAPI()


@app.get("/tonies")
def all_tonies():
    with Session() as session:
        all_data = session.query(Tonies).all()
        all_data = [i.__dict__ for i in all_data]
        return all_data
    
@app.get("/tonie/{x}")    
def one_tonie(x:int):
    with Session() as session:
        new_tonie =  session.query(Tonies).filter(Tonies.tonie_id == x).first()
        new_tonie = new_tonie.__dict__
        titlelist = session.query(Titles).filter(Titles.tonie_id == x).all()
        titlelist = [i for i in titlelist]
        return new_tonie,titlelist

# run code python -m uvicorn main:app --reload --port=8888
