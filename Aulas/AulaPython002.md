# Aula Básica: Operadores em Python

## 1. O que são operadores?

**Operadores** são símbolos utilizados para realizar operações entre valores e variáveis, como cálculos matemáticos, comparações, atribuições e avaliações lógicas.

---

## 2. Operadores Aritméticos

Usados para realizar operações matemáticas.

| Operador | Descrição       | Exemplo      |
|----------|-----------------|--------------|
| +        | Adição          | 5 + 3 = 8    |
| -        | Subtração       | 5 - 3 = 2    |
| *        | Multiplicação   | 5 * 3 = 15   |
| /        | Divisão         | 10 / 2 = 5.0 |
| //       | Divisão inteira | 10 // 3 = 3  |
| %        | Módulo (resto)  | 10 % 3 = 1   |
| **       | Exponenciação   | 2 ** 3 = 8   |

### Exemplos:
```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 3. Operadores de Comparação

Usados para comparar dois valores. O resultado é sempre um valor booleano (`True` ou `False`).

| Operador | Descrição          | Exemplo     |
|----------|--------------------|-------------|
| ==       | Igual a            | 5 == 5      |
| !=       | Diferente de       | 5 != 3      |
| >        | Maior que          | 5 > 3       |
| <        | Menor que          | 5 < 3       |
| >=       | Maior ou igual a   | 5 >= 5      |
| <=       | Menor ou igual a   | 3 <= 5      |

### Exemplos:
```python
x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

---

## 4. Operadores de Atribuição

Usados para atribuir valores a variáveis, muitas vezes combinados com operadores aritméticos.

| Operador | Exemplo  | Equivalente a |
|----------|----------|----------------|
| =        | x = 5    | x = 5          |
| +=       | x += 2   | x = x + 2      |
| -=       | x -= 2   | x = x - 2      |
| *=       | x *= 2   | x = x * 2      |
| /=       | x /= 2   | x = x / 2      |
| //=      | x //= 2 | x = x // 2     |
| %=       | x %= 2  | x = x % 2      |
| **=      | x **= 2 | x = x ** 2     |

### Exemplos:
```python
x = 10
x += 5
print(x)  # 15

x *= 2
print(x)  # 30

x -= 10
print(x)  # 20
```

---

## 5. Operadores Lógicos

Usados para combinar expressões booleanas.

| Operador | Descrição                  | Exemplo                |
|----------|----------------------------|------------------------|
| and      | Retorna True se ambos forem True | True and False = False |
| or       | Retorna True se pelo menos um for True | True or False = True |
| not      | Inverte o valor lógico     | not True = False       |

### Exemplos:
```python
a = 10
b = 5

print(a > 5 and b < 10)
print(a > 5 or b > 10)
print(not (a == b))
```

---

## 6. Operadores de Identidade

Usados para verificar se duas variáveis **apontam para o mesmo objeto na memória**, e não apenas se têm o mesmo valor.

| Operador | Descrição                     | Exemplo        |
|----------|--------------------------------|----------------|
| is       | Retorna True se forem o mesmo objeto | a is b        |
| is not   | Retorna True se NÃO forem o mesmo objeto | a is not b |

### Exemplos:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a == c)      # True (valores iguais, objetos diferentes)
```

---

## 7. Exercícios Práticos

1. Crie duas variáveis numéricas e realize todas as operações aritméticas entre elas.
2. Compare dois números diferentes usando todos os operadores de comparação.
3. Crie uma variável e utilize pelo menos três operadores de atribuição.
4. Crie duas condições booleanas e combine-as usando `and`, `or` e `not`.
5. Teste a diferença entre `==` e `is` usando listas.

---

## 8. Resumo

| Categoria        | Operadores principais              |
|------------------|------------------------------------|
| Aritméticos      | +, -, *, /, //, %, **               |
| Comparação       | ==, !=, >, <, >=, <=                |
| Atribuição       | =, +=, -=, *=, /=, //=, %=, **=     |
| Lógicos          | and, or, not                        |
| Identidade       | is, is not                          |

---

Esses operadores são fundamentais para qualquer lógica de programação em Python e serão usados constantemente em estruturas como `if`, `while`, `for` e funções.
