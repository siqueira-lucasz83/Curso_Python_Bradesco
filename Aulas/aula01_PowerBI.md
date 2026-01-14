# Power bi — conceitos básicos

## 1. o que é Power bi

O **Power bi** é uma ferramenta de **business intelligence (bi)** desenvolvida pela microsoft, utilizada para **análise de dados**, **criação de relatórios interativos** e **dashboards**.

Seu principal objetivo é **transformar dados brutos em informações visuais**, facilitando a tomada de decisão em ambientes corporativos e acadêmicos.

---

## 2. para que serve o Power bi

O Power bi é utilizado para:

- análise de grandes volumes de dados  
- criação de dashboards interativos  
- consolidação de dados de múltiplas fontes  
- acompanhamento de indicadores (kpis)  
- apoio à tomada de decisão  
- visualização clara de métricas e resultados  

---

## 3. principais componentes do Power bi

### 3.1 Power bi desktop

Aplicação utilizada para:
- importar dados
- modelar dados
- criar relatórios e dashboards

É a principal ferramenta para desenvolvimento.

---

### 3.2 Power bi service

Versão online (cloud) usada para:
- publicar relatórios
- compartilhar dashboards
- atualizar dados automaticamente

---

### 3.3 Power bi mobile

Aplicativo para acesso aos dashboards via celular ou tablet.

---

## 4. fontes de dados suportadas

O Power bi permite conexão com diversas fontes, como:

- excel  
- csv  
- sql server  
- mysql  
- postgresql  
- oracle  
- sharepoint  
- arquivos txt  
- apis e serviços web  

---

## 5. conceitos básicos de modelagem de dados

### 5.1 tabelas

São estruturas que armazenam os dados importados.

---

### 5.2 relacionamentos

Ligação entre tabelas por meio de:
- chaves primárias
- chaves estrangeiras

Exemplo:
- tabela vendas ligada à tabela clientes pelo id_cliente

---

### 5.3 modelo estrela

Modelo mais comum no Power bi:
- tabela fato (ex.: vendas)
- tabelas dimensão (ex.: clientes, produtos, datas)

---

## 6. principais funcionalidades do Power bi

### 6.1 criação de relatórios

- gráficos de barras  
- gráficos de linhas  
- gráficos de pizza  
- tabelas e matrizes  
- cartões (cards)  
- mapas  

---

### 6.2 filtros

Permitem restringir os dados exibidos:
- filtro por página
- filtro por relatório
- segmentação de dados (slicers)

---

### 6.3 dashboards

Painéis visuais com indicadores principais (kpis).

---

## 7. introdução ao dax (data analysis expressions)

O **dax** é a linguagem usada no Power bi para criar **medidas** e **colunas calculadas**.

### exemplos básicos de funções dax

#### soma
total_vendas = sum(vendas[valor])

#### média
media_vendas = average(vendas[valor])

#### contagem
qtd_vendas = count(vendas[id_venda])

#### contagem distinta
clientes_unicos = distinctcount(vendas[id_cliente])

---

## 8. fluxo básico de uso do Power bi

1. importar dados  
2. tratar dados no power query  
3. criar relacionamentos  
4. criar medidas com dax  
5. montar visualizações  
6. publicar no power bi service  

---

## 9. Power query (tratamento de dados)

O **power query** é usado para:
- limpar dados
- remover colunas desnecessárias
- tratar valores nulos
- alterar tipos de dados
- combinar tabelas

Essas transformações são feitas **antes da análise**.

---

## 10. vantagens do Power bi

- interface intuitiva  
- integração com ferramentas microsoft  
- atualização automática de dados  
- alta capacidade de visualização  
- suporte a grandes volumes de dados  

---

## 11. quando utilizar Power bi

O Power bi é indicado quando:
- há necessidade de análise visual de dados  
- relatórios manuais não são suficientes  
- existe grande volume de informações  
- é preciso compartilhar resultados facilmente  

---

## 12. conclusão

O Power bi é uma ferramenta essencial para análise de dados e business intelligence. Seu uso básico envolve importação, modelagem, criação de medidas e visualização, sendo amplamente adotado em empresas e instituições de ensino.

Dominar seus conceitos fundamentais é o primeiro passo para análises mais avançadas e tomadas de decisão baseadas em dados.
