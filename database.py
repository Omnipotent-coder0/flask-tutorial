import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host_name = os.getenv('HOST')
db_name = os.getenv('DB')

# print(user)

my_secret = f'postgresql+psycopg2://{user}:{password}@{host_name}:5432/{db_name}'

engine = create_engine(my_secret)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
        result_all = result.all()
        return (result_all) 