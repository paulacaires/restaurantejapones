import os
from flask import Flask, render_template, url_for
from supabase import create_client, Client
from dotenv import load_dotenv

from backend.database.data_acess import (
    buscar_todos_funcionarios,
    buscar_todos_cardapios
    )
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# --- Configuração do Supabase ---
try:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
except Exception as e:
    print(f"Erro ao conectar com Supabase: {e}")
    supabase = None

@app.route('/')
def index():

    #Alterar esse nome com o arquivo do módulo que queira testar ou a tela inicial na fase de implentação
    return render_template('index.html')

@app.route('/test_patterns')
def test_patterns():
    return render_template('test_patterns.html')


@app.route('/funcionarios', methods=['GET']) 
def funcionarios():
    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500

    lista_funcionarios = buscar_todos_funcionarios(supabase) or []
    
    return render_template('funcionarios.html', funcionarios=lista_funcionarios)

@app.route('/cardapio')
def cardapio():
    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500
        
    lista_cardapios = buscar_todos_cardapios(supabase) or []
    
    return render_template('cardapio.html', cardapios=lista_cardapios)

if __name__ == '__main__':
    app.run(debug=True)