from flask import Flask ,render_template

app = Flask(__name__)
# 127.0.0.1:2525/
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')   #urls
def about():
    return render_template('about.html')

@app.route('/contact')   #urls
def contact():
    return render_template('contact.html')





if __name__ == "__main__":
    app.run(debug=True)



