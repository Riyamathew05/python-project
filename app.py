from flask import Flask,render_template,request

# Create the flask Application
app=Flask(__name__)

#create a dictionary for login

user_dict={'admin':'1234','deepa':'4567'}


# Define a route and corresponding view

@app.route('/')
def Hello():
    #return "Hello World!!!"
    # Call our html Page
    return render_template('index.html')

# Define a route and corresponding view Home page
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/emp_home', methods=['POST'])
def emp_home():
    username=request.form['username']
    pwd=request.form['password']
    if username not in user_dict:
        return render_template('login.html', msg='Invalid Username')
    elif user_dict[username]!=pwd:
        return render_template('login.html', msg='Invalid Password')
    else:
        return render_template('index.html')

    # Run flask Applications
if __name__=='__main__':
    app.run(debug=True)