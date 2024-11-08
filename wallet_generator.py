from flask import Flask, jsonify, render_template
import tonweb
import webbrowser

# Создаем Flask-приложение
app = Flask(__name__)

# Функция для генерации кошелька TON
def generate_ton_wallet(user_id="12345"):
    # Инициализация TonWeb
    api_url = 'https://toncenter.com/api/v2/jsonRPC'
    tonweb_instance = tonweb.TonWeb(api_url)

    # Генерация ключей TON
    keys = tonweb_instance.utils.generateKeys()

    # Получаем адрес из публичного ключа
    address = tonweb_instance.utils.addressFromPublicKey(keys.public)

    return {
        "user_id": user_id,
        "mnemonic": str(keys.mnemonic),  # Получаем мнемонику для восстановления
        "wallet": {
            "address": address,
            "private_key": keys.secret
        }
    }

# Маршрут для генерации кошелька для user_id=12345
@app.route('/api/user=12345', methods=['GET'])
def generate_wallets_route():
    # Генерируем кошельки для user_id=12345
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
