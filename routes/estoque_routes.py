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
    buscar_todos_itens_estoque
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
    
    return render_template('estoque.html', estoque=lista_estoque)

@estoque_bp.route("/estoque/adicionar", methods=["POST"])
def adicionar_item_estoque():
    supabase = current_app.supabase
    
    try:
        id_item = request.form.get("id_item")
        quantidade = request.form.get("quantidade")
        data_validade = request.form.get("data_validade")

        if not id_item or not quantidade:
            flash("Por favor, selecione o item e informe a quantidade.", "erro")
            return redirect(url_for("estoque.listar_estoque"))

        novo_item = {
            "id_item": int(id_item),
            "quantidade": float(quantidade),
            "data_validade": data_validade or None,
        }

        supabase.table(ESTOQUE_TABELA).insert(novo_item).execute()

        flash("Item adicionado ao estoque com sucesso!", "sucesso")
        return redirect(url_for("estoque.listar_estoque"))

    except Exception as e:
        print(f"Erro ao adicionar item ao estoque: {e}")
        flash("Erro ao adicionar item ao estoque.", "erro")
        return redirect(url_for("estoque.listar_estoque"))
