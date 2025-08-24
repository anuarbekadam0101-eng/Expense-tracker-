from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Хранилище данных (пока в памяти)
transactions = []

@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['POST'])
def add():
    amount = int(request.form['amount'])
    description = request.form['description']
    date = datetime.datetime.now()

    transactions.append({
        'amount': amount,
        'description': description,
        'date': date.strftime("%Y-%m-%d %H:%M")
    })
    return redirect(url_for('index'))
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
