-- =========================
-- criação do banco de dados
-- =========================

create database if not exists aula;
use aula;

-- =========================
-- criação da tabela
-- =========================

create table if not exists motoristas (
    id int auto_increment primary key,
    nome varchar(100) not null,
    rf varchar(20) not null unique,
    cnh varchar(20) not null unique,
    veiculo varchar(50) not null
);

-- =========================
-- inserção dos dados
-- =========================

insert into motoristas (nome, rf, cnh, veiculo) values
('joão silva', 'rf001', 'cnh123456', 'gol'),
('maria souza', 'rf002', 'cnh654321', 'onix'),
('carlos pereira', 'rf003', 'cnh987654', 'corolla'),
('ana oliveira', 'rf004', 'cnh456789', 'hb20');

-- =========================
-- consulta de dados
-- =========================

select * from motoristas;
