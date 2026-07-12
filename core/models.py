from sqlmodel import SQLModel, Field


class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    source: str
    external_id: str

    title: str
    description: str
    registration_period: str
    link: str