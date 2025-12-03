from backend.database.queries_relatorio import (
    buscar_cardapios, buscar_itens_cardapio, buscar_funcionarios,
    buscar_consumos, buscar_clientes
)
from datetime import datetime

VALOR_PAGO_REFEICAO = {
    "inteira_estudante": 9.50,
    "visitante_prof": 17.50,
}

CATEGORIA_CLIENTE = {
    "meia_estudante": "Meia — Estudante",
    "inteira_estudante": "Inteira — Estudante",
    "visitante_prof": "Visitante / Professor",
    "gratuidade": "Gratuidade"
}

def calcula_faturamento(supabase):

    # -------------------------------
    # 1. Buscar dados do banco
    # -------------------------------
    cardapios       = buscar_cardapios(supabase)
    itens_cardapio  = buscar_itens_cardapio(supabase)
    funcionarios    = buscar_funcionarios(supabase)
    consumos        = buscar_consumos(supabase)
    clientes        = buscar_clientes(supabase)

    # Transformar listas → dict para lookup rápido
    itens_por_id = {i["id_item"]: i for i in itens_cardapio}
    clientes_por_cpf = {c["cpf"]: c for c in clientes}

    # 📌 Agora cardápio por ID → muito importante para ligar consumo à data
    cardapio_por_id = {c["id_cardapio"]: c for c in cardapios}

    # -------------------------------
    # 2. Custos fixos independentes do mês
    # -------------------------------
    custo_salarios = sum(float(f["salario"]) for f in funcionarios)

    # Custo de ingredientes (fixo no seu modelo)
    custo_ingredientes = 0
    for card in cardapios:
        for campo in ["entrada", "main_sushi", "main_ramen", "sobremesa", "bebida"]:
            item_id = card[campo]
            item = itens_por_id[item_id]
            custo_ingredientes += float(item["estoque_minimo"]) * float(item["custo_unitario"])

    # -------------------------------
    # 3. AGRUPAR POR MÊS
    # -------------------------------
    dados_mensais = {}  # Exemplo: {"2025-12": {...}}

    for consumo in consumos:

        # 🔍 Achar o cardápio correspondente
        card_id = consumo["cardapio_id"]
        card = cardapio_por_id.get(card_id)

        if not card:
            print(f"[AVISO] cardapio_id {card_id} não encontrado!")
            continue

        # Data do cardápio
        dia_str = card["dia"]  # vem como "2025-12-05"
        data = datetime.strptime(dia_str, "%Y-%m-%d")

        # chave do mês: "2025-12"
        mes = f"{data.year}-{data.month:02d}"

        # Criar entrada se não existir
        if mes not in dados_mensais:
            dados_mensais[mes] = {
                "faturamento": 0.0,
                "num_refeicoes": 0
            }

        # Categorizar cliente
        cpf = consumo["cliente_cpf"]
        cliente = clientes_por_cpf[cpf]
        categoria = cliente["categoria"]

        # Faturamento por categoria
        if categoria == "meia_estudante":
            dados_mensais[mes]["faturamento"] += VALOR_PAGO_REFEICAO["inteira_estudante"] / 2
        elif categoria == "inteira_estudante":
            dados_mensais[mes]["faturamento"] += VALOR_PAGO_REFEICAO["inteira_estudante"]
        elif categoria == "visitante_prof":
            dados_mensais[mes]["faturamento"] += VALOR_PAGO_REFEICAO["visitante_prof"]

        dados_mensais[mes]["num_refeicoes"] += 1

    # -------------------------------
    # 4. Calcular lucro e consolidar resultados
    # -------------------------------
    resultado = {}

    for mes, dados in dados_mensais.items():

        faturamento = dados["faturamento"]
        num_refeicoes = dados["num_refeicoes"]

        custo_total = custo_ingredientes + custo_salarios
        lucro = faturamento - custo_total

        resultado[mes] = {
            "custo_ingredientes": round(custo_ingredientes, 2),
            "custo_salarios": round(custo_salarios, 2),
            "custo_total": round(custo_total, 2),
            "faturamento_total": round(faturamento, 2),
            "lucro": round(lucro, 2),
            "num_refeicoes": num_refeicoes
        }

    return resultado