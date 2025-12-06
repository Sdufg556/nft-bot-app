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
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }
            
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                color: #333;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255, 255, 255, 0.98);
                border-radius: 25px;
                padding: 25px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.2);
            }
            
            header {
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 3px solid #f0f0f0;
            }
            
            h1 {
                color: #333;
                font-size: 2.5rem;
                margin-bottom: 10px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .tagline {
                color: #666;
                font-size: 1.1rem;
                margin-bottom: 25px;
                font-style: italic;
            }
            
            .user-panel {
                display: flex;
                justify-content: center;
                margin-bottom: 30px;
            }
            
            .stars {
                background: linear-gradient(45deg, #FFD700, #FFA500);
                padding: 15px 30px;
                border-radius: 50px;
                font-size: 1.8rem;
                font-weight: bold;
                color: #333;
                box-shadow: 0 5px 15px rgba(255,215,0,0.3);
            }
            
            .section {
                margin: 40px 0;
            }
            
            h2 {
                color: #444;
                font-size: 1.8rem;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .shop-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            
            .gift-card {
                background: white;
                border-radius: 20px;
                padding: 20px;
                text-align: center;
                border: 3px solid #e0e0e0;
                transition: all 0.3s;
            }
            
            .gift-card:hover {
                transform: translateY(-5px);
                border-color: #667eea;
                box-shadow: 0 10px 25px rgba(102,126,234,0.2);
            }
            
            .gift-icon {
                font-size: 4rem;
                margin-bottom: 15px;
            }
            
            .gift-name {
                color: #333;
                font-size: 1.3rem;
                margin-bottom: 10px;
            }
            
            .gift-price {
                color: #FF8C00;
                font-size: 1.5rem;
                font-weight: bold;
                margin: 15px 0;
            }
            
            .buy-btn {
                background: linear-gradient(45deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 25px;
                font-size: 1.1rem;
                font-weight: bold;
                width: 100%;
                cursor: pointer;
                transition: all 0.3s;
            }
            
            .buy-btn:hover {
                transform: scale(1.05);
                opacity: 0.9;
            }
            
            .buy-btn:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }
            
            .my-gifts {
                background: rgba(248, 249, 250, 0.7);
                border-radius: 20px;
                padding: 25px;
                margin-top: 20px;
                border: 2px dashed #667eea;
            }
            
            .gift-item {
                background: white;
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 15px;
                border-left: 5px solid #667eea;
            }
            
            .gift-info {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
                margin-top: 15px;
                font-size: 0.9rem;
            }
            
            .info-cell {
                background: #f8f9fa;
                padding: 8px;
                border-radius: 8px;
                text-align: center;
            }
            
            .upgrade-btn {
                background: #28a745;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 20px;
                cursor: pointer;
                margin-top: 15px;
                width: 100%;
                font-weight: bold;
            }
            
            .alert {
                position: fixed;
                top: 20px;
                right: 20px;
                background: #28a745;
                color: white;
                padding: 15px 25px;
                border-radius: 10px;
                display: none;
                z-index: 1000;
            }
            
            @media (max-width: 600px) {
                .container { padding: 15px; border-radius: 20px; }
                h1 { font-size: 2rem; }
                .shop-grid { grid-template-columns: 1fr; }
            }
        </style>
    </head>
    <body>
        <div class="alert" id="alert"></div>
        
        <div class="container">
            <header>
                <h1>🎁 NFT Gifter</h1>
                <p class="tagline">Покупай и улучшай подарки, наслаждайся ботом :)</p>
                
                <div class="user-panel">
                    <div class="stars">
                        ⭐ <span id="starCount">1000</span>
                    </div>
                </div>
            </header>
            
            <main>
                <section class="section">
                    <h2>🛍️ Магазин подарков</h2>
                    <p class="tagline">Оставь тут свои звёздочки :)</p>
                    
                    <div class="shop-grid" id="shop">
                        <!-- Подарки загружаются через JS -->
                    </div>
                </section>
                
                <section class="section">
                    <h2>🎀 Ваши подарки</h2>
                    <div class="my-gifts" id="myGifts">
                        <p style="text-align: center; color: #666; padding: 40px 20px;">
                            У вас пока нет подарков. Купите первый в магазине!
                        </p>
                    </div>
                </section>
            </main>
        </div>
        
        <script>
            // Телеграм WebApp
            const tg = window.Telegram?.WebApp;
            let userId = 'user_' + Math.random().toString(36).substr(2, 9);
            
            if (tg) {
                tg.expand();
                tg.MainButton.setText("Вернуться в бот");
                tg.MainButton.show();
                userId = tg.initDataUnsafe?.user?.id || userId;
            }
            
            let userStars = 1000;
            let userGifts = [];
            
            // Магазин
            const shopItems = [
                { id: 1, type: 'basic', name: 'Базовый подарок', price: 50, emoji: '🎁' },
                { id: 2, type: 'premium', name: 'Премиум подарок', price: 150, emoji: '💎' },
                { id: 3, type: 'legendary', name: 'Легендарный подарок', price: 500, emoji: '👑' },
                { id: 4, type: 'special', name: 'Особый подарок', price: 300, emoji: '✨' }
            ];
            
            // Загружаем данные
            function loadData() {
                // Пробуем загрузить из localStorage
                const saved = localStorage.getItem('nft_gifter_' + userId);
                if (saved) {
                    const data = JSON.parse(saved);
                    userStars = data.stars || 1000;
                    userGifts = data.gifts || [];
                }
                
                updateUI();
            }
            
            // Сохраняем данные
            function saveData() {
                const data = {
                    stars: userStars,
                    gifts: userGifts
                };
                localStorage.setItem('nft_gifter_' + userId, JSON.stringify(data));
            }
            
            // Обновляем интерфейс
            function updateUI() {
                // Звезды
                document.getElementById('starCount').textContent = userStars;
                
                // Магазин
                const shop = document.getElementById('shop');
                shop.innerHTML = '';
                
                shopItems.forEach(item => {
                    const card = document.createElement('div');
                    card.className = 'gift-card';
                    card.innerHTML = `
                        <div class="gift-icon">${item.emoji}</div>
                        <div class="gift-name">${item.name}</div>
                        <div class="gift-price">${item.price} ⭐</div>
                        <button class="buy-btn" onclick="buyGift('${item.type}', ${item.price})" 
                                ${userStars < item.price ? 'disabled' : ''}>
                            ${userStars < item.price ? 'Недостаточно звезд' : 'Купить'}
                        </button>
                    `;
                    shop.appendChild(card);
                });
                
                // Мои подарки
                const myGifts = document.getElementById('myGifts');
                
                if (userGifts.length === 0) {
                    myGifts.innerHTML = `
                        <p style="text-align: center; color: #666; padding: 40px 20px;">
                            У вас пока нет подарков. Купите первый в магазине!
                        </p>
                    `;
                } else {
                    myGifts.innerHTML = '';
                    userGifts.forEach((gift, index) => {
                        const item = document.createElement('div');
                        item.className = 'gift-item';
                        item.innerHTML = `
                            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                                <div style="font-size: 3rem;">${getEmoji(gift.type)}</div>
                                <div>
                                    <h3 style="margin: 0;">${gift.name}</h3>
                                    <p style="color: #666; margin: 5px 0;">Уровень: ${gift.level}</p>
                                </div>
                            </div>
                            
                            <div class="gift-info">
                                <div class="info-cell">🎨 ${gift.pattern}</div>
                                <div class="info-cell">🖼️ ${gift.background}</div>
                                <div class="info-cell">⭐ ${gift.rarity}</div>
                                <div class="info-cell">#${index + 1}</div>
                            </div>
                            
                            <button class="upgrade-btn" onclick="upgradeGift(${index})">
                                Улучшить (25 ⭐)
                            </button>
                        `;
                        myGifts.appendChild(item);
                    });
                }
            }
            
            // Покупаем подарок
            function buyGift(type, price) {
                if (userStars < price) {
                    showAlert('Недостаточно звезд!', 'error');
                    return;
                }
                
                if (!confirm(`Купить подарок за ${price} звезд?`)) return;
                
                userStars -= price;
                
                const patterns = ["Сердца", "Звезды", "Полосы", "Точки", "Волны"];
                const backgrounds = ["Синий", "Красный", "Золотой", "Космос", "Радуга"];
                const rarities = ["Обычный", "Редкий", "Эпический", "Легендарный"];
                
                const newGift = {
                    type: type,
                    name: shopItems.find(item => item.type === type)?.name || 'Подарок',
                    price: price,
                    level: 1,
                    pattern: patterns[Math.floor(Math.random() * patterns.length)],
                    background: backgrounds[Math.floor(Math.random() * backgrounds.length)],
                    rarity: rarities[Math.floor(Math.random() * rarities.length)]
                };
                
                userGifts.push(newGift);
                saveData();
                updateUI();
                showAlert('🎉 Подарок успешно куплен!', 'success');
            }
            
            // Улучшаем подарок
            function upgradeGift(index) {
                if (userStars < 25) {
                    showAlert('Недостаточно звезд для улучшения!', 'error');
                    return;
                }
                
                userStars -= 25;
                userGifts[index].level += 1;
                
                saveData();
                updateUI();
                showAlert('✨ Подарок улучшен до уровня ' + userGifts[index].level + '!', 'success');
            }
            
            // Вспомогательные функции
            function getEmoji(type) {
                const emojis = { basic: '🎁', premium: '💎', legendary: '👑', special: '✨' };
                return emojis[type] || '🎁';
            }
            
            function showAlert(message, type = 'success') {
                const alert = document.getElementById('alert');
                alert.textContent = message;
                alert.style.background = type === 'success' ? '#28a745' : '#dc3545';
                alert.style.display = 'block';
                
                setTimeout(() => {
                    alert.style.display = 'none';
                }, 3000);
            }
            
            // Запускаем
            document.addEventListener('DOMContentLoaded', () => {
                loadData();
            });
        </script>
    </body>
    </html>
    '''

@app.route('/api/test')
def test():
    return {"status": "online", "message": "NFT Gifter работает!"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
