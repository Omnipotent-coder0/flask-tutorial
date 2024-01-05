import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host_name = os.getenv('HOST')
db_name = os.getenv('DB')

my_secret = f'postgresql+psycopg2://{user}:{password}@{host_name}:5432/{db_name}'

engine = create_engine(my_secret)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results = True).execute(text("select * from jobs"))
        result_all = result.all()
        result_dict = []
        for row in result_all:
            result_dict.append(dict(row._mapping))
        return (result_dict)
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execution_options(stream_results = True).execute(text(f'select * from jobs where id = {id}'))
        result_all = result.all()
        if len(result_all) == 0:
            return None
        return (dict(result_all[0]._mapping))
    
def none_handler(para):
    for key in para:
        if len(para[key]) == 0:
            para[key] = None
        print('hello para key : ',key)
    return para


def post_in_db(data,id):
    with engine.connect() as conn:
        para ={
            'job_id' : id,
            'name' : data.get('name'),
            'mail' : data.get('mail'),
            'phone' : data.get('phone'),
            'education' : data.get('edu'),
            'resume' : data.get('resume'),
            'linkedin' : data.get('linkedin')
        }
        para = none_handler(para)  # for empty None that becomes null in postgresql rather than being empty string
        query = text("insert into application (job_id, name, mail, phone, education, resume, linkedin) values (:job_id,:name,:mail,:phone,:education,:resume,:linkedin)")
        result = conn.execute(query,para)
        conn.commit()
