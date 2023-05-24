from dotenv import dotenv_values
import ast

env_dict = dotenv_values('.env')

EMAIL_SENDER: str = str(env_dict["EMAIL_SENDER"])
EMAIL_PASSWORD: str = str(env_dict["EMAIL_PASSWORD"])
SMTP_SERVER: str = str(env_dict["SMTP_SERVER"])
