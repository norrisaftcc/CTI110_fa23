from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """
    
  <h1>Hello from CTI110!</h1>

  <p>This is a webpage.<p>

  <p>Name: Mr. Norris</p>
  <p>Fave Pokemon: Bulbasaur</p>
  <p>Fave Vehicle: RAV 4</p>
  
  """


app.run(host='0.0.0.0', port=81)
