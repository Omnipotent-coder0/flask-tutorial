from flask import Flask

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
  # return 'hello world'
  return (
    '<h1>Hello World</h1>' 
    '<p>hello this is a paragraph tag</p>'
  )

if __name__ == '__main__':  
  print('hello this is inside if statement')
  app.run(host = '0.0.0.0',debug = True)