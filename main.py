from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist('file')
    for file in uploaded_files:
        file.save(file.filename)
    return 'Files uploaded successfully.'

@app.route('/run-python', methods=['POST'])
def run_python():
    # Install required modules
    subprocess.run(['pip', 'install', '-r', 'r.txt'])

    # Run main.py
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
