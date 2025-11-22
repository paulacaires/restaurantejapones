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
    buscar_itens_cardapio,
    verificar_baixo_estoque
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

    itens_alerta = verificar_baixo_estoque(lista_estoque)

    return render_template(
        "estoque.html",
        estoque=lista_estoque,
        itens_cardapio=itens_cardapio,
        itens_alerta=itens_alerta
    )

@estoque_bp.route("/estoque", methods=["POST"])
def adicionar_item_estoque():
    supabase = current_app.supabase

    if not supabase:
        flash("Erro ao conectar ao banco de dados.", "erro")
        return redirect(url_for("estoque.estoque"))

    try:
        # Dados enviados pelo form
        id_item         = request.form.get("id_item")
        quantidade      = request.form.get("quantidade")
        data_validade   = request.form.get("data_validade")

        # Validações básicas
        if not id_item or not quantidade or not data_validade:
            flash("Preencha todos os campos antes de continuar.", "aviso")
            return redirect(url_for("estoque.estoque"))

        payload = {
            "id_item": int(id_item),
            "quantidade": int(quantidade),
            "data_validade": data_validade
        }

        # Buscar se já existe um registro de estoque para esse item
        response = (
            supabase.table(ESTOQUE_TABELA)
            .select("id_estoque, quantidade")
            .eq("id_item", id_item)
            .maybe_single()
            .execute()
        )

        # Se já existe um registro no estoque para esse item
        if response and response.data:
            id_estoque = response.data["id_estoque"]
            quantidade_atual = response.data["quantidade"]

            nova_quantidade = int(quantidade_atual) + int(quantidade)

            # Atualizar quantidade e validade
            supabase.table(ESTOQUE_TABELA).update({
                "quantidade": nova_quantidade,
                "data_validade": data_validade
            }).eq("id_estoque", id_estoque).execute()

            flash(f"Estoque atualizado com sucesso! Quantidade atual: {nova_quantidade}.", "sucesso")

        else:
            # Criar novo registro
            supabase.table(ESTOQUE_TABELA).insert({
                "id_item": id_item,
                "quantidade": quantidade,
                "data_validade": data_validade,
            }).execute()

            flash("Item adicionado ao estoque com sucesso!", "sucesso")

        return redirect(url_for("estoque.estoque"))
        
    except Exception as e:
        print(f"Erro ao adicionar item ao estoque: {e}")
        flash("Ocorreu um erro ao tentar adicionar o item ao estoque.", "erro")
        return redirect(url_for("estoque.estoque"))

