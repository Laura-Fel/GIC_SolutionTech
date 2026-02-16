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
        print("1. ➕ Ingresar Cliente")
        print("2. 🛒 Simular Venta (Cargar Producto por ID)")
        print("3. 👥 Ver Listado de Clientes")
        print("4. 📦 Ver Listado de Productos y Descuentos")
        print("5. ❌ Salir")
        print("="*65)
        
        op = input("\nSeleccione una opción: ")

        if op == "1":
            limpiar()
            print("--- REGISTRO DE CLIENTE ---")
            nom = input("Nombre: ").strip()
            ape = input("Apellido: ").strip()
            cor = input("Correo: ").strip()

            if not nom or not ape or not cor:
                print("\n🛑 ERROR: Los campos Nombre, Apellido y Correo son obligatorios.")
                input("\nPresione Enter para reintentar...")
                continue 

            try:
                datos = {"nombre": nom, "apellido": ape, "correo": cor}
                print("\nCategoría: 1.Regular (5%) | 2.Premium (20%) | 3.Corporativo (30%)")
                t = input("Opción: ")
                clases = {"1": ClienteRegular, "2": ClientePremium, "3": ClienteCorporativo}
                
                if t in clases:
                    nuevo = clases[t](**datos)
                    print(f"\n¿Confirmar registro de {nuevo._nombre} {nuevo._apellido}?")
                    if input("Presione 'Sí (S)/No (N)' para confirmar: ").lower() == 's':
                        gestor.registrar(nuevo)
                        print("\n✅ Cliente registrado con éxito.")
                    else:
                        print("\n⚠️ Operación cancelada.")
                else:
                    print("\n❌ Tipo de cliente no válido.")
            
            except ValueError as e:
                print(f"\n🛑 ERROR DE VALIDACIÓN: {e}")
            
            input("\nPresione Enter para volver...")

        elif op == "2":
            limpiar()
            productos = cargar_productos_json()
            if not gestor.clientes or not productos:
                print("⚠️ Se requieren Clientes y Productos en la BD.")
            else:
                print("--- SIMULACIÓN DE VENTA ---")
                print(f"{'ID':<4} {'CLIENTE':<30} {'TIPO':<10}")
                for i, c in enumerate(gestor.clientes):
                    print(f"[{i:<2}] {c['nombre']} {c['apellido']:<20} ({c['tipo']})")
                
                try:
                    idx_c = int(input("\nID Cliente: "))
                    print("\nSeleccione Producto:")
                    print("1. Ingrese ID | 2. Ver Listado Productos")
                    opt_p = input("Opción: ")
                    
                    idx_p = -1
                    if opt_p == "2":
                        print(f"\n{'ID':<4} {'PRODUCTO':<25} {'PRECIO':<10}")
                        for i, p in enumerate(productos):
                            print(f"[{i:<2}] {p['nombre']:<25} ${p['precio']:<10}")
                        idx_p = int(input("\nID Producto: "))
                    else:
                        idx_p = int(input("ID Producto: "))

                    if 0 <= idx_p < len(productos):
                        p_data = productos[idx_p]
                        prod_obj = Producto(**p_data)
                        c_data = gestor.clientes[idx_c]
                        mapa = {"Regular": ClienteRegular, "Premium": ClientePremium, "Corporativo": ClienteCorporativo}
                        cliente_obj = mapa[c_data['tipo']](**c_data)
                        final = cliente_obj.descuento_fn(prod_obj.precio)
                        
                        p_base = f"{prod_obj.precio:,}".replace(",", ".")
                        p_final = f"{int(final):,}".replace(",", ".")

                        print("\n" + "📜" + "─"*35 + "📜")
                        print(f"    RECIBO DE VENTA SIMULADA")
                        print("─"*37)
                        print(f"👤 Cliente:       {cliente_obj._nombre} {cliente_obj._apellido}")
                        print(f"💎 Tipo:          {cliente_obj.tipo}")
                        print(f"📦 Producto:      {prod_obj.nombre}")
                        print(f"💰 Precio Base:   ${p_base}")
                        print("─"*37)
                        print(f"🚀 PRECIO FINAL:  ${p_final}")
                        print("─"*37)
                    else: print("❌ ID no existe.")
                except Exception as e: print(f"❌ Error: {e}")
            input("\nPresione Enter...")

        elif op == "3":
            limpiar()
            print(f"{'ID':<4} {'NOMBRE':<15} {'APELLIDO':<15} {'TIPO':<15}")
            print("-" * 55)
            for i, c in enumerate(gestor.clientes):
                print(f"{i:<4} {c['nombre']:<15} {c['apellido']:<15} {c['tipo']:<15}")
            input("\nPresione Enter...")

        elif op == "4":
            limpiar()
            productos = cargar_productos_json()
            print(f"{'ID':<4} {'PRODUCTO':<20} {'BASE':<10} {'REG(5%)':<10} {'PRE(20%)':<10} {'CORP(30%)':<10}")
            print("-" * 75)
            for i, p in enumerate(productos):
                b = p['precio']
                print(f"{i:<4} {p['nombre']:<20} ${b:<9} ${b*0.95:<9.0f} ${b*0.80:<9.0f} ${b*0.70:<9.0f}")
            input("\nPresione Enter...")

        elif op == "5":
            break