from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from backend.database.data_acess import (
    buscar_todos_itens_estoque,
    buscar_itens_cardapio
)

# Nome das tabelas no Supabase
ESTOQUE_TABELA = "estoque"

# Criação do blueprint
estoque_bp = Blueprint("estoque", __name__)

@estoque_bp.route("/estoque", methods=["GET"])
def estoque():
    supabase = current_app.supabase

    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500
        
    lista_estoque = buscar_todos_itens_estoque(supabase) or []
    itens_cardapio = buscar_itens_cardapio(supabase) or []

    return render_template(
        "estoque.html",
        estoque=lista_estoque,
        itens_cardapio=itens_cardapio
    )

@estoque_bp.route("/estoque/adicionar", methods=["POST"])
def adicionar_item_estoque():
    supabase = current_app.supabase
    if not supabase:
        flash("Erro ao conectar ao banco de dados.", "erro")
        return redirect(url_for("estoque.estoque"))

    try:
        # Dados enviados pelo form
        id_item       = request.form.get("id_item")
        quantidade      = request.form.get("quantidade")
        data_validade   = request.form.get("data_validade")

        # Validações básicas
        if not id_item or not quantidade or not data_validade:
            flash("Por favor, selecione o item e informe a quantidade.", "erro")
            return redirect(url_for("estoque.estoque"))
        
        payload = {
            "id_item": int(id_item),
            "quantidade": int(quantidade),
            "data_validade": data_validade
        }

        response = supabase.table(ESTOQUE_TABELA).insert(payload).execute()

        if response.data:
            print(response.data[0])
            return redirect(url_for("estoque.estoque"))
    
        return None  # deu algum erro silencioso

    except Exception as e:
        print(f"Erro ao adicionar item ao estoque: {e}")
        return redirect(url_for("estoque.estoque"))
