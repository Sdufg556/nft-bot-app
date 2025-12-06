from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎁 NFT Gifter</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://telegram.org/js/telegram-web-app.js"></script>
        <style>
            body {
                background: purple;
                color: white;
                text-align: center;
                padding: 20px;
                font-family: Arial;
            }
            .card {
                background: white;
                color: black;
                padding: 20px;
                margin: 20px auto;
                border-radius: 10px;
                max-width: 500px;
            }
            button {
                background: blue;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 10px;
                font-size: 18px;
                width: 100%;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h1>🎁 NFT GIFTER</h1>
        <div class="card">
            <h2>⭐ Звёзды: <span id="stars">1000</span></h2>
            <button onclick="buy()">Купить подарок (50 ⭐)</button>
            <div id="gifts" style="margin-top: 20px;">
                Подарков пока нет
            </div>
        </div>
        
        <script>
            let stars = 1000;
            let gifts = 0;
            
            function buy() {
                if(stars >= 50) {
                    stars -= 50;
                    gifts++;
                    document.getElementById('stars').textContent = stars;
                    document.getElementById('gifts').innerHTML = 
                        '🎁 Подарок #' + gifts + ' куплен!<br>' +
                        '<button onclick="upgrade()">Улучшить (25 ⭐)</button>';
                    alert('Куплено!');
                } else {
                    alert('Мало звёзд!');
                }
            }
            
            function upgrade() {
                if(stars >= 25) {
                    stars -= 25;
                    document.getElementById('stars').textContent = stars;
                    alert('Улучшено!');
                }
            }
            
            // Telegram
            if(window.Telegram && Telegram.WebApp) {
                Telegram.WebApp.expand();
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
