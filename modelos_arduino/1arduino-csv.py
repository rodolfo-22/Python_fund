import serial
import csv

# Configuración del puerto serial
puerto = 'COM7'  # Cambia al puerto correcto
baudrate = 9600  # Debe coincidir con la configuración en Arduino
archivo_salida = 'datitos2.csv'  # Archivo donde se guardarán los datos útiles

try:
    # Abrir conexión serial
    with serial.Serial(puerto, baudrate, timeout=1) as ser, open(archivo_salida, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        print("Conexión al puerto serial establecida.")
        print("Esperando interacciones con el Arduino...")

        while True:
            # Leer línea desde el puerto serial
            linea = ser.readline().decode('utf-8').strip()

            # Mostrar todos los mensajes del Arduino en la terminal
            if linea:
                print(linea)  # Mostrar el mensaje del Arduino

                # Si la línea contiene datos relevantes (formato: Tiempo,Motor,Distancia)
                partes = linea.split(',')
                if len(partes) == 3 and partes[0].isdigit() and partes[2].isdigit():
                    # Guardar datos en el archivo CSV
                    escritor.writerow(partes)

except KeyboardInterrupt:
    print("\nFinalizando la captura de datos.")
except Exception as e:
    print(f"Error: {e}")
