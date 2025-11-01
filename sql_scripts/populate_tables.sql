-- Inserindo funcionários
INSERT INTO funcionarios (nome, salario, turno, funcao, data_ultimo_exame, laudo, cota_social) VALUES
('Carlos Sato', 3500.00, 'almoco', 'cozinheiro', '2025-09-01', 'Apto', 'nenhuma'),
('Mariana Tanaka', 4200.00, 'janta', 'nutricionista', '2025-08-15', 'Apto', 'nenhuma'),
('João Silva', 2500.00, 'almoco', 'operador_caixa', '2025-10-01', 'Apto', 'pcd'),
('Ana Oliveira', 1800.00, 'janta', 'auxiliar_cozinha', '2025-09-20', 'Apto', 'jovem_aprendiz'),
('Roberto Costa', 2000.00, 'almoco', 'estoquista', '2025-09-30', 'Apto', 'nenhuma');

-- Inserindo clientes
INSERT INTO cliente (cpf, nome, saldo, categoria, curso) VALUES
('123.456.789-00', 'Lucas Pereira', 10.00, 'meia_estudante', 'Engenharia'),
('987.654.321-11', 'Fernanda Souza', 0.00, 'inteira_estudante', 'Medicina'),
('111.222.333-44', 'Professor Tiago', 0.00, 'visitante_prof', NULL),
('555.666.777-88', 'Maria Fernandes', 0.00, 'gratuidade', NULL),
('999.888.777-66', 'João da Silva', 20.00, 'inteira_estudante', 'Administração');

--Inserindo itens do cardapio
INSERT INTO item_cardapio (nome_item, categoria, custo_unitario, estoque_minimo, funcionario_responsavel) VALUES
--Entradas
('Sunomono', 'entrada', 5.00, 20, 5),
('Gyoza', 'entrada', 8.00, 30, 5),
('Edamame', 'entrada', 7.00, 25, 5),
--Main sushi
('Combinado Sushi (10 pçs)', 'main_sushi', 15.00, 25, 5),
('Temaki Salmão', 'main_sushi', 12.00, 30, 5),
-- Main Ramen
('Yakisoba', 'main_ramen', 14.00, 20, 5),
('Ramen', 'main_ramen', 16.00, 20, 5),
-- Sobremesa
('Mochi', 'sobremesa', 6.00, 40, 5),
('Sorvete de Chá Verde', 'sobremesa', 5.00, 30, 5),
('Dorayaki', 'sobremesa', 4.50, 30, 5)
-- Bebidas
('Chá Verde (Copo 300ml)', 'bebida', 3.00, 50, 5),
('Refrigerante (Lata)', 'bebida', 4.00, 50, 5),
('Suco Natural (Laranja 300ml)', 'bebida', 5.00, 40, 5);


--Inserindo cardapios de diferentes dias
INSERT INTO cardapio (dia, momento, entrada, main_sushi, main_ramen, sobremesa, bebida) VALUES
('2025-12-02', 'almoco', 2, 4, 7, 9, 11),
('2025-12-02', 'janta', 1, 5, 7, 8, 12),
('2025-12-03', 'almoco', 3, 4, 6, 10, 13),  
('2025-12-03', 'janta', 1, 5, 6, 8, 12),
('2025-12-04', 'almoco', 1, 5, 7, 8, 13), 
('2025-12-04', 'janta', 2, 4, 6, 10, 11),
('2025-12-05', 'almoco', 3, 4, 6, 10, 12), 
('2025-12-05', 'janta', 3, 5, 7, 9, 13);  