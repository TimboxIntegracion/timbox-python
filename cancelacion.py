# coding=utf-8
import zeep

# Parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/cancelacion/wsdl"

usuario = ""
contrasena = ""

# Parametros para la cancelación del CFDI
rfc_emisor   = "AAA010101AAA"
rfc_receptor = "IAD121214B34"
uuid = "66C2B0C5-B67C-4EF8-8D2E-E6625361B059"
total = "7261.60"
motivo = "03"
folio_sustituto = ""

file_cer_pem = open("./Certificados/EKU9003173C9.cer.pem", "r").read()
file_key_pem = open("./Certificados/EKU9003173C9.key.pem", "r").read()

folios = {
"folio": {
	"uuid" : uuid,
	"rfc_receptor": rfc_receptor,
	"total": total,
  "motivo": motivo,
  "folio_sustituto" : folio_sustituto
	}
}

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # Llamar el metodo cancelar_cfdi
  respuesta = cliente.service.cancelar_cfdi(usuario, contrasena, rfc_emisor, folios, file_cer_pem, file_key_pem)
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)
