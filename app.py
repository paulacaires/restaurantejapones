import os
from flask import Flask, render_template
from supabase import create_client, Client
from dotenv import load_dotenv

# [BLUEPRINTS]
from routes.estoque_routes import estoque_bp
from routes.cardapio_routes import cardapio_bp
from routes.funcionarios_routes import funcionarios_bp
from routes.clientes_routes import clientes_bp
from routes.reservas_routes import reservas_bp

def create_app():

    load_dotenv()

    # Inicializar Flask
    app = Flask(__name__)
    app.secret_key = os.urandom(24)

    # --- Configuração do Supabase ---
    try:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        app.supabase: Client = create_client(url, key)
    except Exception as e:
        print(f"Erro ao conectar com Supabase: {e}")
        app.supabase = None

    # Blueprints
    app.register_blueprint(estoque_bp)
    app.register_blueprint(cardapio_bp)
    app.register_blueprint(funcionarios_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(reservas_bp)

    return app

# Para rodar localmente
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)