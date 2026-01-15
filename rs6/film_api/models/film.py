from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from models.person import Actor, Writer


class Film(BaseModel):
    imdbID: str

    Title: str
    Year: int = Field(..., gt=1900)
    Plot: str

    Writer: List[Writer]
    Actors: List[Actor]

    Rated: str
    Runtime: Optional[int] = Field(None, gt=0)

    Genre: str
    Language: str
    Country: str

    imdbRating: Optional[float] = Field(None, ge=0, le=10)
    imdbVotes: Optional[int] = Field(None, gt=0)
    


    Images: List[str]
    type: Literal["movie", "series"]

    Awards: Optional[str] = None
    Poster: Optional[str] = None
