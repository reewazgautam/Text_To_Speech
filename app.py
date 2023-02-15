from flask import Flask, request, render_template
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speech', methods=['POST'])
def speech():
    text = request.form['text']
    engine.say(text)
    engine.startLoop(False)
    engine.iterate()
    engine.endLoop()
    return text

if __name__ == '__main__':
    app.run(debug=True)
