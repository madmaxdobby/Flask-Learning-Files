from flask import Flask 
app=Flask(__name__)
@app.route("/")
def home():
    return "i am rushi and i am learning flask"

@app.route("/about/users")
def about():
    return "this is page about all the users"
@app.route("/about/<user>")
def myself(user):
    return f"hi i am {user} and i am enstusatic learner"
@app.route("/about/<user>/<course>")
def my(user,course):
    return f"hi i am {user} and i am enstusatic learner and i do {course}"

if __name__=="__main__":
    app.run(debug=True)