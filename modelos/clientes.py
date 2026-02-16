class Cliente:
    def __init__(self, **kwargs):
        self.validar_not_null(kwargs)
        for clave, valor in kwargs.items():
            setattr(self, f"_{clave}", valor)
        self.tipo = "Base"
        self.descuento_fn = lambda total: total

    def validar_not_null(self, datos):
        requeridos = ["nombre", "apellido", "correo"]
        for campo in requeridos:
            valor = datos.get(campo, "")
            if valor is None or str(valor).strip() == "":
                raise ValueError(f"El campo '{campo}' no puede estar vacío.")
        
        if "@" not in str(datos.get("correo", "")):
            raise ValueError("El correo debe ser válido.")

    def to_dict(self):
        return {k.lstrip('_'): v for k, v in self.__dict__.items() if k != "descuento_fn"}

class ClienteRegular(Cliente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "Regular"
        self.descuento_fn = lambda total: total * 0.95

class ClientePremium(Cliente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "Premium"
        self.descuento_fn = lambda total: total * 0.80

class ClienteCorporativo(Cliente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tipo = "Corporativo"
        self.descuento_fn = lambda total: total * 0.70