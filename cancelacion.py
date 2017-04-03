# coding=utf-8
import base64
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado/wsdl"
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
