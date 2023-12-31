import json
from sqlalchemy import create_engine, text

with open("config.json",'r') as json_file:
    config = json.load(json_file)

user = config['USER']
password = config['PASSWORD']
host_name = config['HOST']
db_name = config['DB']


# print(config)

my_secret = f'postgresql+psycopg2://{user}:{password}@{host_name}:5432/{db_name}'

# my_secret = os.environ['DB_DATA']

# print(type(my_secret))

engine = create_engine(my_secret)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
        result_all = result.all()
        return result_all
        # for row in result_all:
        #     print(row.id, row.title, row.location, row.salary, row.currency,
        #         row.responsibilities, row.requirements)


    # result_dict.append(dict(row))

    
  # print("result : ",result)
  # print('result type : ',type(result))
  # print('result.all() : ',result.all())
  # print('result.all type : ',type(result.all()))
  # print(result)