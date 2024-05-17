import datetime
from dataclasses import dataclass
from datetime import datetime as datetime_format
from uuid import UUID

from pydantic import BaseModel, ConfigDict, field_validator


def getTablesClass():
    return dict(
        film_work=Film,
        person=Person,
        genre=Genre,
        genre_film_work=GenreFilm,
        person_film_work=PersonFilm,
    )


@dataclass
class Model:
    id: UUID


@dataclass
class Film(BaseModel, Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    title: str
    description: str | None
    creation_date: datetime.date | None
    rating: float | None
    type: str
    file_path: str | None
    created: datetime
    modified: datetime

    def __init__(
        self,
        id: UUID,
        title: str,
        description: str,
        rating: float,
        type: str,
        file_path: str,
        created: datetime,
        modified: datetime,
        creation_date: datetime.date,
    ):
        super().__init__(
            id=id,
            title=title,
            description=description,
            creation_date=creation_date,
            rating=rating,
            type=type,
            file_path=file_path,
            created=created,
            modified=modified,
        )

    @field_validator('created', mode='before')
    @classmethod
    def to_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v

    @field_validator('modified', mode='before')
    @classmethod
    def modified_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v


@dataclass
class Genre(BaseModel, Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    description: str | None
    created: datetime
    modified: datetime

    def __init__(
        self,
        id: UUID,
        name: str,
        description: str,
        created: datetime,
        modified: datetime,
    ):
        super().__init__(
            id=id,
            name=name,
            description=description,
            created=created,
            modified=modified,
        )

    @field_validator('created', mode='before')
    @classmethod
    def to_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v

    @field_validator('modified', mode='before')
    @classmethod
    def modified_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v


@dataclass
class Person(BaseModel, Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    full_name: str
    created: datetime
    modified: datetime

    def __init__(
        self, id: UUID, full_name: str, created: datetime, modified: datetime
    ):
        super().__init__(
            id=id, full_name=full_name, created=created, modified=modified
        )

    @field_validator('created', mode='before')
    @classmethod
    def to_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v

    @field_validator('modified', mode='before')
    @classmethod
    def modified_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v


@dataclass
class GenreFilm(BaseModel, Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    genre_id: UUID
    film_work_id: UUID
    created: datetime

    def __init__(
        self, id: UUID, genre_id: UUID, film_work_id: UUID, created: datetime
    ):
        super().__init__(
            id=id,
            genre_id=genre_id,
            film_work_id=film_work_id,
            created=created,
        )

    @field_validator('created', mode='before')
    @classmethod
    def to_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v


@dataclass
class PersonFilm(BaseModel, Model):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    film_work_id: UUID
    person_id: UUID
    role: str
    created: datetime

    def __init__(
        self,
        id: UUID,
        film_work_id: UUID,
        person_id: UUID,
        role: str,
        created: datetime,
    ):
        super().__init__(
            id=id,
            film_work_id=film_work_id,
            person_id=person_id,
            role=role,
            created=created,
        )

    @field_validator('created', mode='before')
    @classmethod
    def to_timezone(cls, v):
        if isinstance(v, str):
            fd = datetime_format.strptime(v + '00', '%Y-%m-%d %H:%M:%S.%f%z')
            return fd
        return v
