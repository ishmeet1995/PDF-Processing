from flask import Flask , render_template, request
import  os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        file = request.files['file']
        file.save( os.path.join(app.config['UPLOAD_FOLDER'],  file.filename))
        return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
