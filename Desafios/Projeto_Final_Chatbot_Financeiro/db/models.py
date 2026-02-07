from db.connection import get_connection
import json
import bcrypt

def create_user(nome, objetivo, renda, risco, senha):
    conn = get_connection()
    cursor = conn.cursor()
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
    cursor.execute("""
        INSERT INTO users (nome, objetivo, renda, risco, senha_hash)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, objetivo, renda, risco, senha_hash))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return user_id

def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def get_user_by_name(nome):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE nome = %s", (nome,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def verify_password(senha, senha_hash):
    return bcrypt.checkpw(senha.encode(), senha_hash.encode())

def save_message(user_id, role, message):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO conversations (user_id, role, message)
        VALUES (%s, %s, %s)
    """, (user_id, role, message))
    conn.commit()
    cursor.close()
    conn.close()

def get_conversation_history(user_id, limit=20):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT role, message FROM conversations
        WHERE user_id = %s
        ORDER BY created_at ASC
        LIMIT %s
    """, (user_id, limit))
    history = cursor.fetchall()
    cursor.close()
    conn.close()
    return history

def save_simulation(user_id, tipo, parametros, resultado):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO simulations (user_id, tipo, parametros, resultado)
        VALUES (%s, %s, %s, %s)
    """, (user_id, tipo, json.dumps(parametros), resultado))
    conn.commit()
    cursor.close()
    conn.close()

def get_simulations(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT tipo, parametros, resultado, created_at
        FROM simulations
        WHERE user_id = %s
        ORDER BY created_at DESC
    """, (user_id,))
    sims = cursor.fetchall()
    cursor.close()
    conn.close()
    return sims

