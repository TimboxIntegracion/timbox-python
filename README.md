# Python
Ejemplo con la integración al Webservice de Timbox

Se deberá hacer uso de las URL que hacen referencia al WSDL, en cada petición realizada:

- [Timbox Pruebas](https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdl)

- [Timbox Producción](https://sistema.timbox.com.mx/timbrado_cfdi33/wsdl)

Para integrar el Webservice al proyecto se requiere hacer uso del modulo Base64:

```
import base64
```

También se requiere instalar la libreria de [zeep](https://github.com/mvantellingen/python-zeep):

```
pip install zeep
```

## Timbrar CFDI
Para hacer una petición de timbrado de un CFDI, deberá enviar las credenciales asignadas, asi como el xml que desea timbrar convertido a una cadena en base64:
```
# coding=utf-8
import base64
import zeep

# Parametros para conexion al Webservice (URL de Pruebas)
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"
ruta_xml = "archivoXml.xml"

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
Para la cancelación son necesarias las credenciales asignadas, RFC del emisor, un arreglo de UUIDs, el archivo PFX convertido a cadena en base64 y el password del archivo PFX:
```
# coding=utf-8
import base64
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdll"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la cancelación del CFDI
rfc = "AAA010101AAA"
uuids = { "uuid": ["E28DBCF2-F852-4B2F-8198-CD8383891EB0", "3CFF7200-0DE5-4BEE-AC22-AA2A49052FBC", "51408B33-FE29-47DA-9517-FBF420240FD3"] }
# uuid = "E28DBCF2-F852-4B2F-8198-CD8383891EB0"
pfx_path = "archivoPfx.pfx"
bin_file = open(pfx_path, "rb").read()
pfx_base64 = base64.b64encode(bin_file)
pfx_contrasena = "12345678a"

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo cancelar_cfdi
  respuesta = cliente.service.cancelar_cfdi(usuario, contrasena, rfc, uuids, pfx_base64, pfx_contrasena)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
```

