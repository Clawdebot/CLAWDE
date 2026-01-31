import requests

COIN_ALIASES = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana",
    "bnb": "binancecoin",
    "xrp": "ripple",
    "ada": "cardano",
    "doge": "dogecoin"
}

def get_crypto_price(symbol):
    try:
        symbol = symbol.lower()
        coin = COIN_ALIASES.get(symbol, symbol)

        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}"
        r = requests.get(url, timeout=10)
        data = r.json()

        
        if not data:
            return "❌ Coin tidak ditemukan."

        coin_data = data[0]
        price = coin_data["current_price"]
        change = coin_data["price_change_percentage_24h"]
        marketcap = coin_data["market_cap"]
        rank = coin_data["market_cap_rank"]

        arrow = "📈" if change > 0 else "📉"

        return (
            "━━━━━━━━━━━━━━━\n"
            f"💰 {coin.upper()} Price: ${price}\n"
            f"{arrow} 24h Change: {change:.2f}%\n"
            f"🏦 Market Cap: ${marketcap:,}\n"
            f"🏆 Rank: #{rank}\n"
            "━━━━━━━━━━━━━━━"
        )

    except Exception as e:
        return f"⚠️ Crypto Error: {e}"
