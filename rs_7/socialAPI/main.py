from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI()

objave = []
next_id = 1


class ObjavaCreate(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)


class ObjavaResponse(BaseModel):
    id: int
    korisnik: str
    tekst: str
    vrijeme: datetime


@app.post("/objava", response_model=ObjavaResponse, status_code=201)
async def create_objava(objava: ObjavaCreate):
    global next_id
    nova_objava = {
        "id": next_id,
        "korisnik": objava.korisnik,
        "tekst": objava.tekst,
        "vrijeme": datetime.now()
    }
    objave.append(nova_objava)
    next_id += 1
    return nova_objava


@app.get("/objava/{id}", response_model=ObjavaResponse)
async def get_objava(id: int):
    for objava in objave:
        if objava["id"] == id:
            return objava
    raise HTTPException(status_code=404, detail="Objava nije pronađena")


@app.get("/korisnici/{korisnik}/objave", response_model=list[ObjavaResponse])
async def get_objave_korisnika(korisnik: str):
    korisnikove_objave = [o for o in objave if o["korisnik"] == korisnik]
    return korisnikove_objave


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3500)
