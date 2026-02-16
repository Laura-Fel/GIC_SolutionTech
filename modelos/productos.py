class Producto:
    def __init__(self, **kwargs):
        if not kwargs.get('nombre') or not kwargs.get('precio'):
            raise ValueError("Nombre y Precio son obligatorios.")

        p_raw = str(kwargs.get('precio')).replace('.', '').replace(',', '')
        
        try:
            setattr(self, 'precio', int(p_raw))
        except ValueError:
            raise ValueError("El precio debe ser un número entero válido.")
        
        for clave, valor in kwargs.items():
            if clave != 'precio':
                setattr(self, clave, valor)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()}