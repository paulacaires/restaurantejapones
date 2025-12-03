from backend.database.queries_relatorio import (
    buscar_cardapios, buscar_itens_cardapio, buscar_funcionarios,
    buscar_consumos, buscar_clientes
)

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

    # Transformar lista → dict
    itens_por_id = {i["id_item"]: i for i in itens_cardapio}
    clientes_por_cpf = {c["cpf"]: c for c in clientes}

    # -------------------------------
    # 2. Calcular custo dos ingredientes
    # -------------------------------
    custo_ingredientes = 0

    for card in cardapios:
        for campo in ["entrada", "main_sushi", "main_ramen", "sobremesa", "bebida"]:
            item_id = card[campo]
            item = itens_por_id[item_id]

            qtd = float(item["estoque_minimo"])
            preco = float(item["custo_unitario"])

            custo_ingredientes += qtd * preco

    # -------------------------------
    # 3. Custo com funcionários
    # -------------------------------
    custo_salarios = sum(float(f["salario"]) for f in funcionarios)

    # -------------------------------
    # 4. Faturamento pelas refeições
    # -------------------------------
    faturamento_total = 0

    for consumo in consumos:
        cpf = consumo["cliente_cpf"]
        cliente = clientes_por_cpf[cpf]

        categoria = cliente["categoria"]

        if categoria == "meia_estudante":
            faturamento_total += VALOR_PAGO_REFEICAO["inteira_estudante"] / 2
        elif categoria == "inteira_estudante":
            faturamento_total += VALOR_PAGO_REFEICAO["inteira_estudante"]
        elif categoria == "visitante_prof":
            faturamento_total += VALOR_PAGO_REFEICAO["visitante_prof"]
        else:
            faturamento_total += 0

    # -------------------------------
    # 5. Lucro
    # -------------------------------
    custo_total = custo_ingredientes + custo_salarios
    lucro = faturamento_total - custo_total

    return {
        "custo_ingredientes": round(custo_ingredientes, 2),
        "custo_salarios": round(custo_salarios, 2),
        "custo_total": round(custo_total, 2),
        "faturamento_total": round(faturamento_total, 2),
        "lucro": round(lucro, 2),
        "num_refeicoes": len(consumos)
    }
