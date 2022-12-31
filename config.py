from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQBDs6xBrEi1fBwJXQFuN6DYQB8vVza7lPzjLiQ70_cwjg3MjU4d1mPb8DiHEjOs4Zbpy3Ty5RWHOL6PMXekcBjLeB1MxM_ib6f9vPosGllKVhubnsNT67FbbcgwNuQSlyZgim1PY5_nm-2qTxHATCW4CgWqzt_NErplRmetDa8vJ_d43ycVobOiDZx08iDVgoxljjfAddz9FwECZUKOSqbV3RAhk8JFj4cJGoONytuxyfBP5E10AEhuvyZYiGsCqhGQTWkylgXCdU_JNGTNU-tEFGpbNMgIoxhsWWgdRO_HsppVj8u0-HSqZHJHjX7KPJfe8ofbs3ru5VbWzxUuk84UVHsUiQA")
BOT_TOKEN = getenv("2084060024:AAG2qH4BL9PXPKFnvmuIxwDjcKFJG-jLXEQ")
BOT_NAME = getenv("BOT_NAME", "Phoenix")

API_ID = int(getenv("6246021"))
API_HASH = getenv("112a701ebaf8995ce35ba7ae4433eb4b")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1417352329").split()))
