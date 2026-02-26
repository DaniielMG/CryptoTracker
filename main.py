# main.py
from monitor import CryptoEngine

def run_application():
    """
    Función principal para configurar e iniciar 
    el motor de monitoreo de criptomonedas.
    """
    # 1. Instanciamos el motor
    app = CryptoEngine()
    
    # 2. Configuramos la ejecución
    # loops: cuántas veces pedirá datos
    # delay: segundos de espera entre peticiones
    CICLOS = 5 
    ESPERA = 15 
    
    print("========================================")
    print("   CRYPTO MONITORING SYSTEM v1.0        ")
    print("========================================")
    
    # 3. Arrancamos
    app.start(loops=CICLOS, delay=ESPERA)
    
    print("\n[FIN] El proceso ha terminado correctamente.")

if __name__ == "__main__":
    run_application()
    