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

