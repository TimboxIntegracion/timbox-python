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
