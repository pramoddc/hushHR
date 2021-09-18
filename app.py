from flask import Flask, render_template, request
import json



app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")  

@app.route('/role', methods=['GET', 'POST'])
def sign_up():
    message = ""
    if request.method == 'POST':
        selectedRole= request.form.get('selectRole')
        if selectedRole == 1:           
            message = " Junior developer selected"
        elif selectedRole==2:
            message = " Senior developer selected"
        elif selectedRole==3:
            message = " Solution Architect "
    return message

    
if __name__ == "__main__":
    app.run(debug=True)
