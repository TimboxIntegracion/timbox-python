# coding=utf-8
import base64
import zeep

#parametros para conexion al Webservice (URL de Pruebas)
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado/wsdl"
wsdl_username = "user_name"
wsdl_password = "password"

#convertir la cadena del xml en base64
xml_base64 = base64.b64encode(cadena_xml)

#crear un cliente de savon para hacer la petición al WS
client = zeep.Client(wsdl=wsdl_url)

#llamar el metodo timbrar_cfdi
try:
    response = client.service.timbrar_cfdi(wsdl_username, wsdl_password, xml_base64)
    print(response)
except Exception as exception:
    print("Code: %s" % exception.code)
    print("Message: %s" % exception.message)
    print("Actor: %s" % exception.actor)
    print("Detail: %s" % exception.detail)

