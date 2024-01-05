from flask import Flask, render_template, jsonify ,request
from database import load_jobs_from_db, load_job_from_db, post_in_db
app = Flask(__name__)

JOBS = load_jobs_from_db()

@app.route('/')
def hello_world():
  # return 'hello world'
  return render_template('home.html' , jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

@app.route('/job/<id>')
def job(id):
  job = load_job_from_db(id)
  # return jsonify(job)
  if not job:
    return render_template('notfound.html')
  return render_template('jobpage.html',job = job)

@app.route("/job/<id>/submitted" , methods = ['post'])
def submitted(id):
  job = load_job_from_db(id)
  data = request.form
  post_in_db(data,id)
  if not job:
    return render_template('notfound.html')
  return render_template('submitted.html' ,job = job,data = data)

if __name__ == '__main__':  
  print('hello this is inside if statement')
  app.run(host = '0.0.0.0',debug = True)