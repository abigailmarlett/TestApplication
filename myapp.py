from flask import Flask
app = Flask(__name__)

#you could add a parameter like @app.route("/myjoke/<jtype>", methods=["GET"]) and use jtype as the parameter 
@app.route("/myjoke", methods=["GET"])
def mymethod ():
    return "Why did the chicken cross the street? Ha! ha, ha!"

@app.route("/mysecondjoke", methods=["GET"])
def mymethod2 ():
    return "There are 10 types of people"

if __name__ == '__main__':
    app.run(debug=True)