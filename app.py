from flask import Flask 
app=Flask(__name__)
@app.route("/")
def home():
    return "i am rushi and i am learning flask"

@app.route("/about")
def about():
    return "this is about page"
@app.route("/myself")
def myself():
    return "hi i am rushi and i am enstusatic learner"

if __name__=="__main__":
    app.run(debug=True)