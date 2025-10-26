from flask import Flask, render_template, url_for

# Inicializar Flask
app = Flask(__name__)

@app.route('/')
def index():

    #Alterar esse nome com o arquivo do módulo que queira testar ou a tela inicial na fase de implentação
    return render_template('test_patterns.html')

@app.route('/test_patterns')
def test_patterns():
    return render_template('test_patterns.html')

if __name__ == '__main__':
    app.run(debug=True)