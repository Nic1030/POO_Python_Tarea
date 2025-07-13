import os
import time

class GestorDeArchivos:
    """
    Clase que simula la gestión de un archivo, demostrando el uso de
    constructores (__init__) y destructores (__del__).

    El constructor abre un archivo y el destructor lo cierra,
    simulando la gestión de recursos.
    """

    def __init__(self, nombre_archivo, modo='w'):
        """
        Constructor de la clase GestorDeArchivos.

        Se ejecuta automáticamente cuando se crea una nueva instancia de la clase.
        Su propósito principal es inicializar el objeto y sus atributos.

        Args:
            nombre_archivo (str): El nombre del archivo a gestionar.
            modo (str): El modo de apertura del archivo ('w' para escribir, 'a' para añadir, etc.).
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = None
        try:
            # Intentamos abrir el archivo. Esta es la inicialización del recurso.
            self.archivo = open(self.nombre_archivo, modo, encoding='utf-8')
            print(f"CONSTRUCTOR: Archivo '{self.nombre_archivo}' abierto en modo '{modo}'.")
        except IOError as e:
            print(f"CONSTRUCTOR ERROR: No se pudo abrir el archivo '{self.nombre_archivo}': {e}")
            self.archivo = None # Asegurarse de que sea None si falla la apertura

    def escribir_linea(self, texto):
        """
        Método para escribir una línea de texto en el archivo.
        """
        if self.archivo:
            self.archivo.write(texto + '\n')
            print(f"  ESCRITURA: '{texto}' escrito en '{self.nombre_archivo}'.")
        else:
            print(f"  ADVERTENCIA: No se puede escribir. Archivo '{self.nombre_archivo}' no está abierto.")

    def __del__(self):
        """
        Destructor de la clase GestorDeArchivos.

        Se ejecuta automáticamente cuando un objeto de la clase está a punto de ser
        destruido (cuando su contador de referencias llega a cero o el programa finaliza).
        Su propósito es realizar tareas de limpieza, como cerrar recursos, liberar memoria, etc.
        """
        if self.archivo:
            # Cerramos el archivo para liberar el recurso.
            self.archivo.close()
            print(f"DESTRUCTOR: Archivo '{self.nombre_archivo}' cerrado y recurso liberado.")
        else:
            print(f"DESTRUCTOR: No hay archivo que cerrar para '{self.nombre_archivo}'.")

# --- Programa Principal ---

def main():
    print("--- Demostración de Constructores y Destructores ---")

    # --- Caso 1: Creación normal de objeto y finalización de programa ---
    print("\n--- Caso 1: Objeto creado y esperado para la recolección de basura ---")
    # Al crear el objeto, se llama automáticamente al constructor __init__
    gestor1 = GestorDeArchivos("log_ejemplo1.txt", 'w')
    if gestor1.archivo:
        gestor1.escribir_linea("Este es el primer mensaje.")
        gestor1.escribir_linea("Segundo mensaje de prueba.")
    print("Objeto 'gestor1' creado. Esperando la finalización del programa para ver el destructor.")
    # El destructor de 'gestor1' se llamará cuando el script termine.

    # --- Caso 2: Objeto creado y luego se elimina la referencia explícitamente ---
    print("\n--- Caso 2: Objeto creado y referencia eliminada ---")
    gestor2 = GestorDeArchivos("log_ejemplo2.txt", 'w')
    if gestor2.archivo:
        gestor2.escribir_linea("Mensaje para el archivo 2.")
    print("Objeto 'gestor2' creado. Ahora eliminamos explícitamente la referencia.")
    # Al eliminar la última referencia al objeto, el destructor __del__ es llamado.
    del gestor2
    print("Referencia a 'gestor2' eliminada. El destructor debería haberse activado.")

    # --- Caso 3: Objeto en un ámbito de función ---
    print("\n--- Caso 3: Objeto dentro de una función ---")
    def usar_gestor_temporal(nombre):
        """Función que crea un gestor de archivos temporalmente."""
        print(f"  Dentro de 'usar_gestor_temporal' para '{nombre}'.")
        temp_gestor = GestorDeArchivos(nombre, 'a')
        if temp_gestor.archivo:
            temp_gestor.escribir_linea("Contenido añadido desde la función.")
        print(f"  Saliendo de 'usar_gestor_temporal' para '{nombre}'.")
        # Cuando 'temp_gestor' sale de ámbito, su destructor será llamado.

    usar_gestor_temporal("log_ejemplo1.txt") # Reutilizamos el archivo 1, abriéndolo en modo 'a' (append)
    print("Función 'usar_gestor_temporal' finalizada. El destructor del objeto temporal debería haberse activado.")

    # Pequeña pausa para asegurar que los mensajes del destructor se vean en orden
    time.sleep(0.5)

    print("\n--- Fin de la demostración. Los destructores de los objetos restantes (ej. 'gestor1') se llamarán ahora. ---")

    # Opcional: limpiar los archivos generados para futuras ejecuciones
    # if os.path.exists("log_ejemplo1.txt"):
    #     os.remove("log_ejemplo1.txt")
    # if os.path.exists("log_ejemplo2.txt"):
    #     os.remove("log_ejemplo2.txt")
    # print("\nArchivos de ejemplo eliminados.")

if __name__ == "__main__":
    main()
