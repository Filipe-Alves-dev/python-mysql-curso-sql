# 1. Importação (No topo do arquivo)
import mysql.connector
from mysql.connector import Error # Ajuda a lidar com erros de conexão

# --- PARÂMETROS DE CONEXÃO (Ajuste a senha) ---
# O servidor MySQL (MySQL80) geralmente roda na porta 3306 do localhost
# 2. Defina os parâmetros (Nome do Servidor, Banco de Dados, Senha, etc.)

SERVIDOR = "localhost" #localhost ou nome do servidor
USUARIO = "root" #Nome do usuário
SENHA = "jesus" #Senha do usuário
BANCO_DE_DADOS =  "curso_sql" #Nome do banco de dados 


try:
    # 3. Estabelecendo a conexão
    conexao = mysql.connector.connect(
        host=SERVIDOR,
        user=USUARIO,
        password=SENHA,
        database=BANCO_DE_DADOS
    )
    if conexao.is_connected():
        print("--"*30)
        print("Conexão bem sucedida ao banco de dados.")
        print("--"*30)

        #AREA DE TRABALHO COM O BANCO DE DADOS AQUI
        #1. Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        #2. Comandos SQL:
        
#teste commit 1
except Error as e:
    print(f"Erro ao conectar ao MySQL : {e}")

finally:
    if'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão MySQL fechada.")