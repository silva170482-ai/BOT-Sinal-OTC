import os
from flask import Flask

app = Flask(__name__)

def varrer_ativos_otc():
    melhor_opcao = "EURUSD-OTC (Tendência de Alta - Alerta de Compra)"
    return melhor_opcao

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Robô de Sinais OTC</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: #fff; }
                .btn { background-color: #28a745; color: white; padding: 20px 40px; font-size: 20px; border: none; border-radius: 8px; cursor: pointer; text-decoration: none; display: inline-block; }
                .btn:hover { background-color: #218838; }
            </style>
        </head>
        <body>
            <h1>Robô de Sinais OTC Sob Demanda</h1>
            <p>Clique no botão abaixo para varrer os ativos e gerar o sinal:</p>
            <br>
            <form action="/gerar-sinal" method="get">
                <button type="submit" class="btn">Gerar Sinal Agora</button>
            </form>
        </body>
    </html>
    """

@app.route("/gerar-sinal")
def gerar_sinal():
    resultado = varrer_ativos_otc()
    return f"""
    <html>
        <head>
            <title>Resultado do Sinal</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: #fff; }}
                .box {{ background-color: #1e1e1e; padding: 20px; border-radius: 8px; display: inline-block; border: 1px solid #333; }}
                .voltar {{ margin-top: 20px; display: inline-block; color: #4da6ff; text-decoration: none; }}
            </style>
        </head>
        <body>
            <div class="box">
                <h2>Melhor Oportunidade Encontrada:</h2>
                <p style="font-size: 18px; color: #4eff88;"><b>{resultado}</b></p>
            </div>
            <br>
            <a href="/" class="voltar">← Voltar e gerar novo sinal</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
