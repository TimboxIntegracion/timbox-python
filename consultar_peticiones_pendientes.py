# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"

# Parametros para la consulta de peticiones pendientes
rfc_receptor = "EKU9003173C9"
file_cer_pem = open("./Certificados/EKU9003173C9.cer.pem", "r").read()
file_key_pem = open("./Certificados/EKU9003173C9.key.pem", "r").read()


# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo consultar_peticiones_pendientes
  respuesta = cliente.service.consultar_peticiones_pendientes(usuario, contrasena, rfc_receptor, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
