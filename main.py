from core.database import create_db, get_session
from sources.ifs import get_events
from core import repository
from notifications.email import send_email


def sync_events():
    events = get_events()
    new_events = []

    with get_session() as session:
        for event in events:
            if not repository.exists(session, event):
                repository.save_if_new(session, event)
                new_events.append(event)
                print(f"Novo evento: {event.title}")
            else:
                print(f"Já existe: {event.title}")

    return new_events


def main():
    create_db()

    new_events = sync_events()

    if new_events:
        send_email(new_events)
        print(f"{len(new_events)} novo(s) evento(s) enviado(s) por e-mail.")
    else:
        print("Nenhum evento novo encontrado.")


if __name__ == "__main__":
    main()