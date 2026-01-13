-- =========================
-- update (atualização)
-- =========================

-- atualizar veículo usando a chave primária (safe update)
update motoristas
set veiculo = 'polo'
where id = 4;

-- atualizar mais de uma coluna
update motoristas
set nome = 'maria silva',
    veiculo = 'civic'
where id = 2;

-- =========================
-- delete (exclusão de dados)
-- =========================

-- excluir um registro específico
delete from motoristas
where id = 3;

-- conferir após exclusão
select * from motoristas;

-- =========================
-- alter table (alteração da estrutura)
-- =========================

-- adicionar nova coluna
alter table motoristas
add column telefone varchar(20);

-- alterar tamanho da coluna
alter table motoristas
modify column veiculo varchar(100);

-- remover coluna
alter table motoristas
drop column telefone;

-- =========================
-- truncate (excluir todos os dados)
-- =========================

 truncate table motoristas;

-- =========================
-- drop table (excluir tabela inteira)
-- =========================

 drop table motoristas;
