from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@localhost:5434/postgres",
)

# TEST_DATABASE_URL = env.str(
#     "TEST_DATABASE_URL",
#     default="postgresql+asyncpg://postgres_test:postgres_test@localhost:5435/postgres_test",
# )





