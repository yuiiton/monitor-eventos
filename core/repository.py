from sqlmodel import Session, select
from core.models import Event

def save_if_new(session: Session, event: Event) -> bool:
    if exists(session, event):
        return False

    session.add(event)
    session.commit()
    session.refresh(event)

    return True

def exists(session: Session, event: Event) -> bool:
        statement = select(Event).where(
            Event.source == event.source,
            Event.external_id == event.external_id,
        )

        result = session.exec(statement).first()

        return result is not None