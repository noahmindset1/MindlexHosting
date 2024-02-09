from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist('file')
    for file in uploaded_files:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'Files uploaded successfully.'

@app.route('/run-python', methods=['POST'])
def run_python():
    # Install required modules
    subprocess.run(['pip', 'install', '-r', 'r.txt'])

    # Run main.py
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    return result.stdout

@app.route('/get-files', methods=['GET'])
def get_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify(files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
