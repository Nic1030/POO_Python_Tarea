# ==============================================================================
# OBJETIVO:
# Demostrar la aplicación de los conceptos de POO en Python:
# - Definición de Clase y Objeto
# - Herencia
# - Encapsulación
# - Polimorfismo
# ==============================================================================

# 1. Clase Base: Empleado
# Esta clase representa la entidad base de un empleado en la empresa.
class Empleado:
    """
    Clase base para representar un empleado general en la empresa.
    Demuestra la definición de una clase y sus atributos/métodos básicos.
    """
    def __init__(self, nombre, id_empleado, salario):
        """
        Constructor de la clase Empleado.
        Define los atributos básicos de un empleado.
        """
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario = salario

    def mostrar_info(self):
        """
        Método para mostrar la información básica del empleado.
        """
        print(f"--- Información del Empleado ---")
        print(f"Nombre: {self.nombre}")
        print(f"ID Empleado: {self.id_empleado}")
        print(f"Salario: ${self.salario:.2f}")

    def calcular_bono(self):
        """
        Método para calcular un bono base para todos los empleados.
        Este método será sobrescrito en clases derivadas (Polimorfismo).
        """
        return self.salario * 0.05 # 5% de bono base

# 2. Clase Derivada: Gerente
# Esta clase hereda de Empleado y añade funcionalidades específicas de un gerente.
class Gerente(Empleado):
    """
    Clase derivada de Empleado, representa a un Gerente.
    Demuestra el concepto de Herencia: Gerente "es un" Empleado.
    """
    def __init__(self, nombre, id_empleado, salario, departamento):
        """
        Constructor de la clase Gerente.
        Llama al constructor de la clase base (Empleado) y añade un atributo propio.
        """
        super().__init__(nombre, id_empleado, salario) # Llama al constructor de la clase padre
        self.departamento = departamento

    def mostrar_info(self):
        """
        Método sobrescrito de la clase base (Polimorfismo).
        Muestra la información del gerente, incluyendo el departamento.
        """
        super().mostrar_info() # Llama al método mostrar_info de la clase padre
        print(f"Departamento: {self.departamento}")

    def calcular_bono(self):
        """
        Método sobrescrito de la clase base (Polimorfismo).
        Calcula un bono diferente y mayor para los gerentes.
        """
        return self.salario * 0.15 + 500 # 15% de bono + 500 extra

    def gestionar_equipo(self):
        """
        Método específico de la clase Gerente.
        """
        print(f"{self.nombre} está gestionando su equipo en el departamento de {self.departamento}.")

# 3. Clase Derivada: Desarrollador
# Esta clase hereda de Empleado y añade funcionalidades específicas de un desarrollador.
class Desarrollador(Empleado):
    """
    Clase derivada de Empleado, representa a un Desarrollador.
    Demuestra herencia y encapsulación.
    """
    def __init__(self, nombre, id_empleado, salario, lenguaje_principal):
        super().__init__(nombre, id_empleado, salario)
        # Encapsulación: El lenguaje principal es un atributo protegido.
        # Convención: un solo guion bajo '_' indica que es un atributo "protegido".
        # Python no impone la privacidad de forma estricta, pero es una convención.
        self._lenguaje_principal = lenguaje_principal
        # Encapsulación: 'proyectos_asignados' es un atributo privado.
        # Convención: doble guion bajo '__' indica que es un atributo "privado" (name mangling).
        self.__proyectos_asignados = []

    def mostrar_info(self):
        """
        Método sobrescrito de la clase base (Polimorfismo).
        Muestra la información del desarrollador, incluyendo el lenguaje principal.
        """
        super().mostrar_info()
        print(f"Lenguaje Principal: {self._lenguaje_principal}")
        print(f"Proyectos Asignados: {', '.join(self.__proyectos_asignados) if self.__proyectos_asignados else 'Ninguno'}")

    def calcular_bono(self):
        """
        Método sobrescrito de la clase base (Polimorfismo).
        Calcula un bono específico para desarrolladores.
        """
        return self.salario * 0.10 # 10% de bono para desarrolladores

    # Encapsulación: Métodos para acceder y modificar atributos encapsulados (getters/setters)
    def get_lenguaje_principal(self):
        """Getter para _lenguaje_principal."""
        return self._lenguaje_principal

    def set_lenguaje_principal(self, nuevo_lenguaje):
        """Setter para _lenguaje_principal."""
        if isinstance(nuevo_lenguaje, str) and len(nuevo_lenguaje) > 0:
            self._lenguaje_principal = nuevo_lenguaje
            print(f"El lenguaje principal de {self.nombre} se ha actualizado a {nuevo_lenguaje}.")
        else:
            print("Error: El nuevo lenguaje principal no es válido.")

    def asignar_proyecto(self, proyecto):
        """
        Método para añadir proyectos a la lista de proyectos asignados (atributo privado).
        Demuestra cómo interactuar con atributos privados de forma controlada.
        """
        if isinstance(proyecto, str) and proyecto not in self.__proyectos_asignados:
            self.__proyectos_asignados.append(proyecto)
            print(f"Proyecto '{proyecto}' asignado a {self.nombre}.")
        else:
            print(f"Error al asignar proyecto '{proyecto}' a {self.nombre}.")

    def get_proyectos_asignados(self):
        """
        Getter para __proyectos_asignados (atributo privado).
        """
        # Se devuelve una copia para evitar modificación externa directa de la lista original
        return list(self.__proyectos_asignados)


# ==============================================================================
# DEMOSTRACIÓN DE FUNCIONALIDAD
# Creación de objetos e interacción con sus métodos.
# ==============================================================================

if __name__ == "__main__":
    print("===========================================")
    print("DEMOSTRACIÓN DE PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("===========================================\n")

    # 1. Creación de Objetos (Instancias de Clases)
    print("--- Creación de Instancias ---")
    empleado1 = Empleado("Juan Pérez", "EMP001", 30000)
    gerente1 = Gerente("Ana García", "GER001", 75000, "Ventas")
    desarrollador1 = Desarrollador("Carlos Ruiz", "DEV001", 50000, "Python")
    print("Instancias creadas exitosamente.\n")

    # 2. Demostración de Métodos y Atributos (Clase Base)
    print("--- Información de Empleado Base ---")
    empleado1.mostrar_info()
    print(f"Bono de {empleado1.nombre}: ${empleado1.calcular_bono():.2f}\n")

    # 3. Demostración de Herencia y Polimorfismo (Métodos Sobrescritos)
    print("--- Información de Gerente (Clase Derivada y Polimorfismo) ---")
    gerente1.mostrar_info() # Llama al mostrar_info de Gerente (sobrescrito)
    print(f"Bono de {gerente1.nombre}: ${gerente1.calcular_bono():.2f}") # Llama al calcular_bono de Gerente (sobrescrito)
    gerente1.gestionar_equipo() # Método específico de Gerente
    print("")

    print("--- Información de Desarrollador (Clase Derivada y Polimorfismo) ---")
    desarrollador1.mostrar_info() # Llama al mostrar_info de Desarrollador (sobrescrito)
    print(f"Bono de {desarrollador1.nombre}: ${desarrollador1.calcular_bono():.2f}\n")

    # 4. Demostración de Encapsulación (atributos _protegidos y __privados)
    print("--- Demostración de Encapsulación en Desarrollador ---")
    # Acceso a atributo protegido (por convención, se puede acceder directamente pero es desaconsejado)
    print(f"Lenguaje principal (acceso directo a _atributo): {desarrollador1._lenguaje_principal}")

    # Uso de getter y setter para _lenguaje_principal
    desarrollador1.set_lenguaje_principal("Java")
    print(f"Nuevo lenguaje principal (vía getter): {desarrollador1.get_lenguaje_principal()}")

    # Intentar acceder al atributo privado directamente (genera error si se hace fuera de la clase sin name mangling)
    # print(desarrollador1.__proyectos_asignados) # Esto causaría un AttributeError

    # Uso del método público para modificar/acceder al atributo privado
    desarrollador1.asignar_proyecto("Sistema de Nóminas")
    desarrollador1.asignar_proyecto("App Móvil V2")
    print(f"Proyectos asignados (vía getter): {desarrollador1.get_proyectos_asignados()}")
    desarrollador1.mostrar_info() # Verifica que los proyectos se muestran correctamente

    print("\n--- Demostración de Polimorfismo (Argumentos Múltiples/Variables) ---")
    # Función que acepta diferentes tipos de objetos (empleados)
    def imprimir_reporte_bono(empleado):
        """
        Esta función demuestra polimorfismo al aceptar cualquier objeto
        que tenga un método 'mostrar_info()' y 'calcular_bono()'.
        """
        print(f"\nGenerando reporte de bono para: {empleado.nombre}")
        empleado.mostrar_info() # Se llama al método mostrar_info() adecuado para cada tipo de objeto
        print(f"Bono Calculado: ${empleado.calcular_bono():.2f}") # Se llama al método calcular_bono() adecuado

    imprimir_reporte_bono(empleado1)
    imprimir_reporte_bono(gerente1)
    imprimir_reporte_bono(desarrollador1)

    print("\n===========================================")
    print("FIN DE LA DEMOSTRACIÓN")
    print("===========================================")
