from flask import Flask, render_template      
import os
STATIC_DIR = os.path.abspath('static')
TEMPLATE_DIR = os.path.abspath('templates')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def home():
    print(os.getcwd())
    return render_template("main.html")
    
@app.route("/result")
def result():
    return render_template("main2.html")
    
if __name__ == "__main__":
    app.run(debug=True)