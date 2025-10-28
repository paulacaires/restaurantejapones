-- ======================================
-- Limpar todo o schema do Restaurante Japonês
-- ======================================

-- Drop das tabelas
DROP TABLE IF EXISTS reserva_mesas CASCADE;
DROP TABLE IF EXISTS consumo CASCADE;
DROP TABLE IF EXISTS cardapio CASCADE;
DROP TABLE IF EXISTS estoque CASCADE;
DROP TABLE IF EXISTS item_cardapio CASCADE;
DROP TABLE IF EXISTS cliente CASCADE;
DROP TABLE IF EXISTS mesas CASCADE;
DROP TABLE IF EXISTS funcionarios CASCADE;

-- Drop dos tipos ENUM
DROP TYPE IF EXISTS momento_refeicao CASCADE;
DROP TYPE IF EXISTS cliente_categoria CASCADE;
DROP TYPE IF EXISTS funcionario_funcao CASCADE;
DROP TYPE IF EXISTS cota_social CASCADE;
DROP TYPE IF EXISTS estoque_categoria CASCADE;
