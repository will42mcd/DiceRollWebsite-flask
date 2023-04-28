from flask import Flask, render_template, request
from roll_the_dice import roll_the_dice
import time



# Declare Flask App
app = Flask(__name__)

# Render main page
@app.route('/')
@app.route('/input')
def main_page():
    return render_template("input.html")


@app.route('/dice_roll', methods=['POST'])
def roll():
    # Dice Roll Variables
    dice_num = request.form["number of dice"]    
    results = roll_the_dice(int(dice_num))
    dice = results[0]
    dice_sum = results[1]
    
    # User Information
    user_ip = request.remote_addr
    browser = request.user_agent
    ts = int(time.time())
    log_path = f'./logs/user_log_{ts}.txt'
    
    # Write Log File
    with open(log_path, 'w') as file:
        file.write(f"User IP: {user_ip}\n")
        file.write(f"Browser Information: {browser}\n")
        file.write(f"Number of Dice: {dice_num}\n")
        file.write(f"Dice Results: {dice}\n")
        file.write(f"Sum of Dice: {dice_sum}\n")

    # Render Results Page
    return render_template(
        "results.html", 
        dice_num_text = dice_num, 
        dice_text = dice, 
        dice_sum_text = dice_sum 
        )

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
