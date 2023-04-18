"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
  <!doctype html>
  <html>
  Hi! This is the home page.
  <a  href="/hello">Say Hello</a>
  </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <a href='/'>Home</a>
        <form action="/greet">
          What's your name? <input type="text" name="person" required>
          <label for='compliments'> Choose Wisely: </label>
          <select required name='compliments' id='compliments'>
            <option value='' selected disabled> Pick Your Poison </option>
            <option value='Cool'>Cool</option>
            <option value='Awesome'>Awesome</option>
            <option value='Terrific'>Terrific</option>
            <option value='Interesting'>Interesting</option>
            <option value='Neato'>Neato</option>
            <option value='Fantabulous'>Fantabulous</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get('compliments')  # choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment.lower()}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
