import os
from datetime import datetime, timedelta, timezone
from flask import Flask

app = Flask(__name__)

def varrer_ativos_otc():
    melhor_opcao = "EURUSD-OTC (Tendência de Alta - Alerta de Compra)"
    return melhor_opcao

@app.route("/")
def index():
    # Fuso horário de Brasília (UTC-3)
    brasilia_tz = timezone(timedelta(hours=-3))
    agora = datetime.now(brasilia_tz)
    
    horario_atual = agora.strftime("%H:%M")
    expiracao = (agora + timedelta(minutes=5)).strftime("%H:%M")
    
    resultado = varrer_ativos_otc()
    
    return f"""
    <html>
    <head>
        <title>Resultado do Sinal</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: #ffffff; }}
            .box {{ background-color: #1e1e1e; padding: 20px; border-radius: 8px; display: inline-block; }}
            .voltar {{ margin-top: 20px; display: inline-block; color: #4da6ff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Melhor Oportunidade Encontrada:</h2>
            <p>{resultado}</p>
            <p><strong>Horário de Entrada:</strong> {horario_atual}</p>
            <p><strong>Tempo de Expiração:</strong> 5 minutos ({expiracao})</p>
        </div>
        <br>
        <a href="/" class="voltar">← Voltar e gerar novo sinal</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
