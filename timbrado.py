# coding=utf-8
import base64
import zeep

#parametros para conexion al Webservice (URL de Pruebas)
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado/wsdl"
wsdl_usuario = "user_name"
wsdl_contrasena = "password"
ruta_xml = "ruta/del/archivo.xml"

#convertir la cadena del xml en base64
documento_xml = open(ruta_xml, "rb").read()
xml_base64 = base64.b64encode(documento_xml)

#crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl=wsdl_url)

try:
  #llamar el metodo timbrar_cfdi
  respuesta = cliente.service.timbrar_cfdi(wsdl_usuario, wsdl_contrasena, xml_base64)
  print(respuesta)
except Exception as exception:
  #Imprimir los datos de la excepcion
  print("Code: %s" % exception.code)
  print("Message: %s" % exception.message)
  print("Actor: %s" % exception.actor)
  print("Detail: %s" % exception.detail)

