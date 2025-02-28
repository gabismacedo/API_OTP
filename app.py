# biblioteca Flask para trabalhar com a API
from flask import Flask, request, jsonify
from utils import extrai_otp, conexao_banco

# requisição __name__ usada para encontrar arquivos estáticos e determinar o caminho para a aplicação
app = Flask(__name__)

# rota para onde o json se encontra e usado o método POST
@app.route('/otp', methods=['POST']) 

# função para obter o número do OTP
def processo_otp(): 
   ler_requisicao_json = request.get_json() # variável recebe o json que foi enviado do VBA outlook
   # se o json "email_body" não for encontrado, retorna o erro
   if 'email_body' not in ler_requisicao_json:
       return jsonify({"error": "o arquivo json 'email_body' não foi encontrado"}), 400
   
   # se o json for encontrado, ele lê o arquivo, se conecta no banco e armazena o número do OTP no banco
   email_body = ler_requisicao_json['email_body']
   otp = extrai_otp(email_body)
   if otp:
       conexao_banco(otp)
       return jsonify({"message": "OTP processado com sucesso", "otp": otp}), 200
   else:
       return jsonify({"error": "o arquivo json 'email_body' não foi encontrado"}), 400

# localhost e porta que é acessado
if __name__ == "__main__":
   app.run(port=5000, host='localhost', debug=True)