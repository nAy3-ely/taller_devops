# nayhely.py

from datetime import datetime

# Variable que identifica tu taller
TALLER_NOMBRE = "Taller de Contenedores de Nayhely Valle"

def saludar_y_mostrar_info():
    """
    Función que imprime información de bienvenida y datos del sistema.
    """
    
    # Imprime un separador
    print("-" * 40)
    
    # Imprime el nombre de la tarea
    print(f"👋 ¡Hola! Este es mi {TALLER_NOMBRE}")
    
    # Obtiene e imprime la fecha y hora actual
    ahora = datetime.now()
    print(f"La fecha y hora actual del contenedor es: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Imprime el mensaje de éxito
    print("✅ El script Python se ha ejecutado con éxito dentro del contenedor Docker.")
    
    # Imprime un separador
    print("-" * 40)

# El punto de entrada principal del script
if __name__ == "__main__":
    saludar_y_mostrar_info()