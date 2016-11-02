# Python
Ejemplo con la integración al Webservice de Timbox

Se deberá hacer uso de las URL que hacen referencia al WSDL, en cada petición realizada:

- [Timbox Pruebas](https://staging.ws.timbox.com.mx/timbrado/wsdl)

- [Timbox Producción](https://sistema.timbox.com.mx/timbrado/wsdl)

Para integrar el Webservice al proyecto se requiere hacer uso del modulo Base64:

```
import base64
```

También se requiere instalar la libreria de [zeep](https://github.com/mvantellingen/python-zeep):

```
pip install zeep
```

##Timbrar CFDI
Para hacer una petición de timbrado de un CFDI, deberá enviar las credenciales asignadas, asi como el xml que desea timbrar convertido a una cadena en base64:
```
cadena_xml = open("path_xml/example.xml", "rb").read()
xml_base64 = base64.b64encode(cadena_xml)
```
Con la libreria de zeep crear un cliente y hacer el llamado al método timbrar_cfdi enviándole los parametros con la información necesaria:

```
client = zeep.Client(wsdl=wsdl_url)

#llamar el método timbrar
response = client.service.timbrar_cfdi(wsdl_username, wsdl_password, xml_base64)
```

##Cancelar CFDI
Para la cancelación son necesarias las credenciales asignadas, RFC del emisor, un arreglo de UUIDs, el archivo PFX convertido a cadena en base64 y el password del archivo PFX:
```
pfx_path = 'path_del_archivo/archivo.pfx'
bin_file = open(pfx_path, "rb").read()
pfx_base64 = base64.b64encode(bin_file)
```
Crear un cliente de zeep para hacer la petición de cancelación al webservice:
```
client = zeep.Client(wsdl=wsdl_url)

#hacer el llamado al método cancelar_cfdi
response = client.service.cancelar_cfdi(wsdl_username, wsdl_password, rfc, uuid, pfx_base64, pfx_password)
```

