import os
from datetime import datetime, timedelta, timezone
from flask import Flask, render_template_string
import random

app = Flask(__name__)

def varrer_ativos_otc():
    """
    Simula a varredura técnica de ativos OTC com base em critérios de tendência,
    momentum ou regras de indicadores (similar a lógicas de scripts de binárias).
    """
    ativos = ["EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC", "AUDUSD-OTC"]
    ativo_escolhido = random.choice(ativos)
    
    # Exemplo de regra lógica baseada em condições técnicas simuladas
    # Aqui você pode inserir os parâmetros exatos do seu script (ex: RSI, MAs, etc.)
    direcoes = [
        ("Tendência de Alta - Alerta de Compra (CALL)", "🟢"),
        ("Tendência de Baixa - Alerta de Venda (PUT)", "🔴")
    ]
    direcao, icone = random.choice(direcoes)
    
    melhor_opcao = f"{ativo_escolhido} ({direcao}) {icone}"
    return melhor_opcao

@app.route("/")
def index():
    brasilia_tz = timezone(timedelta(hours=-3))
    agora = datetime.now(brasilia_tz)
    
    # Alinha rigidamente para o próximo bloco de 5 minutos cheios
    proximos_5_minutos = 5 - (agora.minute % 5)
    horario_entrada_dt = agora + timedelta(minutes=proximos_5_minutos)
    horario_entrada = horario_entrada_dt.strftime("%H:%M")
    
    # Expiração exata de 5 minutos após o sinal
    expiracao_dt = horario_entrada_dt + timedelta(minutes=5)
    expiracao = expiracao_dt.strftime("%H:%M")
    
    resultado = varrer_ativos_otc()
    
    html = """
    <html>
    <head>
        <title>Bot Sinal OTC - Analítico</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: #ffffff; }
            .box { background-color: #1e1e1e; padding: 25px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
            .voltar { margin-top: 20px; display: inline-block; color: #4da6ff; text-decoration: none; font-weight: bold; }
            .voltar:hover { text-decoration: underline; }
            h2 { color: #00ffcc; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Melhor Oportunidade Encontrada:</h2>
            <p style="font-size: 18px; font-weight: bold;">{{ resultado }}</p>
            <hr style="border: 0; border-top: 1px solid #333; margin: 15px 0;">
            <p><strong>Horário de Entrada:</strong> {{ horario_entrada }}</p>
            <p><strong>Tempo de Expiração:</strong> 5 minutos (Expira às {{ expiracao }})</p>
        </div>
        <br>
        <a href="/" class="voltar">🔄 Atualizar e Gerar Novo Sinal</a>
    </body>
    </html>
    """
    return render_template_string(html, resultado=resultado, horario_entrada=horario_entrada, expiracao=expiracao)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
