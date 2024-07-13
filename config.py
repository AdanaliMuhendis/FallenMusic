from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "33"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/430-490-07-01")
START_IMG = getenv("START_IMG", "https://te.legra.ph/430-490-07-01")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SohbetAlemi")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Alemciyiz")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5988763828").split()))


FAILED = "https://te.legra.ph/430-490-07-01"
