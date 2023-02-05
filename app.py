from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome here to me"
@app.route('/sangarsh')
def sangarsh():
    return "Hope all doing well"


if __name__=="__main__":
    app.run(debug=True)
    