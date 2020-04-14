class lineaDetalle():
    def __init__(self,concepto, precio, unidades, importe_bruto, iva, importe_total):
        self._concepto = concepto
        self._precio = precio
        self._unidades = unidades
        self._importe_bruto = importe_bruto
        self._iva = iva
        self._importe_total = importe_total

    @property
    def concepto(self):
        return self._concepto

    @concepto.setter
    def concepto(self, concepto):
        self._concepto = concepto

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def unidades(self):
        return self._unidades

    @unidades.setter
    def unidades(self, unidades):
        self._unidades = unidades

    @property
    def importeBruto(self):
        return self._importe_bruto

    @importeBruto.setter
    def importeBruto(self, importe_bruto):
        self._importe_bruto = importe_bruto

    @property
    def iva(self):
        return self._iva

    @iva.setter
    def iva(self, iva):
        self._iva = iva

    @property
    def importeTotal(self):
        return self._importe_total

    @importeTotal.setter
    def importeTotal(self, importe_total):
        self._importe_total = importe_total

    def __str__(self):
        return "Unidades: " + self.iva + "\n"


