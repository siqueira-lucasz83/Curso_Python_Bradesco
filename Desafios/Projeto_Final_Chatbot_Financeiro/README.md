# 🤖 PROJETO_FINAL_CHATBOT_FINANCEIRO

Assistente financeiro inteligente com IA generativa local usando Ollama, Python, Streamlit e MySQL.

## 🚀 Funcionalidades
- Chat com IA contextualizada
- Simulações financeiras:
  - CDI
  - Juros compostos
  - Financiamento
- Explicação de produtos financeiros
- Perfil do usuário persistente
- Histórico de conversas e simulações
- 100% local — sem envio de dados sensíveis

## 🧠 Tecnologias
- Python
- Streamlit
- Ollama (LLM local)
- MySQL
- Requests

## ▶️ Como executar

1. Instale o Ollama: https://ollama.com  
2. Baixe um modelo:
ollama pull llama3 
3. Crie o banco no MySQL Workbench: 
```sql 
CREATE DATABASE finance_ai; 
USE finance_ai; 
CREATE TABLE users ( 
   id INT AUTO_INCREMENT PRIMARY KEY, 
   nome VARCHAR(100), 
   objetivo TEXT,
   renda DECIMAL(10,2),
   risco VARCHAR(20),
   senha_hash VARCHAR(255),
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );

CREATE TABLE conversations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT, 
    role ENUM('user', 'assistant'),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (user_id) REFERENCES users(id)
 ); 
CREATE TABLE simulations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    tipo VARCHAR(50),
    parametros JSON, 
    resultado DECIMAL(15,2), 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(id) 
); 
```
4. Instale as dependências: 
```bash
 pip install -r requirements.txt 
 ``` 
5. Edite o arquivo `db/connection.py` com sua senha do MySQL: 
```python
 password="SUA_SENHA" 
 ```
6. Execute o projeto: 
```bash 
cd PROJETO_FINAL_CHATBOT_FINANCEIRO streamlit run app.py
 ```
 
## 📌 Objetivo educacional Este projeto consolida conhecimentos em IA, UX, dados e backend, aplicados a um contexto real de relacionamento financeiro, com foco em segurança, clareza e experiência do usuário.
### Feito com dedicação por Lucas Siqueira