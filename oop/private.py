class Mensajes:
    def _procesa_mensaje(self,mensaje):
        print(mensaje)

    def salida(self, texto):
        self._procesa_mensaje(texto)

m = Mensajes()
m.salida("hola mundo")
    