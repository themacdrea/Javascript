from pathlib import Path
from sqlalchemy import create_engine
from config import username, password, host, port, database_name

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database_name}")

data = engine.execute("SELECT * FROM female")

for record in data:
    print(record)

