import re
import pyodbc
from datetime import datetime
from config import DATABASE_CONFIG


# função para extrair o OTP  
def extrai_otp(body): 
   num_otp = re.compile(r'\b\d{6}\b')
   verifica_otp = num_otp.search(body)
   # o if evita que caso não encontre o otp retorne com um erro
   if verifica_otp: # match
       return verifica_otp.group() # match
   return None

# função para se conectar e armazenar o OTP no banco de dados
def conexao_banco(otp):
   conexao = (
       f"DRIVER={DATABASE_CONFIG['DRIVER']};"
       f"SERVER={DATABASE_CONFIG['SERVER']};"
       f"DATABASE={DATABASE_CONFIG['DATABASE']};"
       f"UID={DATABASE_CONFIG['UID']};"
       f"PWD={DATABASE_CONFIG['PWD']}"
   )

   conn = pyodbc.connect(conexao)
   cursor = conn.cursor()
   
   # Inserir o OTP no banco de dados com a data atual e status de utilização
   data_recebido = datetime.now()
   utilizado = False

   # faz o insert no banco para colocar o número do otp, dia que gerou e se já foi utilizado
   cursor.execute("""
   INSERT INTO OTP_SFA (TOKEN, DATA_RECEBIDO, JA_UTILIZADO)  
   VALUES (?, ?, ?)""" , (otp, data_recebido, utilizado))
   
   # faz um commit para atualizar a tabela e fecha o banco
   conn.commit()
   conn.close()