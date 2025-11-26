import time
from pymodbus.client import ModbusTcpClient  # sync client for pymodbus 3.x

# -------------------------------
# Modbus client setup
# -------------------------------
HOST = "127.0.0.1"  # lokal host, eller IP på serveren
PORT = 5020         # den port vi kørte Modbus server på

client = ModbusTcpClient(HOST, port=PORT)

if not client.connect():
    print("Kunne ikke forbinde til Modbus server")
    exit(1)

print("Forbundet til Modbus server!")

# -------------------------------
# Læs holding register løbende
# -------------------------------
try:
    while True:
        # Læs 1 holding register fra adresse 0
        rr = client.read_holding_registers(address=0, count=1, unit=1)
        
        if rr.isError():
            print("Fejl ved læsning:", rr)
        else:
            # Skaler tilbage til float (x100)
            value = rr.registers[0] / 100.0
            print(f"Register 0: {value}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Stopper Modbus klienten...")
finally:
    client.close()
