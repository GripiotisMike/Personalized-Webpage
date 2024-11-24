from flask import Flask, render_template
import datetime

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route("/")
def hello_world():
    # Get the current year dynamically
    year = datetime.datetime.today().year
    # Render the 'index.html' template and pass the year to the template
    return render_template("index.html", year=year)

# Run the application in debug mode if executed directly
if __name__ == "__main__":
    app.run(debug=True)
