# Aula Básica: Strings em Python

## 1. O que é uma string?

Uma **string** é um tipo de dado usado para armazenar texto. Em Python, strings podem ser criadas usando aspas simples (`'`), aspas duplas (`"`) ou aspas triplas (`'''` ou `"""`).

### Exemplos:
```python
nome = "Lucas"
frase = 'Olá, mundo!'
texto_longo = """Isso é um texto
com várias linhas."""
```

---

## 2. Strings de uma única linha

São as mais comuns, usadas para textos curtos.

```python
mensagem = "Bem-vindo ao Python!"
```

---

## 3. Strings de múltiplas linhas

Usadas quando o texto ocupa mais de uma linha. São criadas com aspas triplas.

```python
texto = """
Este é um texto
com várias linhas
em Python.
"""

print(texto)
```

---

## 4. Strings interpoláveis (formatação de strings)

Interpolação é a técnica de inserir variáveis dentro de uma string.

---

### 4.1 Usando f-strings (recomendado)

```python
nome = "Lucas"
idade = 21

mensagem = f"Meu nome é {nome} e tenho {idade} anos."
print(mensagem)
```

---

### 4.2 Usando `.format()`

```python
nome = "Ana"
idade = 25

mensagem = "Meu nome é {} e tenho {} anos.".format(nome, idade)
print(mensagem)
```

Com posições:
```python
mensagem = "{1} tem {0} anos.".format(30, "Carlos")
print(mensagem)
```

---

### 4.3 Usando `%` (forma antiga)

```python
nome = "João"
idade = 40

mensagem = "Meu nome é %s e tenho %d anos." % (nome, idade)
print(mensagem)
```

---

## 5. Concatenação de strings

Concatenação é juntar duas ou mais strings.

```python
nome = "Lucas"
sobrenome = "Siqueira"
nome_completo = nome + " " + sobrenome
print(nome_completo)
```

---

## 6. Repetição de strings

```python
print("Python! " * 3)
```

---

## 7. Acesso a caracteres (indexação)

```python
palavra = "Python"
print(palavra[0])   # P
print(palavra[1])   # y
print(palavra[-1])  # n
```

---

## 8. Fatiamento (slicing)

```python
texto = "Programação"
print(texto[0:5])   # Progr
print(texto[5:])    # amação
print(texto[:5])    # Progr
print(texto[::2])   # Pormço
```

---

## 9. Principais métodos de strings

```python
texto = "  Python é incrível  "

print(texto.upper())      # Maiúsculas
print(texto.lower())      # Minúsculas
print(texto.strip())      # Remove espaços
print(texto.replace("Python", "Java"))
print(texto.split())      # Divide em lista
print(len(texto))         # Tamanho da string
```

---

## 10. Exercícios Práticos

1. Crie uma string com seu nome completo.
2. Crie uma string de múltiplas linhas com uma pequena biografia.
3. Use uma f-string para mostrar seu nome e idade.
4. Concatene duas strings.
5. Acesse o primeiro e o último caractere de uma palavra.

---

## 11. Resumo

| Conceito                  | Exemplo                           |
|---------------------------|-----------------------------------|
| String simples            | "Olá"                            |
| String múltiplas linhas   | """Texto longo"""              |
| Interpolação (f-string)   | f"Nome: {nome}"                  |
| Concatenação              | "Olá" + " Mundo"               |
| Repetição                 | "Oi" * 3                         |
| Indexação                 | texto[0]                          |
| Fatiamento                | texto[1:4]                        |

---

Strings são fundamentais em Python e aparecem em praticamente todos os programas, desde mensagens simples até sistemas completos.
