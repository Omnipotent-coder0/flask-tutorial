from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengeluru, India',
#     'salary': 'Rs. 10,00,000'
#   },
#   {
#     'id':2,
#     'title': 'Data Scientist',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 15,00,000'
#   },
#   {
#     'id':3,
#     'title': 'Frontend Engineer',
#     'location': 'Remote'
#   },
#   {
#     'id':4,
#     'title': 'Backend Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$120,000'
#   }
# ]

JOBS = load_jobs_from_db()

@app.route('/')
def hello_world():
  # return 'hello world'
  return render_template('home.html' , jobs = JOBS,project_name = "Flask")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':  
  print('hello this is inside if statement')
  app.run(host = '0.0.0.0',debug = True)