#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import  factura
import  lineaDetalle
from webapp2_extras import jinja2

class MainHandler(webapp2.RequestHandler):

    def post(self):
        #Capturar variables linea de detalle
        #concepto, precio, unidades, importe_bruto, iva, importe_total
        concepto = self.request.get("edConcepto", "Desconocido")
        precio = self.request.get("edPrecio", "Desconocido")
        unidades = self.request.get("edUnidades", "Desconocido")
        importeB = self.request.get("edImporteB", "Desconocido")
        IVA = self.request.get("edIVA", "Desconocido")
        importeT = self.request.get("edImporteT", "Desconocido")
        if len(concepto.strip()) == 0:
            concepto = "Desconocido"
        elif len(precio.strip()) == 0:
            precio = "Desconocido"
        elif len(unidades.strip()) == 0:
            unidades = "Desconocido"
        elif len(importeB.strip()) == 0:
            importeB = "Desconocido"
        elif len(IVA.strip()) == 0:
            IVA = "Desconocido"
        elif len(importeT.strip()) == 0:
            importeT = "Desconocido"

        linea = lineaDetalle.lineaDetalle(concepto,precio,unidades,importeB,IVA,importeT)

        # Capturar datos del usuario
        # CIF, nombre, direccion, poblacion, provincia, cp, pais, persona de contacto, email, telemono
        cif = self.request.get("edCIF", "Desconocido")
        nombre = self.request.get("edNombre", "Desconocido")
        direccion = self.request.get("edDireccion", "Desconocido")
        poblacion = self.request.get("edPoblacion", "Desconocido")
        provincia = self.request.get("edProvincia", "Desconocido")
        cp = self.request.get("edCP", "Desconocido")
        pais = self.request.get("edPais", "Desconocido")
        persona = self.request.get("edPC", "Desconocido")
        email = self.request.get("edCP", "Desconocido")
        telefono = self.request.get("edCP", "Desconocido")
        fecha = self.request.get("edFecha", "Desconocido")

        if len(cif.strip()) == 0:
            cif = "Desconocido"
        elif len(nombre.strip()) == 0:
            nombre = "Desconocido"
        elif len(direccion.strip()) == 0:
            direccion = "Desconocido"
        elif len(poblacion.strip()) == 0:
            poblacion = "Desconocido"
        elif len(provincia.strip()) == 0:
            provincia = "Desconocido"
        elif len(cp.strip()) == 0:
            cp = "Desconocido"
        elif len(pais.strip()) == 0:
            pais = "Desconocido"
        elif len(persona.strip()) == 0:
            persona = "Desconocido"
        elif len(email.strip()) == 0:
            email = "Desconocido"
        elif len(telefono.strip()) == 0:
            telefono = "Desconocido"
        elif len(fecha.strip()) == 0:
            fecha = "Desconocido"

        fact = factura.factura(fecha, cif, nombre, direccion, poblacion, provincia, cp, pais, persona, email, telefono)
        fact.inserta(linea)

        # Obtenemos una instancia del motor de templates
        jinja = jinja2.get_jinja2(app=self.app)

        # creamos los valores para la plantilla
        valores_plantilla = {
            "factura": fact

        }

        self.response.write(jinja.render_template("factura.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/facturas', MainHandler)
], debug=True)
