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
        result_dict = []
        for row in result_all:
            result_dict.append(dict(row._mapping))
        return (result_dict)
    
# id = 3
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execution_options(stream_results = True).execute(text(f'select * from jobs where id = {id}'))
        result_all = result.all()
        if len(result_all) == 0:
            return None
        return (dict(result_all[0]._mapping))