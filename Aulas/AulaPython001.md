# Aula Básica: Tipos de Variáveis e Tipos de Dados em Python

## 1. O que é uma variável?

Uma **variável** é um nome que aponta para um valor armazenado na memória do computador. Em Python, você não precisa declarar o tipo da variável explicitamente — o próprio Python identifica automaticamente o tipo com base no valor atribuído.

### Exemplo:
```python
x = 10
nome = "Lucas"
altura = 1.75
```

---

## 2. Tipos de Dados Principais em Python

### 2.1 int (Inteiro)
Usado para números inteiros, positivos ou negativos.

```python
idade = 20
saldo = -150
```

---

### 2.2 float (Ponto flutuante / Decimal)
Usado para números com casas decimais.

```python
preco = 19.99
temperatura = -3.5
```

---

### 2.3 str (String / Texto)
Usado para armazenar textos.

```python
nome = "Ana"
mensagem = "Olá, mundo!"
```

Você pode usar aspas simples (`'`) ou duplas (`"`).

---

### 2.4 bool (Booleano)
Usado para representar valores lógicos: **True** ou **False**.

```python
ligado = True
aprovado = False
```

---

### 2.5 list (Lista)
Usada para armazenar vários valores em uma única variável, em ordem.

```python
numeros = [1, 2, 3, 4]
nomes = ["Ana", "João", "Carlos"]
```

---

### 2.6 tuple (Tupla)
Parecida com lista, porém **imutável** (não pode ser alterada).

```python
coordenadas = (10, 20)
cores = ("vermelho", "azul", "verde")
```

---

### 2.7 dict (Dicionário)
Armazena dados no formato **chave: valor**.

```python
aluno = {
    "nome": "Lucas",
    "idade": 21,
    "curso": "Engenharia"
}
```

---

### 2.8 set (Conjunto)
Armazena valores **únicos** e sem ordem.

```python
numeros = {1, 2, 3, 3, 4}
print(numeros)  # Saída: {1, 2, 3, 4}
```

---

## 3. Descobrindo o tipo de uma variável

Você pode usar a função `type()`:

```python
x = 10
print(type(x))  # <class 'int'>
```

---

## 4. Mudando o tipo de um dado (Conversão / Casting)

```python
x = "10"
y = int(x)     # Converte string para inteiro
z = float(x)   # Converte string para float
w = str(20)    # Converte inteiro para string
```

---

## 5. Exercícios básicos

1. Crie uma variável com seu nome e outra com sua idade.
2. Crie uma lista com 5 números.
3. Crie um dicionário com dados de um produto (nome, preço, estoque).
4. Use `type()` para imprimir o tipo de cada variável.

---

## 6. Resumo

| Tipo  | Uso principal                 |
|-------|------------------------------|
| int   | Números inteiros              |
| float | Números decimais              |
| str   | Texto                         |
| bool  | Verdadeiro ou falso           |
| list  | Coleção mutável de valores    |
| tuple | Coleção imutável de valores   |
| dict  | Estrutura chave-valor         |
| set   | Conjunto de valores únicos    |


Esa base é essencial para qualquer programa em Python e será usada constantemente em projetos maiores.
-->
