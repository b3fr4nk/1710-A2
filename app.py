from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template("froyo_form.html")

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        "flavor":request.args.get("flavor"),
        "toppings":request.args.get("toppings")
        }
    return render_template("froyo_results.html", **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    form = """
        <form action="/favorites_results" method="GET">
            What is your favorite animal? <br>
            <input type="text" name="animal">
            What is your favorite color? <br>
            <input type="text" name="color">
            What is your favorite city? <br>
            <input type="text" name="city">
            <input type="submit" value="submit">
        </form>
    """
    return form

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    animal = request.args.get("animal")
    color = request.args.get("color")
    city = request.args.get("city")
    return f"wow I didn't know {color} {animal}s lived in {city}"
    

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    form = """
        <form action="/message_results" method="POST">
            What is the secret message? <br>
            <input type="text" name="message">
            <input type="submit" value="submit">
        </form>
    """
    return form

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get("message")
    print(message)
    return sort_letters(message)

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
        "operand1":request.args.get("operand1"),
        "operation":request.args.get("operation"),
        "operand2":request.args.get("operand2")
    }
    if context["operand1"].isnumeric() and context["operand2"].isnumeric():
        num1 = int(context["operand1"])
        num2 = int(context["operand2"])
        if context["operation"] == "add":
            context["result"] = num1 + num2
        elif context["operation"] == "subtract":
            context["result"] = num1 - num2
        elif context["operation"] == "divide":
            context["result"] = num1 / num2
        elif context["operation"] == "multiply":
            context["result"] = num1 * num2

    else: 
        context["result"] = "Error please enter valid number(s)"

    print(context["result"])

    return render_template("calculator_results.html", **context)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get("horoscope_sign")

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES[horoscope_sign]

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randrange(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
