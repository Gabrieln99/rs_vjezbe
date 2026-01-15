import json
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from models.film import Film
from models.person import Actor, Writer


router = APIRouter(
    prefix="/filmovi",
    tags=["Filmovi"]
)


def parse_people(text: str) -> List[dict]:
    people = []

    if not text or text == "N/A":
        return people

    for p in text.split(","):
        parts = p.strip().split(" ")
        people.append({
            "name": parts[0],
            "surname": parts[-1]
        })

    return people


def parse_year(year: str) -> int:
    return int(year.split("–")[0])


def parse_runtime(runtime: str) -> Optional[int]:
    if not runtime or runtime == "N/A":
        return None
    return int(runtime.replace("min", "").strip())


def parse_imdb_votes(votes: str) -> Optional[int]:
    if not votes or votes == "N/A":
        return None
    return int(votes.replace(",", ""))


def parse_imdb_rating(rating: str) -> Optional[float]:
    if not rating or rating == "N/A":
        return None
    return float(rating)


with open("data/filmovi.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

filmovi: List[Film] = []

for film in raw_data:
    film_clean = {
        "imdbID": film["imdbID"],
        "Title": film["Title"],
        "Year": parse_year(film["Year"]),
        "Plot": film["Plot"],
        "Writer": parse_people(film.get("Writer")),
        "Actors": parse_people(film.get("Actors")),
        "Rated": film.get("Rated", "N/A"),
        "Runtime": parse_runtime(film.get("Runtime")),
        "Genre": film["Genre"],
        "Language": film["Language"],
        "Country": film["Country"],
        "imdbRating": parse_imdb_rating(film.get("imdbRating")),
        "imdbVotes": parse_imdb_votes(film.get("imdbVotes")),
        "Images": film.get("Images", []),
        "type": film["Type"].lower(),
        "Awards": film.get("Awards"),
        "Poster": film.get("Poster")
    }

    filmovi.append(Film(**film_clean))


@router.get("/", response_model=List[Film])
def get_filmovi(
    min_year: Optional[int] = Query(None, gt=1900),
    max_year: Optional[int] = None,
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None)
):
    rezultat = filmovi

    if min_year is not None:
        rezultat = [f for f in rezultat if f.Year >= min_year]

    if max_year is not None:
        rezultat = [f for f in rezultat if f.Year <= max_year]

    if min_rating is not None:
        rezultat = [
            f for f in rezultat
            if f.imdbRating is not None and f.imdbRating >= min_rating
        ]

    if max_rating is not None:
        rezultat = [
            f for f in rezultat
            if f.imdbRating is not None and f.imdbRating <= max_rating
        ]

    if type is not None:
        rezultat = [f for f in rezultat if f.type == type]

    return rezultat


@router.get("/{imdbID}", response_model=Film)
def get_film_by_imdb_id(imdbID: str):
    film = next((f for f in filmovi if f.imdbID == imdbID), None)

    if not film:
        raise HTTPException(status_code=404, detail="Film nije pronađen")

    return film


@router.get("/naslov/{title}", response_model=Film)
def get_film_by_title(title: str):
    film = next(
        (f for f in filmovi if f.Title.lower() == title.lower()),
        None
    )

    if not film:
        raise HTTPException(status_code=404, detail="Film nije pronađen")

    return film
