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
        form{
         background-color: blue;
         display: flex;
         flex-direction: column;
         width: 25%;
         padding: 20px;
         border-radius: 10px;
        }
        </style>
    </head>
    <body>
        <h1>Enter Your Team Code</h1>
        <form method="POST">
            <label for="teamcode" style="font-weight: bold;">Team Code:</label>
            <input type="text" id="teamcode" name="teamcode" required>
            <button type="submit" style = "cursor:pointer">Get Riddle</button>
        </form>

        {% if riddle %}
        <h2>{{ riddle }}</h2>
        {% endif %}
    </body>
    </html>
    """
    
    return render_template_string(html_template, riddle=riddle)

if __name__ == '__main__':
    app.run(debug=True)
