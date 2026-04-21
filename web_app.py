from flask import Flask, render_template, request
from orders import check_price

# IMPORTANT: templates folder is inside bot
app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        runs = request.form.get("runs")

        # validation
        if not runs or not runs.isdigit():
            result = "Invalid input ❌"
        else:
            runs = int(runs)
            output = []

            for i in range(runs):
                price = check_price()
                output.append(price)

            result = output

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)