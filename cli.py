import time
import random

class MockBinanceFuturesClient:
    """Simulates the Binance Futures API without needing real keys."""
    def __init__(self):
        self.balance = 10000.00  # Starts with 10,000 USDT test balance

    def get_account_balance(self):
        return round(self.balance, 2)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        print(f"\n⏳ Processing {order_type} {side} order for {quantity} {symbol}...")
        time.sleep(1)  # Simulate network latency
        
        # Calculate mock trade price
        exec_price = price if price else round(random.uniform(60000, 65000), 2)
        total_cost = round(exec_price * quantity, 2)
        
        if side.upper() == "BUY":
            self.balance -= total_cost
        else:
            self.balance += total_cost

        return {
            "orderId": random.randint(100000, 999999),
            "symbol": symbol.upper(),
            "status": "FILLED",
            "side": side.upper(),
            "type": order_type.upper(),
            "price": exec_price,
            "origQty": quantity,
        }

def main():
    bot = MockBinanceFuturesClient()

    print("==========================================")
    print(" 🚀 Binance Futures CLI Bot (Simulated)   ")
    print("==========================================")
    print(f"✅ Connected to Simulation Server")
    print(f"💰 Starting Balance: {bot.get_account_balance()} USDT\n")

    # Interactive CLI Loop
    while True:
        print("\nChoose an option:")
        print("1. Check Wallet Balance")
        print("2. Place Market Order (BUY/SELL)")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            print(f"\n💰 Current Wallet Balance: {bot.get_account_balance()} USDT")
        elif choice == "2":
            symbol = input("Enter Symbol (e.g. BTCUSDT): ").strip().upper() or "BTCUSDT"
            side = input("Enter Side (BUY/SELL): ").strip().upper() or "BUY"
            try:
                qty = float(input("Enter Quantity (e.g. 0.1): ").strip() or "0.1")
            except ValueError:
                print("❌ Invalid quantity. Using default 0.1")
                qty = 0.1
                
            order = bot.place_order(symbol, side, "MARKET", qty)
            print("\n🎉 --- ORDER FILLED ---")
            print(f"Order ID: {order['orderId']}")
            print(f"Symbol  : {order['symbol']}")
            print(f"Side    : {order['side']}")
            print(f"Price   : ${order['price']}")
            print(f"Remaining Balance: {bot.get_account_balance()} USDT")
        elif choice == "3":
            print("\nExiting CLI Bot. Goodbye! 👋")
            break
        else:
            print("❌ Invalid selection. Try again.")

if __name__ == "__main__":
    main()