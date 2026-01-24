# Aula Básica: Estruturas Condicionais e de Repetição em Python

## 1. O que são estruturas de controle?

As **estruturas de controle** permitem que um programa tome decisões e repita ações com base em condições. Elas são fundamentais para criar programas dinâmicos e inteligentes.

---

## 2. Estruturas Condicionais

As estruturas condicionais permitem que o programa execute diferentes blocos de código dependendo de uma condição.

---

### 2.1 if

Executa um bloco de código se a condição for verdadeira.

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

---

### 2.2 if...else

Executa um bloco se a condição for verdadeira e outro se for falsa.

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

---

### 2.3 if...elif...else

Permite testar múltiplas condições.

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")
```

---

### 2.4 Condicionais Aninhadas

Você pode colocar um `if` dentro de outro.

```python
idade = 20
carteira = True

if idade >= 18:
    if carteira:
        print("Pode dirigir")
    else:
        print("Não possui carteira")
else:
    print("Menor de idade")
```

---

### 2.5 Operador Ternário (Condicional em uma linha)

```python
idade = 18
mensagem = "Maior" if idade >= 18 else "Menor"
print(mensagem)
```

---

## 3. Estruturas de Repetição (Laços / Loops)

As estruturas de repetição permitem executar um bloco de código várias vezes.

---

### 3.1 while

Executa enquanto a condição for verdadeira.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

---

### 3.2 for

Usado para percorrer sequências como listas, tuplas, strings ou intervalos.

```python
for i in range(1, 6):
    print(i)
```

Outro exemplo:
```python
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)
```

---

### 3.3 break

Interrompe o loop imediatamente.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

---

### 3.4 continue

Pula a iteração atual e vai para a próxima.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

---

### 3.5 else em loops

O `else` é executado quando o loop termina normalmente (sem `break`).

```python
for i in range(1, 4):
    print(i)
else:
    print("Loop finalizado com sucesso")
```

---

## 4. Laços Aninhados

Você pode colocar um loop dentro de outro.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

---

## 5. Uso com Condições

Loops e condicionais geralmente trabalham juntos.

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "é par")
    else:
        print(i, "é ímpar")
```

---

## 6. Exercícios Práticos

1. Crie um programa que leia um número e diga se ele é positivo, negativo ou zero.
2. Use um `for` para imprimir os números de 1 a 20.
3. Use um `while` para somar números até que o usuário digite 0.
4. Crie um loop que pare quando encontrar o número 7.
5. Use um `for` com `else` para mostrar quando o loop terminar normalmente.

---

## 7. Resumo

### Condicionais:
- `if`
- `if...else`
- `if...elif...else`
- Condicionais aninhadas
- Operador ternário

### Repetição:
- `while`
- `for`
- `break`
- `continue`
- `else` em loops
- Laços aninhados

---

Essas estruturas formam a base da lógica de programação em Python e são essenciais para resolver problemas reais de forma eficiente.
