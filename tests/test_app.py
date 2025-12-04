import sys
import os
import pytest
from unittest.mock import MagicMock, patch
from app import create_app

# --- Configuração do Ambiente de Teste (Fixture) ---
@pytest.fixture
def client():
    """
    Cria uma versão do site para testes com o Supabase simulado
    """
    app = create_app()
    app.config['TESTING'] = True
    
    app.supabase = MagicMock()
    
    with app.test_client() as client:
        client.application.supabase = app.supabase
        yield client


# Teste do Módulo de ESTOQUE
def test_estoque(client):
    """
    Verifica a página de estoque.
    """
    # Dados simulados de um item no estoque
    dados_estoque = [{
        "id_estoque": 1, "quantidade": 5, "data_validade": "2025-12-01",
        "item_cardapio": {
            "id_item": 1, "nome_item": "Salmão", "categoria": "main_sushi",
            "custo_unitario": 40.0, "estoque_minimo": 10,
            "funcionario_responsavel": {"nome": "Responsavel Teste"}
        }
    }]
    
    dados_itens = [{"id_item": 1, "nome_item": "Salmão", "categoria": "main_sushi"}]

    query_mock = client.application.supabase.table.return_value.select.return_value
    query_mock.execute.return_value.data = dados_itens
    
    query_mock.order.return_value.execute.return_value.data = dados_estoque

    response = client.get('/estoque')
    assert response.status_code == 200
    assert b"Salm" in response.data 

# Teste do Módulo de CARDÁPIO
def test_cardapio(client):
    """Verifica a página de cardápio."""
    dados_cardapio = [{
        "dia": "2025-10-05", "momento": "almoco",
        "entrada": {"nome_item": "Sunomono"},
        "main_sushi": {"nome_item": "Sushi"},
        "main_ramen": {"nome_item": "Shoyu Ramen"},
        "sobremesa": {"nome_item": "Mochi"},
        "bebida": {"nome_item": "Chá"}
    }]

    query_mock = client.application.supabase.table.return_value.select.return_value
    query_mock.order.return_value.execute.return_value.data = dados_cardapio

    query_mock.execute.return_value.data = [] 

    response = client.get('/cardapio')
    assert response.status_code == 200
    assert b"Sunomono" in response.data

# Teste do Módulo de FUNCIONÁRIOS
def test_funcionarios(client):
    """Verifica a listagem de funcionários."""
    dados_func = [{
        "id_funcionario": 1, "nome": "Remy Carosella", "salario": 1500.00,
        "turno": "almoco", "funcao": "Cozinheiro", "cota_social": "nenhuma",
        "data_ultimo_exame": "2025-01-01", "laudo": "Apto"
    }]

    client.application.supabase.table.return_value.select.return_value.execute.return_value.data = dados_func

    response = client.get('/funcionarios')
    assert response.status_code == 200
    assert b"Remy Carosella" in response.data


# Teste do Módulo de CLIENTES
def test_clientes(client):
    """Verifica a listagem de clientes."""
    dados_clientes = [{
        "cpf": "123.123.123-00", "nome": "Shaun House", "saldo": 100.00,
        "categoria": "inteira_estudante", "curso": "Medicina"
    }]

    client.application.supabase.table.return_value.select.return_value.execute.return_value.data = dados_clientes

    response = client.get('/clientes')
    assert response.status_code == 200
    assert b"Shaun House" in response.data

# Teste do Módulo de RESERVA
def test_reserva(client):
    """
    Verifica a página de reservas.
    """
    dados_reserva = [{
        "id_reserva": 10, "dia_reserva": "2025-12-25", "momento_refeicao": "janta",
        "mesa_numero": 9,
        "cliente": {"nome": "Jose Bezerra"},
        "mesas": {"lugares": 4}
    }]

    query_mock = client.application.supabase.table.return_value.select.return_value
    query_mock.execute.return_value.data = [{"cpf": "1", "nome": "Cliente"}]
    
    query_mock.order.return_value.execute.return_value.data = [{"numero": 1, "lugares": 2}]
    query_mock.order.return_value.order.return_value.execute.return_value.data = dados_reserva

    response = client.get('/reservas')
    assert response.status_code == 200
    assert b"Jose Bezerra" in response.data

# Teste do Módulo de RELATÓRIO 
@patch('routes.relatorio_routes.calcula_faturamento')
def test_relatorio(mock_calcula, client):
    """Verifica a geração do PDF de relatório."""
    mock_calcula.return_value = {
        "Novembro/2025": {
            "faturamento_total": 5000.00,
            "custo_total": 2000.00,
            "lucro": 3000.00,
            "num_refeicoes": 150
        }
    }

    response = client.get('/gerar-pdf')
    
    assert response.status_code == 200
    assert response.content_type == 'application/pdf'


# Teste do Módulo de CONSUMO
def test_consumo(client):
    """Verifica a página de histórico de consumo."""
    dados_consumo = [{
        "id_consumo": 1, 
        "cliente_cpf": "000.000.000-00",
        "avaliacao": 5,
        "cardapio": {"dia": "2025-01-01", "momento": "almoco"},
        "cliente": {"nome": "Timmy Bouvier"}
    }]
    
    client.application.supabase.table.return_value.select.return_value.execute.return_value.data = dados_consumo
    response = client.get('/consumo')

    assert response.status_code == 200
    assert b"Consumo" in response.data