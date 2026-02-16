🚀 GIC Solution Tech - Sistema de Gestión de Ventas

GIC Solution Tech es una aplicación de consola desarrollada en Python que implementa un sistema integral de gestión de clientes y simulación de ventas. El proyecto destaca por su arquitectura de N-Capas y un uso avanzado de los pilares de la Programación Orientada a Objetos (POO).


🏗️ Arquitectura del Sistema (Estructura de Carpetas)
El proyecto sigue una organización modular para separar las responsabilidades, facilitando el mantenimiento y la escalabilidad:

SolutionTech/
├── main.py                 # Orquestador y CLI (Interfaz de Usuario)
├── modelos/                # Entidades de Dominio (Herencia)
│   ├── __init__.py
│   ├── clientes.py         # Clases Cliente (Regular, Premium y Corporativo)
│   └── productos.py        # Modelo de Producto
├── servicios/              # Lógica de Negocio y Persistencia
│   ├── __init__.py
│   └── clientes_servicios.py # Gestión de JSON y sanitización de datos
├── base_datos/             # Almacenamiento Persistente
│   ├── clientes.json       # DB de Clientes
│   └── productos.json      # DB de Productos
├── docs/                   # Documentación Técnica
│   └── diagrama_clases.puml # Código fuente UML
└── .gitignore              # Exclusión de archivos temporales y locales


🧩 Pilares POO Implementados

1. Encapsulamiento
La inicialización se realiza mediante Metaprogramación con setattr(), permitiendo que las clases sean flexibles a cambios en el esquema de datos.

2. Herencia Dinámica
Existe una clase base Cliente de la cual heredan tres especializaciones:

ClienteRegular: Aplica un 5% de descuento.

ClientePremium: Aplica un 20% de descuento.

ClienteCorporativo: Aplica un 30% de descuento.

3. Polimorfismo
El motor de ventas no requiere conocer el tipo de cliente de antemano. Al invocar el método calcular_total(precio), Python ejecuta automáticamente la lógica de descuento correspondiente a la instancia específica en tiempo de ejecución.

4. Abstracción
El uso de **kwargs en los constructores permite abstraer la creación de objetos, delegando la responsabilidad de los atributos a la estructura de los datos crudos (JSON).


🛠️ Funcionalidades Principales

Registro Dinámico: Alta de clientes con asignación de ID autoincremental gestionada por el servicio.

Simulador de Venta: Integración entre clientes y productos con cálculo de beneficios en tiempo real.

Gestión de Catálogo: Visualización tabulada y formateada de productos disponibles.

Persistencia Robusta: Carga y guardado automático en archivos JSON con manejo de errores para datos corruptos.


📈 Reglas de Negocio: Segmentación y Beneficios

El sistema implementa una arquitectura basada en herencia y funciones de orden superior para el cálculo de ventas. Cada categoría de cliente extiende de la clase base Cliente y sobrescribe el comportamiento del cálculo mediante una expresión lambda:

Tipo de Cliente	| Descuento |	Lógica Técnica (Método)
Regular	        | 5%       	| self.descuento_fn = lambda total: total * 0.95
Premium	        | 20%       | self.descuento_fn = lambda total: total * 0.80
Corporativo 	| 30%	    | self.descuento_fn = lambda total: total * 0.70

Nota para el desarrollador: Esta estructura permite modificar los porcentajes de beneficio directamente en el archivo modelos/clientes.py sin alterar el flujo de venta en el main.py.


📊 Guía de Pruebas (Seed Data)

Para validar el Polimorfismo y la Persistencia de inmediato, el sistema cuenta con los siguientes datos base pre-cargados:

1. Perfiles de Cliente (base_datos/clientes.json)

ID	|Nombre	      |Tipo	       |Descuento
1	|Juan Perez	  |Regular	   |5%
2	|Ana Garcia   |Premium	   |20%
3	|Carlos Soto  |Corporativo |30%

2. Catálogo de Productos (base_datos/productos.json)

ID	|Producto	            |Precio Base
1	|Laptop Gamer           |$1.200.000
2	|Mouse Inalámbrico   	|$25.000
3	|Monitor 4K         	|$350.000


Escenario de Prueba: Al seleccionar al Cliente ID 2 (Premium) y el Producto ID 1 ($1.200.000), el sistema aplicará automáticamente el beneficio Premium, resultando en un total de **$960.000**.


🚀 Instalación y Uso
Clonar el repositorio y navegar a la carpeta raíz.

Preparar la base de datos: El sistema creará los archivos automáticamente si no existen, pero se recomienda tener productos.json con datos iniciales en la carpeta base_datos/.

Ejecutar la aplicación:

python main.py

Nota: El sistema detectará automáticamente si faltan las bases de datos e inicializará los archivos .json en su primer inicio.


📊 Documentación Gráfica

El código fuente del diagrama de clases se encuentra en docs/diagrama_clases.puml. Este diagrama detalla las relaciones de asociación, dependencia y herencia entre los módulos.

