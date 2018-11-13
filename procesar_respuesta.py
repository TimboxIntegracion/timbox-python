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
print(cliente)
try:
  # Llamar el metodo procesar_respuesta
  respuesta = cliente.service.procesar_respuesta(usuario, contrasena, rfc_receptor, respuestas, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception.decode("utf-8"))