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
