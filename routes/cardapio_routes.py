from flask import (
    Blueprint,
    render_template,
    current_app
)

from backend.database.data_acess import (
  buscar_todos_cardapios
)

# Nome da tabela no Supabase
CARDAPIO_TABELA = "cardapio"

# Criação do blueprint
cardapio_bp = Blueprint("cardapio", __name__)

@cardapio_bp.route("/cardapio", methods=["GET"])
def cardapio():
    # Pega a conexão do app
    supabase = current_app.supabase
    
    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500

    lista_cardapios = buscar_todos_cardapios(supabase) or []

    return render_template("cardapio.html", cardapios=lista_cardapios)


