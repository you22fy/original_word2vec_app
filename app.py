from flask import Flask,request,render_template
from model import calculate_emotion_vector,search_most_similar
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new',methods=['GET',"POST"])
def new():
    if request.method == 'GET':
        return render_template('new.html')
    elif request.method == 'POST':
        return render_template('new.html')

@app.route('/show',methods=['GET',"POST"])
def show():
    if request.method == 'GET':
        return render_template('result.html')
    elif request.method == 'POST':
        char = request.form.getlist("character")
        ideal = request.form.getlist("ideal")
        key_list = char + ideal
        emothion_vector = calculate_emotion_vector(key_list)
        max_lang = search_most_similar(emothion_vector)
        return render_template("show.html",max_lang = max_lang)

if __name__ == "__main__":
    app.run(debug=True)
