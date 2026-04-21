# Binance Futures Trading Bot

## Setup

1. Create virtual environment
   python -m venv venv

2. Activate
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Add API keys in .env

---

## Run

### Market Order
python -m bot.cli trade BTCUSDT BUY MARKET 0.001

### Limit Order
python -m bot.cli trade BTCUSDT SELL LIMIT 0.001 --price 30000