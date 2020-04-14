import lineaDetalle
class factura():
    """ cif = self.request.get("edCIF", "Desconocido")
        nombre = self.request.get("edNombre", "Desconocido")
        direccion = self.request.get("edDireccion", "Desconocido")
        poblacion = self.request.get("edPoblacion", "Desconocido")
        provincia = self.request.get("edProvincia", "Desconocido")
        cp = self.request.get("edCP", "Desconocido")
        pais = self.request.get("edPais", "Desconocido")
        persona = self.request.get("edPC", "Desconocido")
        email = self.request.get("edCP", "Desconocido")
        telefono = self.request.get("edCP", "Desconocido")
        fecha = self.request.get("edFecha", "Desconocido")"""
    def __init__(self, fecha, cif, nombre, direccion, poblacion, provincia, cp, pais, persona, email, telefono):
        self._fecha = fecha
        self._cif = cif
        self._nombre = nombre
        self._direccion = direccion
        self._poblacion = poblacion
        self._provincia = provincia
        self._cp = cp
        self._pais = pais
        self._persona = persona
        self._email = email
        self._telefono = telefono
        self._linea = list()

    @property
    def fecha(self):
        return  self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def cif(self):
        return self._cif

    @property
    def nombre(self):
        return self._nombre

    @property
    def direccion(self):
        return self._direccion

    @property
    def poblacion(self):
        return self._poblacion

    @property
    def provincia(self):
        return self._provincia

    @property
    def cp(self):
        return self._cp

    @property
    def pais(self):
        return self._pais

    @property
    def persona(self):
        return self._persona

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    @property
    def linea(self):
        return self._linea

    def inserta(self, lin):
        self.linea.append(lin)