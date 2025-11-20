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
    buscar_todos_funcionarios
)

# Nome das tabelas no Supabase
funcionarios_TABELA = "funcionarios"

# Criação do blueprint
funcionarios_bp = Blueprint("funcionarios", __name__)

@funcionarios_bp.route("/funcionarios", methods=["GET"])
def funcionarios():
    supabase = current_app.supabase

    if not supabase:
        return "Erro: Conexão com o banco de dados não estabelecida.", 500
        
    lista_funcionarios = buscar_todos_funcionarios(supabase) or []
    
    return render_template('funcionarios.html', funcionarios=lista_funcionarios)
