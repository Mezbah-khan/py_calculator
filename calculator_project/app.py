from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ''
    if request.method == "POST":
        try:
            # Get the expression from the user input
            expression = request.form.get('expression')
            # Evaluate the expression
            result = str(eval(expression))
        except Exception as e:
            result = "Error"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
