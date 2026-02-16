import os
import json
from menu_servicios import ejecutar_menu

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    limpiar_pantalla()
    print("="*50)
    print("  GESTOR INTELIGENTE DE CLIENTES   ")
    print("="*50)
    print("Verificando integridad de la base de datos...")

def inicializar_entorno():
   
    rutas = ['base_datos', 'docs', 'modelos', 'servicios']
    for r in rutas:
        if not os.path.exists(r):
            os.makedirs(r)
    
  
    archivos = {
        'base_datos/clientes.json': [],
        'base_datos/productos.json': []
    }
    
    for ruta, contenido in archivos.items():
        if not os.path.exists(ruta):
            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump(contenido, f, indent=4)
            print(f"✔️ Archivo {ruta} inicializado.")

def ejecutar():
    try:
      
        inicializar_entorno()
        mostrar_bienvenida()
        
        ejecutar_menu()
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa finalizado por el usuario.")
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO: {e}")
    finally:
        print("\n" + "="*50)
        print("         GRACIAS POR USAR EL SISTEMA")
        print("="*50)

if __name__ == "__main__":
    ejecutar()