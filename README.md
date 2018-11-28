# Python
Ejemplo con la integración al Webservice de Timbox

Se deberá hacer uso de las URL que hacen referencia al WSDL, en cada petición realizada:

Webservice de Timbrado:
- [Timbox Pruebas](https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdl)

- [Timbox Producción](https://sistema.timbox.com.mx/timbrado_cfdi33/wsdl)

Webservice de Cancelación:

- [Timbox Pruebas](https://staging.ws.timbox.com.mx/cancelacion/wsdl)

- [Timbox Producción](https://sistema.timbox.com.mx/cancelacion/wsdl)

Para integrar el Webservice al proyecto se requiere hacer uso de varias librerías como base64 y zeep(para hacer peticiones soap). Para poder generar el sello se necesitarán de las librerías: xml.dom.minidom, [M2Crypto](https://gitlab.com/m2crypto/m2crypto)  (para criptografia), time, lxml, haslib:

```
import base64
...
from M2Crypto import RSA
```
Estas librerías se pueden instalar por medio de pip:
```
pip install zeep
```
Si está utilizando python3 y tiene errores al instalar M2Crypto, puede seguir los siguientes pasos:
- Instalar prerequisitos
```
sudo apt-get install build-essential python3-dev python-dev libssl-dev swig
```
- Clonar proyecto e instalar: 
```
git clone https://gitlab.com/m2crypto/m2crypto.git
cd m2crypto-<version>
sudo python3 setup.py build
sudo python3 setup.py install
```
Para mayor información puede consultar el archivo 'INSTALL.rst' (dentro del repositorio de M2Crypto)
## Timbrar CFDI
### Generación de Sello
Para generar el sello se necesita: la llave privada (.key) en formato PEM y el XSLT del SAT (cadenaoriginal_3_3.xslt).El XSLT del SAT se utiliza para poder transformar el XML y obtener la cadena original.

La cadena original se utiliza para obtener el digest, usando las funciones de la librería de criptografía, luego se utiliza el digest y la llave privada para obtener el sello. Todo esto se realiza utilizando la libreria M2Crypto y hashlib.

Una vez generado el sello, se actualiza en el XML para que este sea codificado y enviado al servicio de timbrado.
Esto se logra mandando llamar el método de generar_sello:
```
generar_sello(comprobante, path_llave, password_llave);
```
### Timbrado
Para hacer una petición de timbrado de un CFDI, deberá enviar las credenciales asignadas, asi como el xml que desea timbrar convertido a una cadena en base64:
```
# Parametros para conexion al Webservice (URL de Pruebas)
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"
ruta_xml = "ejemplo_cfdi_33.xml"

#Actualizar Sello
actualizar_sello(ruta_xml)
# Convertir la cadena del xml en base64
documento_xml = open(ruta_xml, "rb").read()
xml_base64 = base64.b64encode(documento_xml)

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # llamar el metodo timbrar_cfdi
  respuesta = cliente.service.timbrar_cfdi(usuario, contrasena, xml_base64).encode("utf-8")
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
```
Con la libreria de zeep crear un cliente y hacer el llamado al método timbrar_cfdi enviándole los parametros con la información necesaria:

```
client = zeep.Client(wsdl=wsdl_url)

# llamar el método timbrar
response = client.service.timbrar_cfdi(wsdl_username, wsdl_password, xml_base64)
```

## Cancelar CFDI
Para la cancelación son necesarios el certificado y llave, en formato pem que corresponde al emisor del comprobante:
```
file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()
```
Con la libreria de zeep crear un cliente y hacer el llamado al método cancelar_cfdi enviándole los parametros con la información necesaria:
```
# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la cancelación del CFDI
rfc_emisor   = "AAA010101AAA"
rfc_receptor = "IAD121214B34"
uuid = "66C2B0C5-B67C-4EF8-8D2E-E6625361B059"
total = "7261.60"

file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()

folios = {
"folio": {
	"uuid" : uuid, 
	"rfc_receptor": rfc_receptor, 
	"total": total
	} 
}

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo cancelar_cfdi
  respuesta = cliente.service.cancelar_cfdi(usuario, contrasena, rfc_emisor, folios, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)

```
## Consultar Estatus CFDI
Para la consulta de estatus de CFDI solo es necesario generar la petición de consulta, Crear un cliente y hacer el llamado al método consultar_estatus enviándole los parametros con la información necesaria:
```
# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la consulta de estatus de un CFDI
rfc_emisor   = "AAA010101AAA"
rfc_receptor = "IAD121214B34"
uuid = "66C2B0C5-B67C-4EF8-8D2E-E6625361B059"
total = "7261.60"

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo consultar_estatus
  respuesta = cliente.service.consultar_estatus(usuario, contrasena, uuid, rfc_emisor, rfc_receptor, total)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)

```

## Consultar Peticiones Pendientes
Para la consulta de peticiones pendientes son necesarios el certificado y llave, en formato pem que corresponde al receptor del comprobante:
```
file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()
```
Con la libreria de zeep crear un cliente y hacer el llamado al método consultar_peticiones_pendientes enviándole los parametros con la información necesaria:
```
# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la consulta de peticiones pendientes
rfc_receptor = "AAA010101AAA"
file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()


# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo consultar_peticiones_pendientes
  respuesta = cliente.service.consultar_peticiones_pendientes(usuario, contrasena, rfc_receptor, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
```

## Procesar Respuesta
Para realizar la petición de aceptación/rechazo de la solicitud de cancelación son necesarios el certificado y llave, en formato pem que corresponde al receptor del comprobante:
```
file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()
```
Con la libreria de zeep crear un cliente y hacer el llamado al método procesar_respuesta enviándole los parametros con la información necesaria:
```
# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la procesar respuesta
rfc_emisor   = "AAA010101AAA"
rfc_receptor = "AAA010101AAA"
uuid = "66C2B0C5-B67C-4EF8-8D2E-E6625361B059"
total = "7261.60"

file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()

# A(Aceptar la solicitud), R(Rechazar la solicitud)
respuesta_solicitud = 'A'

respuestas = {
"folios_respuestas": {
	"uuid" : uuid, 
	"rfc_emisor" : rfc_emisor, 
	"total" : total,
	"respuesta" : respuesta_solicitud
	} 
}


# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo procesar_respuesta
  respuesta = cliente.service.procesar_respuesta(usuario, contrasena, rfc_receptor, respuestas, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
```
## Consultar Documentos Relacionados
Para realizar la petición de consulta de documentos relacionados son necesarios el certificado y llave, en formato pem que corresponde al receptor del comprobante:
```
file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()
```
Con la libreria de zeep crear un cliente y hacer el llamado al método consultar_documento_relacionado enviándole los parametros con la información necesaria:
```
# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la consulta de documentos relacionados
rfc_receptor = "AAA010101AAA"
uuid = "2636D0CC-EF64-43C1-A83E-EDAE28A08478"

file_cer_pem = open("CSD01_AAA010101AAA.cer.pem", "r").read()
file_key_pem = open("CSD01_AAA010101AAA.key.pem", "r").read()

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo consultar_documento_relacionado
  respuesta = cliente.service.consultar_documento_relacionado(usuario, contrasena, uuid, rfc_receptor, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
```
