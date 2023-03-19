import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Execute the Python script and capture its output
    output = subprocess.check_output(['python', 'app.py']).decode('utf-8')
    # Render the output in a simple HTML template
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
