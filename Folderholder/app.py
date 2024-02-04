from flask import Flask, render_template
import calendar

app = Flask(__name__)
port = 4000

# Initialize an empty list
user_list = []

# Get user input for the number of assignments
num_elements = int(input("How many assignments do you have? "))

# Loop to get user input for each assignment
for _ in range(num_elements):
    element_input = input("Enter the assignments in order: ")
    user_list.append(element_input)

# Generate the calendar for January 2024
calendar_output = calendar.TextCalendar(calendar.SUNDAY)
calendar_html = calendar_output.formatmonth(2024, 1)

# Render the HTML template with the dynamic content
@app.route('/')
def index():
    return render_template('output.html', calendar_html=calendar_html, user_list=user_list)

if __name__ == '__main__':
    app.run(port=port, debug=True)
