import requests
import time
import pandas as pd
from datetime import datetime

class CryptoEngine:
    def __init__(self):
        # El Top 10 más influyente en 2026
        self.symbols = [
            "BTCUSDT",  # Bitcoin
            "ETHUSDT",  # Ethereum
            "SOLUSDT",  # Solana (Alta velocidad)
            "BNBUSDT",  # Binance Coin
            "XRPUSDT",  # Ripple (Pagos)
            "ADAUSDT",  # Cardano
            "DOGEUSDT", # Dogecoin (Comunidad/Meme)
            "TRXUSDT",  # TRON
            "DOTUSDT",  # Polkadot (Interoperabilidad)
            "LINKUSDT"  # Chainlink (Oráculos de datos)
        ]
        self.base_url = "https://api.binance.com/api/v3/ticker/price"
        self.data_log = []

    def get_market_data(self):
        """Extrae datos de la API para los 10 símbolos"""
        print(f"\n[INFO] Fetching data at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
        
        current_batch = []
        for symbol in self.symbols:
            try:
                response = requests.get(f"{self.base_url}?symbol={symbol}", timeout=5)
                data = response.json()
                
                entry = {
                    'timestamp': datetime.now(),
                    'symbol': data['symbol'].replace('USDT', ''),
                    'price': float(data['price'])
                }
                current_batch.append(entry)
                self.data_log.append(entry)
            except Exception as e:
                print(f" Error with {symbol}: {e}")
        
        return current_batch

    def display_report(self, batch):
        """Muestra un reporte limpio en consola"""
        df = pd.DataFrame(batch)
        print(df[['symbol', 'price']].to_string(index=False))

    def save_to_csv(self):
        """Guarda todo el histórico a un archivo CSV"""
        df_final = pd.DataFrame(self.data_log)
        filename = f"crypto_history_{datetime.now().strftime('%Y%m%d')}.csv"
        df_final.to_csv(filename, index=False)
        print(f"\n Data saved to {filename}")

    def start(self, loops=3, delay=10):
        try:
            for i in range(loops):
                data = self.get_market_data()
                self.display_report(data)
                if i < loops - 1:
                    time.sleep(delay)
            self.save_to_csv()
        except KeyboardInterrupt:
            print("\nStop requested by user.")
            self.save_to_csv()

