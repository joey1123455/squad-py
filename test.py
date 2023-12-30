from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
a = Squad(secret_key=config["SECRET_KEY"])