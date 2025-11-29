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
    buscar_todas_reservas, 
    buscar_todas_mesas, 
    buscar_todos_clientes
)

reservas_bp = Blueprint("reservas", __name__)

@reservas_bp.route("/reservas", methods=["GET"])
def reservas():
    supabase = current_app.supabase

    if not supabase:
        flash("Erro de conexão com o banco de dados.", "erro")
        return render_template('reservas.html', reservas=[], mesas=[], clientes=[])


    lista_reservas = buscar_todas_reservas(supabase) or []
    lista_mesas = buscar_todas_mesas(supabase) or []
    lista_clientes = buscar_todos_clientes(supabase) or []
    
    return render_template(
        'reservas.html', 
        reservas=lista_reservas,
        mesas=lista_mesas,
        clientes=lista_clientes
    )

@reservas_bp.route("/reservas/adicionar", methods=["POST"])
def adicionar_reserva():
    supabase = current_app.supabase

    try:
        cpf_cliente = request.form.get("cliente")
        numero_mesa = request.form.get("mesa")
        data        = request.form.get("data")
        momento     = request.form.get("momento")

        nova_reserva = {
            "cliente_responsavel_cpf": cpf_cliente,
            "mesa_numero": int(numero_mesa),
            "dia_reserva": data,
            "momento_refeicao": momento
        }


        supabase.table("reserva_mesas").insert(nova_reserva).execute()

        flash("✅ Mesa reservada com sucesso!", "sucesso")
        return redirect(url_for("reservas.reservas"))

    except Exception as e:
        msg_erro = str(e)
        if "duplicate key" in msg_erro or "violates unique constraint" in msg_erro:
            flash(f"⚠️ A Mesa {numero_mesa} já está reservada para este horário!", "erro")
        else:
            flash(f"❌ Erro ao realizar reserva: {msg_erro}", "erro")
            
        print(f"Erro no backend: {e}")
        return redirect(url_for("reservas.reservas"))