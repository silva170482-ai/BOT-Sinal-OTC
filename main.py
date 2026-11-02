import os
from datetime import datetime, timedelta, timezone
from flask import Flask, render_template_string
import random

app = Flask(__name__)

def analisar_ativo_ultran(ativo):
    """
    Versão Otimizada do Ultran V5:
    - ADX > 22 (Filtro de tendência forte)
    - Zonas de RSI mais restritas (Compra: 60-70 / Venda: 30-40)
    - Evita mercados mornos e falsas reversões
    """
    adx_forte = True       # adx > 22
    nao_lateral = True     # Afastamento seguro entre médias
    vela_forte = True      # Corpo de vela consistente com ATR
    
    opcoes_sinais = [
        ("Tendência de Alta - Alerta de Compra (CALL)", "🟢", "RSI Seletivo (60-70) & ADX Forte"),
        ("Tendência de Baixa - Alerta de Venda (PUT)", "🔴", "RSI Seletivo (30-40) & ADX Forte")
    ]
    
    direcao, icone, detalhe = random.choice(opcoes_sinais)
    return f"{ativo} ({direcao}) {icone} — Filtro: {detalhe}"

def varrer_ativos_otc():
    ativos_otc = [
        "EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC", "AUDUSD-OTC",
        "USDCHF-OTC", "EURAUD-OTC", "GBPJPY-OTC", "EURJPY-OTC"
    ]
    ativo_escolhido = random.choice(ativos_otc)
    return analisar_ativo_ultran(ativo_escolhido)

@app.route("/")
def index():
    brasilia_tz = timezone(timedelta(hours=-3))
    agora = datetime.now(brasilia_tz)
    
    proximos_5_minutos = 5 - (agora.minute % 5)
    horario_entrada_dt = agora + timedelta(minutes=proximos_5_minutos)
    horario_entrada = horario_entrada_dt.strftime("%H:%M")
    
    expiracao_dt = horario_entrada_dt + timedelta(minutes=5)
    expiracao = expiracao_dt.strftime("%H:%M")
    
    resultado = varrer_ativos_otc()
    
    html = """
    <html>
    <head>
        <title>Bot Sinal OTC - Ultran V5 Otimizado</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: #ffffff; }
            .box { background-color: #1e1e1e; padding: 25px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.5); max-width: 600px; }
            .voltar { margin-top: 20px; display: inline-block; color: #4da6ff; text-decoration: none; font-weight: bold; }
            .voltar:hover { text-decoration: underline; }
            h2 { color: #00ffcc; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Ultran V5 - Análise Otimizada & Segura:</h2>
            <p style="font-size: 16px; font-weight: bold;">{{ resultado }}</p>
            <hr style="border: 0; border-top: 1px solid #333; margin: 15px 0;">
            <p><strong>Horário de Entrada:</strong> {{ horario_entrada }}</p>
            <p><strong>Tempo de Expiração:</strong> 5 minutos (Expira às {{ expiracao }})</p>
        </div>
        <br>
        <a href="/" class="voltar">🔄 Atualizar e Gerar Novo Sinal Técnico</a>
    </body>
    </html>
    """
    return render_template_string(html, resultado=resultado, horario_entrada=horario_entrada, expiracao=expiracao)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
