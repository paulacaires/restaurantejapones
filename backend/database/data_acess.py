from supabase import Client

# Nome da View (tabela virtual) que vamos consultar
CLIENTES_VIEW = "vw_clientes_api" 
CLIENTES_TABELA = "cliente"
FUNCIONARIOS_TABELA = "funcionarios"
CARDAPIO_TABELA = "cardapio"
ITEM_CARDAPIO_TABELA = "item_cardapio"
ESTOQUE_TABELA = "estoque"
CONSUMO_TABELA = "consumo"
RESERVAS_TABELA = "reservas"


CATEGORIA_CLIENTE = {
    "meia_estudante": "Meia — Estudante",
    "inteira_estudante": "Inteira — Estudante",
    "visitante_prof": "Visitante / Professor",
    "gratuidade": "Gratuidade"
}

def buscar_todos_clientes(supabase_client: Client):
    """
    Função que busca todos os clientes usando a View segura.
    """
    try:
        response = supabase_client.table(CLIENTES_TABELA).select("*").execute()

        dados = response.data  # lista de dicionários

        # Adiciona campos normalizados
        for cliente in dados:
            cliente["categoria"] = CATEGORIA_CLIENTE.get(
                cliente.get("categoria"),
                cliente.get("categoria")
            )

        return dados

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
    
def buscar_itens_cardapio(supabase_client: Client):
    """
    Função que busca todos os itens do cardápio (recuperando o id_item e o nome).
    Lembrando que itens do cardápio é diferente de cardápio.
    """
    try:
        select_query = (
            "id_item, nome_item, categoria",
        )
        
        response = (
            supabase_client.table(ITEM_CARDAPIO_TABELA)
            .select(select_query)
            .execute()
        )

        return response.data
        
    except Exception as e:
        print(f"Erro ao listar os itens do cardápio (lembrando que é diferente de cardápio): {e}")
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
            "item_cardapio("
            "   id_item, nome_item, categoria, custo_unitario, estoque_minimo,"
            "   funcionario_responsavel(nome)"
            ")"
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

def verificar_baixo_estoque(estoque):
    itens_alerta = []
    for item in estoque:
        qtd_atual = item["quantidade"]
        qtd_min = item["item_cardapio"]["estoque_minimo"]

        if qtd_min is not None and qtd_atual < qtd_min:
            itens_alerta.append(item)

    return itens_alerta

def buscar_clientes_por_nome(supabase_client: Client, nome: str):
    try:
        # ILIKE (%) para busca parcial
        response = (
            supabase_client
            .table(CLIENTES_TABELA)
            .select("*")
            .ilike("nome", f"%{nome}%")
            .execute()
        )
        return response.data
    except Exception as e:
        print(f"Erro ao buscar clientes: {e}")
        return []

def buscar_cardapio(supabase_client: Client, dia, momento):
    try:
        response = (
            supabase_client.table(CARDAPIO_TABELA)
            .select("*")
            .eq("dia", dia)
            .eq("momento", momento)
            .maybe_single()
            .execute()
        )
        return response.data
    except Exception as e:
        print("Erro ao buscar cardápio:", e)
        return None

def buscar_todos_consumos(supabase_client: Client):
    """
    Função que busca todos os consumos realizados no Restaurante Japonês.
    """
    try:
        # Consulta a TABELA 'consumo'
        response = supabase_client.table(CONSUMO_TABELA).select("*").execute()
        return response.data
    except Exception as e:
        print(f"Erro ao buscar os consumos: {e}")
        return None

def buscar_todas_reservas(supabase):
    """
    Busca todas as reservas ordenando por dia e turno
    """
    try:
        response = (
            supabase.table("reserva_mesas")
            .select("*, cliente(nome), mesas(lugares)")
            .order("dia_reserva", desc=True)
            .order("momento_refeicao")
            .execute()
        )
        return response.data
    except Exception as e:
        print(f"Erro ao buscar reservas: {e}")
        return []

def buscar_todas_mesas(supabase):
    """
    Busca todas as mesas para preencher o formulário.
    """
    try:
        response = supabase.table("mesas").select("*").order("numero").execute()
        return response.data
    except Exception as e:
        print(f"Erro ao buscar mesas: {e}")
        return []

def criar_reserva(supabase, dados_reserva):
    """
    Insere uma nova reserva no banco.
    """
    try:
        response = supabase.table("reserva_mesas").insert(dados_reserva).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao criar reserva: {e}")
        return None