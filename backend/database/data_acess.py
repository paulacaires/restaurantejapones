from supabase import Client

# Nome da View (tabela virtual) que vamos consultar
CLIENTES_VIEW = "vw_clientes_api" 
CLIENTES_TABELA = "cliente"

def buscar_todos_clientes(supabase_client: Client):
    """
    Função que busca todos os clientes usando a View segura.
    """
    try:
        # Consulta a VIEW criada no PostgreSQL
        response = supabase_client.table(CLIENTES_VIEW).select("*").execute()
        
        # Retorna a lista de dados
        return response.data
    except Exception as e:
        print(f"Erro ao buscar clientes: {e}")
        return None

def adicionar_novo_cliente(supabase_client: Client, dados_cliente: dict):
    """
    Função que insere um novo cliente.
    (Note que inserimos na TABELA original, não na View)
    """
    try:
        response = (
            supabase_client.table(CLIENTES_TABELA)
            .insert(dados_cliente)
            .execute()
        )
        # Retorna os dados do novo cliente inserido (ou o que o Supabase retornar)
        return response.data
    except Exception as e:
        print(f"Erro ao adicionar cliente: {e}")
        return None