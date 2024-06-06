from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user_data')
def user_data():
    return render_template('user_data.html')



if __name__ =="__main__":
    app.run(debug=True)

## google form with in two 2