import smtplib

from email.message import EmailMessage

from core.models import Event
from core.configs import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_USER,
    EMAIL_PASSWORD,
    EMAIL_TARGET,
)


def create_email(events: list[Event]) -> EmailMessage:
    """Cria a mensagem de email com os novos eventos."""

    message = EmailMessage()

    message["Subject"] = f"{len(events)} novo(s) evento(s) encontrado(s)"
    message["From"] = EMAIL_USER
    message["To"] = EMAIL_TARGET

    html = """
    <html>
        <body>
            <h2>Novos eventos encontrados</h2>
    """

    for event in events:
        html += f"""
            <hr>

            <h3>{event.title}</h3>

            <p>
                <strong>Fonte:</strong> {event.source}
            </p>

            <p>
                <strong>Descrição:</strong><br>
                {event.description}
            </p>

            <p>
                <strong>Período de inscrição:</strong><br>
                {event.registration_period}
            </p>

            <p>
                <a href="{event.link}">
                    Acessar evento
                </a>
            </p>
        """

    html += """
        </body>
    </html>
    """

    message.set_content(
        "Seu cliente de email não suporta HTML."
    )

    message.add_alternative(
        html,
        subtype="html"
    )

    return message


def send_email(events: list[Event]) -> None:
    """Envia um email contendo os novos eventos."""

    if not events:
        return

    if not EMAIL_USER or not EMAIL_PASSWORD or not EMAIL_TARGET:
        raise RuntimeError(
            "As configurações de email não foram definidas."
        )

    message = create_email(events)

    with smtplib.SMTP_SSL(
        EMAIL_HOST,
        EMAIL_PORT
    ) as smtp:

        smtp.login(
            EMAIL_USER,
            EMAIL_PASSWORD
        )

        smtp.send_message(message)