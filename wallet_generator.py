from flask import Flask, jsonify
from tonsdk.contract.wallet import Wallets, WalletVersionEnum

app = Flask(__name__)

@app.route('/generate_wallet', methods=['GET'])
def generate_wallet():
    # Генерация кошелька
    mnemonics, pub_k, priv_k, wallet = Wallets.create(WalletVersionEnum.v4r2, workchain=0)
    wallet_address = wallet.address.to_string(True, True, False)

    # Формируем ответ в формате JSON с мнемониками как список
    response = {
        'address': wallet_address,
        'mnemonics': mnemonics  # Список мнемоник
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)