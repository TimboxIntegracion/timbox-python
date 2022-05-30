# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = ""
contrasena = ""

# Parametros para la consulta de documentos relacionados
rfc_receptor = "AAA010101AAA"
uuid = "2636D0CC-EF64-43C1-A83E-EDAE28A08478"

file_cer_pem = open("./Certificados/EKU9003173C9.cer.pem", "r").read()
file_key_pem = open("./Certificados/EKU9003173C9.key.pem", "r").read()

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo consultar_documento_relacionado
  respuesta = cliente.service.consultar_documento_relacionado(usuario, contrasena, uuid, rfc_receptor, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
