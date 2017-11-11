# Python
Ejemplo con la integración al Webservice de Timbox

Se deberá hacer uso de las URL que hacen referencia al WSDL, en cada petición realizada:

- [Timbox Pruebas](https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdl)

- [Timbox Producción](https://sistema.timbox.com.mx/timbrado_cfdi33/wsdl)

Para integrar el Webservice al proyecto se requiere hacer uso de varias librerías como base64 y zeep(para hacer peticiones soap). Para poder generar el sello se necesitarán de las librerías: xml.dom.minidom, M2Crypto(para criptografia), time, lxml, haslib:

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
- Clonar proyecto e instalar, para mayor información puede consultar el archivo 'INSTALL.rst' (dentro del repositorio de M2Crypto)
```
git clone https://gitlab.com/m2crypto/m2crypto/tree/python3/
cd m2crypto-<version>
sudo python3 setup.py build
sudo python3 setup.py install
```

## Timbrar CFDI
### Generación de Sello
Para generar el sello se necesita: la llave privada (.key) en formato PEM. También es necesario incluir el XSLT del SAT para poder transformar el XML y obtener la cadena original.

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

