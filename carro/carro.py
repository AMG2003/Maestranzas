# class Carro:
#     def __init__(self, request):
#         self.request = request
#         self.session = request.session
#         carro = self.session.get("carro")
#         if not carro:
#             carro = self.session["carro"] = {}
#         # else:
#         self.carro = carro

#     def agregar(self, pieza):
#         if str(pieza.id) not in self.carro.keys():
#             self.carro[pieza.pieza] = {
#                 "pieza": pieza.id,
#                 "descripcion": pieza.descripcion,
#                 "numero_serie": pieza.numero_serie,
#                 "cantidad": 1,
#                 "precio_unitario": str(pieza.precio_unitario),
#                 
#             }
#         else:
#             for key, value in self.carro.items():
#                 if key == str(pieza.id):
#                     value["cantidad"] = value["cantidad"] + 1
#                     value["precio_unitario"] = float(value["precio_unitario"]) + pieza.precio_unitario
#                     break
#         self.guardar_Carro()

#     def guardar_Carro(self):
#         self.session["carro"] = self.carro
#         self.session.modified = True

#     def eliminar(self, pieza):
#         pieza.id = str(pieza.id)
#         if pieza.id in self.carro:
#             del self.carro[pieza.id]
#             self.guardar_Carro()

#     def restar_producto(self, pieza):
#         for key, value in self.carro.items():
#             if key == str(pieza):
#                 value["cantidad"] = value["cantidad"] - 1
#                 value["precio_unitario"] = float(value["precio_unitario"]) - pieza.precio_unitario
#                 if value["cantidad"] < 1:
#                     self.eliminar(producto)
#                 break
#         self.guardar_Carro()

#     def limpiar_carro(self):
#         self.session["carro"] = {}
#         self.session.modified = True
