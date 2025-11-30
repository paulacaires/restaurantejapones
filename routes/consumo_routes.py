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
  buscar_todos_consumos
)

CARDAPIO_TABELA = "cardapio"
CONSUMO_TABELA = "consumo"
CLIENTE_TABELA = "cliente"

# Criação do blueprint
consumo_bp = Blueprint("consumo", __name__)

@consumo_bp.route("/consumo", methods=["GET"])
def consumo():
    supabase = current_app.supabase

    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500
        
    lista_consumos = buscar_todos_consumos(supabase) or []
    
    return render_template('consumo.html', consumos=lista_consumos)

@consumo_bp.route("/consumo", methods=["POST"])
def registrar_consumo():
    supabase = current_app.supabase

    if not supabase:
        flash("Erro ao conectar ao banco de dados.", "erro")
        return redirect(url_for("consumo.consumo"))

    try:
        # Dados enviados pelo form
        cliente_cpf = request.form.get("cliente_cpf")
        dia         = request.form.get("dia")
        momento     = request.form.get("momento")
        avaliacao   = request.form.get("avaliacao")

        # Validação básica
        if not cliente_cpf or not dia or not momento:
            flash("Preencha todos os campos obrigatórios.", "aviso")
            return redirect(url_for("consumo.consumo"))

        # === Buscar o cardápio correspondente (dia + momento) ===
        cardapio_resp = (
            supabase.table(CARDAPIO_TABELA)
            .select("id_cardapio")
            .eq("dia", dia)
            .eq("momento", momento)
            .execute()
        )

        print(cardapio_resp.data[0]['id_cardapio'])

        if not cardapio_resp or not cardapio_resp.data:
            flash("Não existe cardápio cadastrado para esse dia e momento.", "erro")
            return redirect(url_for("consumo.consumo"))

        cardapio_id = cardapio_resp.data[0]['id_cardapio']

        # Payload para inserir
        novo_consumo = {
            "cliente_cpf": cliente_cpf,
            "cardapio_id": cardapio_id,
            "avaliacao": int(avaliacao) if avaliacao else None
        }

        # === Verificar se já existe consumo para esse cliente nesse cardápio ===
        consumo_existente = (
            supabase.table("consumo")
            .select("id_consumo")
            .eq("cliente_cpf", cliente_cpf)
            .eq("cardapio_id", cardapio_id)
            .maybe_single()
            .execute()
        )

        if consumo_existente and consumo_existente.data:
            flash(f"O cliente já entrou no Restaurante Japonês no dia {dia} no período {momento}", "erro")
            return redirect(url_for("consumo.consumo"))
        
        else:
            # Inserir novo consumo
            insert_resp = (
                supabase.table("consumo")
                .insert(novo_consumo)
                .execute()
            )
            flash("Consumo registrado com sucesso!", "sucesso")

        return redirect(url_for("consumo.consumo"))

    except Exception as e:
        print(f"Erro ao registrar consumo: {e}")
        flash("Ocorreu um erro ao registrar o consumo.", "erro")
        return redirect(url_for("consumo.consumo"))
