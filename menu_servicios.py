import os
import json
from modelos.clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from modelos.productos import Producto
from servicios.clientes_servicios import clientes_servicios

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_productos_json():
    ruta = 'base_datos/productos.json'
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            try: return json.load(f)
            except: return []
    return []

def ejecutar_menu():
    gestor = clientes_servicios()
    
    while True:
        limpiar()
        print("="*65)
        print(f" GESTOR INTELIGENTE DE CLIENTES ")
        print("="*65)
        print("1. 👥 Gestor de Clientes (Ingresar, Editar, Eliminar)")
        print("2. 🛒 Simular Venta")
        print("3. 📦 Ver Listado de Productos y Descuentos")
        print("4. ❌ Salir")
        print("="*65)
        
        op = input("\nSeleccione una opción: ")

        if op == "1":
            while True:
                limpiar()
                print("--- MENÚ GESTOR DE CLIENTES ---")
                print("1. Ingresar Cliente")
                print("2. Editar Cliente")
                print("3. Eliminar Cliente")
                print("4. Ver Listado")
                print("5. Volver al Menú Principal")
                sub_op = input("\nOpción: ")

                if sub_op == "1":
                    limpiar()
                    print("--- REGISTRO DE CLIENTE ---")
                    nom = input("Nombre: ").strip()
                    ape = input("Apellido: ").strip()
                    cor = input("Correo: ").strip()
                    if not nom or not ape or not cor:
                        print("\n🛑 ERROR: Campos obligatorios.")
                    else:
                        print("\nCategoría: 1.Regular | 2.Premium | 3.Corporativo")
                        t = input("Opción: ")
                        clases = {"1": ClienteRegular, "2": ClientePremium, "3": ClienteCorporativo}
                        if t in clases:
                            nuevo = clases[t](nombre=nom, apellido=ape, correo=cor)
                            gestor.registrar(nuevo)
                            print("\n✅ Cliente registrado.")
                        else: print("\n❌ Tipo no válido.")
                    input("Presione Enter...")

                elif sub_op in ["2", "3"]:
                    accion = "EDITAR" if sub_op == "2" else "ELIMINAR"
                    limpiar()
                    print(f"--- {accion} CLIENTE ---")
                    print("1. Ingrese ID | 2. Ver Listado de Clientes")
                    metodo = input("Opción: ")
                    if metodo == "2":
                        for i, c in enumerate(gestor.clientes):
                            print(f"[{i}] {c['nombre']} {c['apellido']}")
                    
                    try:
                        idx = int(input(f"\nID Cliente a {accion.lower()}: "))
                        if 0 <= idx < len(gestor.clientes):
                            if sub_op == "2":
                                print("Deje en blanco para no cambiar.")
                                n_nom = input("Nuevo Nombre: ").strip() or gestor.clientes[idx]['nombre']
                                n_ape = input("Nuevo Apellido: ").strip() or gestor.clientes[idx]['apellido']
                                n_cor = input("Nuevo Correo: ").strip() or gestor.clientes[idx]['correo']
                                gestor.clientes[idx]['nombre'] = n_nom
                                gestor.clientes[idx]['apellido'] = n_ape
                                gestor.clientes[idx]['correo'] = n_cor
                                gestor.guardar_datos()
                                print("✅ Editado")
                            else:
                                del gestor.clientes[idx]
                                gestor.guardar_datos()
                                print("🗑️ Eliminado")
                        else: print("❌ ID no existe")
                    except: print("❌ Error de ingreso")
                    input("Presione Enter...")

                elif sub_op == "4":
                    limpiar()
                    print(f"{'ID':<4} {'NOMBRE':<15} {'APELLIDO':<15} {'TIPO':<15}")
                    print("-" * 55)
                    for i, c in enumerate(gestor.clientes):
                        print(f"{i:<4} {c['nombre']:<15} {c['apellido']:<15} {c['tipo']:<15}")
                    input("\nPresione Enter...")

                elif sub_op == "5": break

        elif op == "2":
            limpiar()
            productos = cargar_productos_json()
            if not gestor.clientes or not productos:
                print("⚠️ Se requieren Clientes y Productos.")
            else:
                try:
                    while True:
                        print("1. Ingrese ID Cliente | 2. Ver Listado")
                        if input("Opción: ") == "2":
                            for i, c in enumerate(gestor.clientes): print(f"[{i}] {c['nombre']} {c['apellido']}")
                        idx_c = int(input("ID Cliente: "))
                        if 0 <= idx_c < len(gestor.clientes): break
                    
                    while True:
                        print("\n1. Ingrese ID Producto | 2. Ver Listado")
                        if input("Opción: ") == "2":
                            for i, p in enumerate(productos): print(f"[{i}] {p['nombre']} - ${p['precio']}")
                        idx_p = int(input("ID Producto: "))
                        if 0 <= idx_p < len(productos): break

                    p_data, c_data = productos[idx_p], gestor.clientes[idx_c]
                    mapa = {"Regular": ClienteRegular, "Premium": ClientePremium, "Corporativo": ClienteCorporativo}
                    cliente_obj = mapa[c_data['tipo']](**c_data)
                    final = cliente_obj.descuento_fn(p_data['precio'])
                    
                    print(f"\n🚀 PRECIO FINAL: ${int(final):,}".replace(",", "."))
                except: print("❌ Error en simulación.")
            input("\nPresione Enter...")

        elif op == "3":
            limpiar()
            productos = cargar_productos_json()
            for i, p_data in enumerate(productos):
                p = Producto(**p_data)
                print(f"[{i}] {p.nombre:<20} ${f'{p.precio:,}'.replace(',', '.'):<10}")
            input("\nPresione Enter...")

        elif op == "4": break