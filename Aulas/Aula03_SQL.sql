-- =========================
-- banco de dados
-- =========================

create database if not exists aula;
use aula;

-- =========================
-- tabela de veiculos
-- =========================

create table if not exists veiculos (
    id int auto_increment primary key,
    modelo varchar(50) not null,
    placa varchar(10) not null unique
);

-- =========================
-- tabela de motoristas
-- =========================

create table if not exists motoristas (
    id int auto_increment primary key,
    nome varchar(100) not null,
    cnh varchar(20) not null unique,
    veiculo_id int,
    primary key (id),
    foreign key (veiculo_id) references veiculos(id)
);

-- =========================
-- insercao de dados em veiculos
-- =========================

insert into veiculos (modelo, placa) values
('gol', 'abc1a23'),
('onix', 'def4b56'),
('corolla', 'ghi7c89'),
('hb20', 'jkl0d12');

-- =========================
-- insercao de dados em motoristas
-- =========================

insert into motoristas (nome, cnh, veiculo_id) values
('joão silva', 'cnh123', 1),
('maria souza', 'cnh456', 2),
('carlos pereira', 'cnh789', 3),
('ana oliveira', 'cnh321', null);

-- =========================
-- inner join
-- retorna apenas registros com relacao
-- =========================

select 
    m.nome,
    m.cnh,
    v.modelo,
    v.placa
from motoristas m
inner join veiculos v
on m.veiculo_id = v.id;

-- =========================
-- left join
-- retorna todos os motoristas
-- mesmo sem veiculo
-- =========================

select 
    m.nome,
    v.modelo
from motoristas m
left join veiculos v
on m.veiculo_id = v.id;

-- =========================
-- right join
-- retorna todos os veiculos
-- mesmo sem motorista
-- =========================

select 
    m.nome,
    v.modelo
from motoristas m
right join veiculos v
on m.veiculo_id = v.id;

-- =========================
-- funcoes agregadas
-- =========================

-- quantidade total de motoristas
select count(*) as total_motoristas
from motoristas;

-- quantidade de motoristas com veiculo
select count(veiculo_id) as motoristas_com_veiculo
from motoristas;

-- =========================
-- group by
-- =========================

-- quantidade de motoristas por modelo de veiculo
select 
    v.modelo,
    count(m.id) as total_motoristas
from veiculos v
left join motoristas m
on m.veiculo_id = v.id
group by v.modelo;

-- =========================
-- funcoes agregadas com group by
-- =========================

-- menor e maior id de motorista por veiculo
select 
    v.modelo,
    min(m.id) as menor_id,
    max(m.id) as maior_id
from veiculos v
left join motoristas m
on m.veiculo_id = v.id
group by v.modelo;

-- =========================
-- indices
-- =========================

-- indice para melhorar buscas por nome
create index idx_motoristas_nome
on motoristas(nome);

-- indice para melhorar joins
create index idx_motoristas_veiculo
on motoristas(veiculo_id);
