import os
from flask import *
from werkzeug.utils import secure_filename
import classify 
import sys
import io

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Read the contents of the file into a BytesIO object
            file_stream = io.BytesIO()
            file.save(file_stream)
            # Seek to the beginning of the stream
            file_stream.seek(0)

            result = classify.check(file_stream)
            return render_template('main.html', result=result)
        
    return render_template('main.html')
 
if __name__ == '__main__':  
   app.run(debug=True)
