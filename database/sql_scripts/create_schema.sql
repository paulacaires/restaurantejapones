-- ======================================
-- Esquema: Restaurante Japonês (PostgreSQL)
-- ======================================

-- Tipos ENUM
CREATE TYPE momento_refeicao AS ENUM ('almoco','janta');

CREATE TYPE cliente_categoria AS ENUM (
  'gratuidade',       -- 0: Gratuidade
  'meia_estudante',   -- 1: Paga metade do valor estudante
  'inteira_estudante',-- 2: Paga o valor inteiro estudante
  'visitante_prof'    -- 3: Visitantes e Professores
);

CREATE TYPE funcionario_funcao AS ENUM (
  'cozinheiro',
  'nutricionista',
  'operador_caixa',
  'auxiliar_cozinha',
  'auxiliar_geral',
  'acougueiro',
  'estoquista'
);

CREATE TYPE cota_social AS ENUM (
  'pcd',        -- Pessoa com Deficiência
  'trans',      -- Pessoas Transgênero/Transexuais/Travestis
  'imigrante',  -- Imigrantes / refugiados
  'sem_teto',   -- Pessoas em situação de rua
  'jovem_aprendiz',
  'nenhuma'     -- quando não pertence às cotas sociais
);

CREATE TYPE estoque_categoria AS ENUM (
  'entrada',
  'main_sushi',
  'main_ramen',
  'sobremesa',
  'bebida'
);

-- Funcionários
CREATE TABLE funcionarios (
  id_funcionario BIGSERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  salario NUMERIC(10, 2) NOT NULL CHECK (salario > 0), -- Coluna de salário adicionada (DECIMAL é sinônimo de NUMERIC no PostgreSQL)
  turno momento_refeicao NOT NULL,
  funcao funcionario_funcao NOT NULL,
  data_ultimo_exame DATE,
  laudo TEXT,
  cota_social cota_social DEFAULT 'nenhuma'
);

-- Tabela de itens do estoque
CREATE TABLE item_cardapio (
  id_item BIGSERIAL PRIMARY KEY,
  nome_item TEXT NOT NULL UNIQUE,
  categoria estoque_categoria NOT NULL,
  custo_unitario NUMERIC(12,4) NOT NULL CHECK (custo_unitario >= 0),
  estoque_minimo NUMERIC(12,3) NOT NULL CHECK (estoque_minimo >= 0),
  funcionario_responsavel BIGINT REFERENCES funcionarios(id_funcionario) ON DELETE SET NULL
);

-- Estoque
CREATE TABLE estoque (
  id_estoque BIGSERIAL PRIMARY KEY,
  id_item BIGINT NOT NULL REFERENCES item_cardapio(id_item) ON DELETE CASCADE,
  quantidade NUMERIC(12,3) NOT NULL CHECK (quantidade >= 0),
  data_validade DATE
);

-- Tabela Cardápio
CREATE TABLE cardapio (
  id_cardapio BIGSERIAL PRIMARY KEY,
  dia DATE NOT NULL,
  momento momento_refeicao NOT NULL,
  entrada BIGINT NOT NULL REFERENCES item_cardapio(id_item),
  main_sushi BIGINT REFERENCES item_cardapio(id_item),
  main_ramen BIGINT REFERENCES item_cardapio(id_item),
  sobremesa BIGINT REFERENCES item_cardapio(id_item),
  bebida BIGINT REFERENCES item_cardapio(id_item),
  UNIQUE (dia, momento)
);

-- Cliente
CREATE TABLE cliente (
  cpf TEXT PRIMARY KEY NOT NULL,
  nome TEXT NOT NULL,
  saldo NUMERIC(10,2) DEFAULT 0.00 CHECK (saldo >= 0),
  categoria cliente_categoria NOT NULL,
  curso TEXT
);

-- Consumo (registro de consumo para um cliente em um cardápio)
CREATE TABLE consumo (
  id_consumo BIGSERIAL PRIMARY KEY,
  cliente_cpf TEXT NOT NULL REFERENCES cliente(cpf) ON DELETE CASCADE,
  cardapio_id BIGINT NOT NULL REFERENCES cardapio(id_cardapio) ON DELETE CASCADE,
  avaliacao SMALLINT CHECK (avaliacao BETWEEN 1 AND 5),
  UNIQUE (cliente_cpf, cardapio_id)
);

-- Mesas
CREATE TABLE mesas (
  numero SMALLINT PRIMARY KEY CHECK (numero BETWEEN 0 AND 20),
  lugares SMALLINT NOT NULL CHECK (lugares > 0)
);

-- Reserva de mesas
CREATE TABLE reserva_mesas (
  id_reserva BIGSERIAL PRIMARY KEY,
  cliente_responsavel_cpf TEXT NOT NULL REFERENCES cliente(cpf) ON DELETE RESTRICT,
  mesa_numero SMALLINT NOT NULL REFERENCES mesas(numero) ON DELETE RESTRICT,
  dia_reserva DATE NOT NULL,
  momento_refeicao momento_refeicao NOT NULL, 

  -- não permitir reservas na mesma mesa no mesmo dia e momento (almoço ou janta)
  UNIQUE (mesa_numero, dia_reserva, momento_refeicao)
);