from flask import Flask, render_template, jsonify,request
import serial
app = Flask(__name__)
ser = serial.Serial('COM3', baudrate=9600, timeout=1)

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
    message = f"{one},{two},{three},{four},{five},{six}"
    ser.write(message.encode('utf-8'))
    return jsonify({"good":True})

if __name__ == "__main__":
  app.run(debug=True)
