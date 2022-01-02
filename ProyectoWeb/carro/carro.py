class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        else:
            self.carro = carro
    
    #agregar producto al carro
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[str(producto.id)]= {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
        self.guardar_carro()

    #guardar carro en la session
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
    
    #eliminar producto del carro
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    #restamos elementos a un producto
    def restar_producto(self, producto):
        if producto.id in self.carro:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]-1
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()

    #limpiar carro
    def vaciar_carro(self):
        self.session['carro']= {}
        self.session.modified = True