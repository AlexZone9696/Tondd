from flask import Flask, jsonify, render_template
import requests
import webbrowser

# Создаем Flask-приложение
app = Flask(__name__)

# Функция для генерации кошелька TON через API
def generate_ton_wallet(user_id="12345"):
    # Запрос к API TON Center для создания нового кошелька
    url = "https://toncenter.com/api/v2/jsonRPC"
    
    # API запрос для создания кошелька
    data = {
        "method": "createWallet",
        "params": {}
    }
    
    headers = {
        "Content-Type": "application/json"
    }

    # Отправка запроса
    response = requests.post(url, json=data, headers=headers)
    
    # Проверка успешности запроса
    if response.status_code == 200:
        result = response.json()
        wallet_data = {
            "user_id": user_id,
            "mnemonic": result.get("mnemonic", "Ошибка генерации мнемоники"),
            "wallet": {
                "address": result.get("address", "Не удалось получить адрес"),
                "private_key": result.get("private_key", "Не удалось получить приватный ключ")
            }
        }
        return wallet_data
    else:
        return {
            "error": "Не удалось сгенерировать кошелек TON",
            "details": response.text
        }

# Маршрут для генерации кошелька для user_id=12345
@app.route('/api/user=12345', methods=['GET'])
def generate_wallets_route():
    wallet_data = generate_ton_wallet("12345")
    return jsonify(wallet_data)

# Главная страница
@app.route('/')
def index():
    return render_template('generate_wallets.html')

if __name__ == '__main__':
    # Открываем браузер автоматически после запуска сервера
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)