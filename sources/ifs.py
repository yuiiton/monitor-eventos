import requests
from bs4 import BeautifulSoup
from core.models import Event
from core.configs import HEADERS

BASE_URL = "https://suap.ifs.edu.br"
EVENTS_URL = f"{BASE_URL}/eventos/inscricao/"


def get_event_id(link: str) -> str:
    """Extrai o ID do evento a partir da URL."""
    return link.rstrip("/").split("/")[-1]


def get_events() -> list[Event]:
    """Obtém todos os eventos do portal do IFS."""

    response = requests.get(
    EVENTS_URL,
    headers=HEADERS,
    timeout=10,
)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    event_boxes = soup.find_all("div", class_="general-box")

    events = []

    for event in event_boxes:
        relative_link = event.find("a")["href"]
        link = BASE_URL + relative_link

        extra = event.find("div", class_="extra-info")

        events.append(Event(
            source="IFS",
            external_id=get_event_id(link),
            title=event.find("h4", class_="title").text.strip(),
            description=extra.text.strip() if extra else "Sem descrição",
            registration_period=event.find("dd").text.strip(),
            link=link,
        ))

    return events


if __name__ == "__main__":
    for event in get_events():
        print(event)