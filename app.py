from flask import Flask, request

# The Flask app must be top-level for Render (gunicorn app:app)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default message on first load
    result = "<span style='color:blue'>Enter a number to analyze it!</span>"

    if request.method == 'POST':
        user_num = request.form.get('myNumber')

        try:
            n = float(user_num)

            square = n ** 2
            cube = n ** 3
            even_odd = "even" if n % 2 == 0 else "odd"

            result = f"""
            <div style='color:green; margin-top:20px;'>
                <b>Results for {n}:</b><br>
                Square: {square}<br>
                Cube: {cube}<br>
                Even/Odd: {even_odd}
            </div>
            """
        except:
            result = "<span style='color:red'>Please enter a valid number!</span>"

    # --- HTML page template ---
    html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Number Analyzer</title>
    </head>
    <body>
        <h2 align="center">Flask Number Analyzer</h2>
        <form method="post" action="/">
            <label for="myNumber">Enter a number:</label>
            <input type="text" id="myNumber" name="myNumber">
            <input type="submit" value="Analyze">
        </form>
        {result}
    </body>
    </html>
    """
    return html_page

# --- REMOVE FOR DEPLOY ---
# if __name__ == '__main__':
#     app.run(debug=True)
# -------------------------
