# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado_cfdi40/wsdl"

usuario = ""
contrasena = ""

uuid_buscar = "00000000-0000-0000-0000-000000000000"

comprobante = { "uuid": uuid_buscar }
uuid = { "Comprobante" : comprobante}

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo consultar_estatus
  respuesta = cliente.service.recuperar_comprobante(usuario, contrasena, uuid)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)

