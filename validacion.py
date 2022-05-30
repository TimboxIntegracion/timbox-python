# coding=utf-8
import zeep
import base64

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/valida_cfdi/wsdl"
usuario = ""
contrasena = ""

# Parametros para la validacion de CFDI
file_xml = open("ejemplo_cfdi_33.xml", "r").read()
xml =  base64.b64encode(file_xml)

sxml = {
"Comprobante": {
	"sxml" : xml,
	"external_id" : "1"
	},
}

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo validar_cfdi
  respuesta = cliente.service.validar_cfdi(usuario, contrasena, sxml)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
