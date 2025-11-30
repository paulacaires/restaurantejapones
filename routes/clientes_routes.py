from flask import (
    Blueprint,
    jsonify,
    render_template,
    current_app,
    request
)

from backend.database.data_acess import (
    buscar_todos_clientes
)

clientes_bp = Blueprint("clientes", __name__)

@clientes_bp.route("/clientes", methods=["GET"])
def clientes():
    supabase = current_app.supabase

    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500
        
    lista_clientes = buscar_todos_clientes(supabase) or []
    
    return render_template('clientes.html', clientes=lista_clientes)

@clientes_bp.route("/clientes/buscar")
def buscar_cliente():
    supabase = current_app.supabase

    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500

    nome = request.args.get("nome", "")
    
    consulta = (
        supabase.table("cliente")
        .select("nome, cpf")
        .ilike("nome", f"%{nome}%")
        .execute()
    )

    dados = consulta.data if consulta.data else []
    return jsonify(dados)
