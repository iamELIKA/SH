from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

# Load the Excel file
file_path = 'Final_Team_Details.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Function to get the riddle based on the team code
def get_riddle(teamcode):
    # Filter the data based on the team code
    team_data = data[data['teamcode'] == teamcode]
    
    if not team_data.empty:
        # Get the riddle (assuming all team members have the same riddle)
        riddle = team_data.iloc[0]['riddle']
        return f"The riddle for team {teamcode} is: {riddle}"
    else:
        return "Team code not found."

# Route to display the form and result
@app.route('/', methods=['GET', 'POST'])
def index():
    riddle = None
    if request.method == 'POST':
        teamcode = request.form['teamcode']
        riddle = get_riddle(teamcode)
    
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Team Riddle</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            h1 {
                font-size: 24px;
                margin-bottom: 20px;
            }
            form {
                display: flex;
                flex-direction: column;
            }
            label {
                margin-bottom: 10px;
                font-weight: bold;
                text-align: left;
            }
            input[type="text"] {
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                padding: 10px;
                background-color: #28a745;
                color: #fff;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #218838;
            }
            h2 {
                margin-top: 20px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Enter Your Team Code</h1>
            <form method="POST">
                <label for="teamcode">Team Code:</label>
                <input type="text" id="teamcode" name="teamcode" required>
                <button type="submit">Get Riddle</button>
            </form>

            {% if riddle %}
            <h2>{{ riddle }}</h2>
            {% endif %}
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, riddle=riddle)

if __name__ == '__main__':
    app.run(debug=True)
