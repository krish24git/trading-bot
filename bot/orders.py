from bot.client import get_client
def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        print("\n✅ ORDER SUCCESS")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\nFULL RESPONSE:")
        print(response)

    except Exception as e:
        print("❌ Binance API Error:", e)