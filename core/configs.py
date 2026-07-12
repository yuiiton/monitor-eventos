import os
from dotenv import load_dotenv

load_dotenv()


EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TARGET = os.getenv("EMAIL_TARGET")