from core.database import create_db
from core.database import get_session
from sources.ifs import get_events
from core import repository

def sync_events():
    events = get_events()

    with get_session() as session:
        for event in events:
            if not repository.exists(session, event):
                repository.save(session, event)
                print(f"Novo evento: {event.title}")
            else:
                print(f"Já existe: {event.title}")

def main():
    create_db()
    sync_events()

if __name__ == "__main__":
    main()