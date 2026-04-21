import typer
from bot.orders import place_order

app = typer.Typer()

@app.command()
def main(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    app()