from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test_patterns.html')

@app.route('/test_patterns')
def test_patterns():
    return render_template('test_patterns.html')

if __name__ == '__main__':
    app.run(debug=True)