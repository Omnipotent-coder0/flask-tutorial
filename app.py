from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db
app = Flask(__name__)

JOBS = load_jobs_from_db()

@app.route('/')
def hello_world():
  # return 'hello world'
  return render_template('home.html' , jobs = JOBS,project_name = "Flask")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

@app.route('/job/<id>')
def job(id):
  job = load_job_from_db(id)
  return jsonify(job)

if __name__ == '__main__':  
  print('hello this is inside if statement')
  app.run(host = '0.0.0.0',debug = True)