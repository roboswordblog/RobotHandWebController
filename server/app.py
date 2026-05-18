from flask import Flask, render_template, jsonify,request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/sendHandAngles")
def getData():
    one = request.get_json("1")
    two = request.get_json("2")
    three = request.get_json("3")
    four = request.get_json("4")
    five = request.get_json("5")
    
if __name__ == "__main__":
  app.run(debug=True)
