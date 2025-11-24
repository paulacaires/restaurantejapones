from flask import (
    Blueprint,
    render_template,
    current_app
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