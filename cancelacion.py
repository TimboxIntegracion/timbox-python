# coding=utf-8
import base64
import zeep

#parametros para la conexión al Webservice
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado/wsdl"
wsdl_username = "user_name"
wsdl_password = "password"

#parametros para la cancelación del CFDI
rfc = "IAD121214B34"
uuid = "A7A812CC-3B51-4623-A219-8F4173D061FE"
pfx_path = 'path_del_archivo/iad121214b34.pfx'
bin_file = open(pfx_path, "rb").read()
pfx_base64 = base64.b64encode(bin_file)
pfx_password = "12345678a"

#crear un cliente de savon para hacer la petición al WS, en produccion quitar el "log: true"
client = zeep.Client(wsdl=wsdl_url)

#llamar el metodo cancelar_cfdi
try:
    response = client.service.cancelar_cfdi(wsdl_username, wsdl_password, rfc, uuid, pfx_base64, pfx_password)
    print(response)
except Exception as exception:
    print("Code: %s" % exception.code)
    print("Message: %s" % exception.message)
    print("Actor: %s" % exception.actor)
    print("Detail: %s" % exception.detail)
