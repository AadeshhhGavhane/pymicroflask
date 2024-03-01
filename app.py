from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to store words and their meanings
dictionary = {}

@app.route('/')
def index():
    return render_template('index.html', dictionary=dictionary)

@app.route('/add_word', methods=['POST'])
def add_word():
    word = request.form['word']
    meaning = request.form['meaning']
    dictionary[word] = meaning
    return render_template('index.html', dictionary=dictionary)

@app.route('/update_word', methods=['POST'])
def update_word():
    word = request.form['word']
    meaning = request.form['meaning']
    if word in dictionary:
        dictionary[word] = meaning
    return render_template('index.html', dictionary=dictionary)

@app.route('/delete_word', methods=['POST'])
def delete_word():
    word = request.form['word']
    if word in dictionary:
        del dictionary[word]
    return render_template('index.html', dictionary=dictionary)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
