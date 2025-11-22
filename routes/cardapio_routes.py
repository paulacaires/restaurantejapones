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
  buscar_todos_cardapios,
  buscar_itens_cardapio
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
    itens_cardapio = buscar_itens_cardapio(supabase) or []

    return render_template("cardapio.html", 
                           cardapios=lista_cardapios,
                           itens_cardapio=itens_cardapio)

@cardapio_bp.route("/cardapio", methods=["POST"])
def adicionar_cardapio():
    supabase = current_app.supabase

    if not supabase:
        return redirect(url_for("cardapio.cardapio"))

    try:
        # ---------------------------
        # 1. Dados do formulário
        # ---------------------------
        data_cardapio   = request.form.get("data_cardapio")
        turno           = request.form.get("turno")
        entrada         = request.form.get("entrada")
        main_sushi      = request.form.get("main_sushi")
        main_ramen      = request.form.get("main_ramen")
        sobremesa       = request.form.get("sobremesa")
        bebida          = request.form.get("bebida")
        aumento_demanda = request.form.get("aumento_demanda") == "true"

        itens_selecionados = [entrada, main_sushi, main_ramen, sobremesa, bebida]

        # ---------------------------
        # 2. Verificar se cardápio já existe para data e momento
        # ---------------------------
        duplicado = (
            supabase.table(CARDAPIO_TABELA)
            .select("*")
            .eq("dia", data_cardapio)
            .eq("momento", turno)
            .execute()
        )

        if duplicado.data:
            print('Já existe duplicado!')
            return redirect(url_for("cardapio.cardapio"))

        # ---------------------------
        # 3. Buscar qtd mínima dos itens selecionados
        # ---------------------------
        itens_info = (
            supabase.table("item_cardapio")
            .select("id_item, nome_item, estoque_minimo")
            .in_("id_item", itens_selecionados)
            .execute()
        ).data

        # Transformar em dict fácil de usar
        info_por_id = {str(item["id_item"]): item for item in itens_info}

        # ---------------------------
        # 4. Calcular demanda básica
        # ---------------------------
        demanda_default = {
            item_id: info_por_id[item_id]["estoque_minimo"]
            for item_id in itens_selecionados
            if item_id is not None
        }

        # ---------------------------
        # 5. Se houver aumento de demanda, aumentar 30%
        # ---------------------------
        fator_aumento = 1.30 if aumento_demanda else 1.0

        demanda_final = {
            item_id: round(qtd * fator_aumento)
            for item_id, qtd in demanda_default.items()
        }

        # ---------------------------
        # 6. Verificar estoque
        # ---------------------------
        ids_para_verificar = list(demanda_final.keys())

        estoque_atual = (
            supabase.table("estoque")
            .select("id_item, quantidade")
            .in_("id_item", ids_para_verificar)
            .execute()
        ).data

        estoque_map = {str(item["id_item"]): item["quantidade"] for item in estoque_atual}

        # Verificar insuficiência
        insuficientes = []
        for item_id, qtd_necessaria in demanda_final.items():
            qtd_estoque = estoque_map.get(str(item_id), 0)
            if qtd_estoque < qtd_necessaria:
                insuficientes.append((item_id, qtd_estoque, qtd_necessaria))

        if insuficientes:
            msg = ""
            for id_item, estoque_atual, necessario in insuficientes:
                nome = info_por_id[id_item]["nome_item"]
                msg += f"- {nome}: tem {estoque_atual}, precisa de {necessario}\n"

            flash(f"🍣 Faltam ingredientes para montar o cardápio: {msg}.", "erro")
            return redirect(url_for("cardapio.cardapio"))

        # ---------------------------
        # 7. Registrar cardápio na tabela
        # ---------------------------
        payload = {
            "dia": data_cardapio,
            "momento": turno,
            "entrada": entrada,
            "main_sushi": main_sushi,
            "main_ramen": main_ramen,
            "sobremesa": sobremesa,
            "bebida": bebida,
            "aumento_demanda": aumento_demanda
        }

        supabase.table(CARDAPIO_TABELA).insert(payload).execute()

        # ---------------------------
        # 8. Descontar do estoque
        # ---------------------------
        for item_id, qtd_usada in demanda_final.items():
            estoque_atual = estoque_map[item_id]
            novo_estoque = estoque_atual - qtd_usada

            supabase.table("estoque").update({"quantidade": novo_estoque}).eq("id_item", item_id).execute()

        return redirect(url_for("cardapio.cardapio"))

    except Exception as e:
        print(f"Erro ao adicionar cardápio: {e}")
        return redirect(url_for("cardapio.cardapio"))


