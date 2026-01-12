create database aula
use aula;

create table motoristas (
    id int auto_increment primary key,
    nome varchar(100) not null,
    rf varchar(20) not null,
    cnh varchar(20) not null,
    veiculo varchar(50) not null
);

insert into motoristas (nome, rf, cnh, veiculo) values
('joão silva', 'rf001', 'cnh123456', 'gol'),
('maria souza', 'rf002', 'cnh654321', 'onix'),
('carlos pereira', 'rf003', 'cnh987654', 'corolla'),
('ana oliveira', 'rf004', 'cnh456789', 'hb20');
