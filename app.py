from flask import Flask, render_template

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
  # return 'hello world'
  return render_template('home.html')

if __name__ == '__main__':  
  print('hello this is inside if statement')
  app.run(host = '0.0.0.0',debug = True)