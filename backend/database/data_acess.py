from supabase import Client

# Nome da View (tabela virtual) que vamos consultar
CLIENTES_VIEW = "vw_clientes_api" 
CLIENTES_TABELA = "cliente"
FUNCIONARIOS_TABELA = "funcionarios"
CARDAPIO_TABELA = "cardapio"
ESTOQUE_TABELA = "estoque"

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
   
def buscar_todos_funcionarios(supabase_client: Client):
    """
    Função que busca todos os funcionários (implementação estática).
    """
    try:
        # Consulta a TABELA 'funcionarios'
        response = supabase_client.table(FUNCIONARIOS_TABELA).select("*").execute()
        return response.data
    except Exception as e:
        print(f"Erro ao buscar funcionários: {e}")
        return None
    
def buscar_todos_cardapios(supabase_client: Client):
    """
    Função que busca todos os cardápios .
    
    Esta consulta usa a sintaxe do Supabase para buscar dados de
    tabelas relacionadas, definidas no create_schema.sql.
    """
    try:
        # A consulta seleciona o dia, momento e o nome dos itens
        # de cada categoria (entrada, main_sushi, etc.)
        select_query = (
            "dia, momento, "
            "entrada(nome_item), "
            "main_sushi(nome_item), "
            "main_ramen(nome_item), "
            "sobremesa(nome_item), "
            "bebida(nome_item)"
        )
        
        response = (
            supabase_client.table(CARDAPIO_TABELA)
            .select(select_query)
            .order("dia", desc=True)
            .execute()
        )
        
        return response.data
        
    except Exception as e:
        print(f"Erro ao buscar cardápio: {e}")
        return None
    
def buscar_todos_itens_estoque(supabase_client: Client):
    """
    Função que busca todos os itens do estoque com informações do cardápio.

    Faz uma junção entre as tabelas 'estoque' e 'item_cardapio' usando
    o relacionamento definido no Supabase (FK id_item).
    """
    try:
        select_query = (
            "id_estoque, quantidade, data_validade, "
            "item_cardapio(id_item, nome_item, categoria, custo_unitario, funcionario_responsavel)"
        )
        
        response = (
            supabase_client.table(ESTOQUE_TABELA)
            .select(select_query)
            .order("id_estoque", desc=False)
            .execute()
        )
        
        return response.data

    except Exception as e:
        print(f"Erro ao buscar itens do estoque: {e}")
        return None

def buscar_id_item_por_nome(supabase_client, nome_item: str):
    """
    Retorna o ID do item no cardápio com base no nome.
    Se não encontrar, retorna None.
    """
    try:
        response = (
            supabase_client
            .table("item_cardapio")
            .select("id_item")
            .eq("nome_item", nome_item)
            .limit(1)
            .execute()
        )

        if response.data:
            return response.data[0]["id_item"]
        return None

    except Exception as e:
        print(f"Erro ao buscar id do item '{nome_item}': {e}")
        return None

