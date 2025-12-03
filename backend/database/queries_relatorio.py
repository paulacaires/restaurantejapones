from supabase import Client

# Nomes das tabelas
CARDAPIO_TABELA = "cardapio"
ITEM_CARDAPIO_TABELA = "item_cardapio"
FUNCIONARIOS_TABELA = "funcionarios"
CONSUMO_TABELA = "consumo"
CLIENTES_TABELA = "cliente"


# --------------------------
# CARDÁPIO
# --------------------------
def buscar_cardapios(supabase: Client):
    resp = supabase.table(CARDAPIO_TABELA).select("*").execute()
    return resp.data or []


# --------------------------
# ITENS DO CARDÁPIO
# --------------------------
def buscar_itens_cardapio(supabase: Client):
    resp = supabase.table(ITEM_CARDAPIO_TABELA).select("*").execute()
    return resp.data or []


# --------------------------
# FUNCIONÁRIOS
# --------------------------
def buscar_funcionarios(supabase: Client):
    resp = supabase.table(FUNCIONARIOS_TABELA).select("*").execute()
    return resp.data or []


# --------------------------
# CONSUMOS (refeições vendidas)
# --------------------------
def buscar_consumos(supabase: Client):
    resp = supabase.table(CONSUMO_TABELA).select("*").execute()
    return resp.data or []


# --------------------------
# CLIENTES
# --------------------------
def buscar_clientes(supabase: Client):
    resp = supabase.table(CLIENTES_TABELA).select("*").execute()
    return resp.data or []
