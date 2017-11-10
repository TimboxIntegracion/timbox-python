# coding=utf-8
from xml.dom.minidom import parse
import xml.dom.minidom
import base64
import zeep
from M2Crypto import RSA
from time import strftime
from lxml import etree as ET


def actualizar_sello( nombre_archivo, llave_pem ):
	#Obtener fecha y actualizarla en xml
	DOMTree = xml.dom.minidom.parse(nombre_archivo)
	fecha = strftime("%Y-%m-%dT%H:%M:%S")
	DOMTree.documentElement.setAttribute("Fecha", fecha)
	file = open(nombre_archivo, 'w')
	file.write(DOMTree.toxml())
	file.close()

	#Obtener cadena original
	file = open(nombre_archivo, 'r')
	xml = file.read()
	xdoc = ET.fromstring(xml)
	xsl_root = ET.parse('cadenaoriginal_3_3.xslt')
	xsl = ET.XSLT(xsl_root)
	cadena_original = xsl(xdoc)

	#Generar digestion y apartir de ella el sello
	keys = RSA.load_key(llave_pem)
	digest = hashlib.new('sha1', str(cadena_original)).digest()
	sello = base64.b64encode(keys.sign(digest, "sha1"))

	#Actualizar sello en xml
	DOMTree.documentElement.setAttribute("Sello", sello)
	file = open(nombre_archivo, 'w')
	file.write(DOMTree.toxml())
	file.close()

	pass

# Parametros para conexion al Webservice (URL de Pruebas)
wsdl_url = "https://staging.ws.timbox.com.mx/timbrado_cfdi33/wsdl"
usuario = "AAA010101000"
contrasena = "h6584D56fVdBbSmmnB"
ruta_xml = "ejemplo_cfdi_33.xml"

#Actualizar Sello
actualizar_sello(ruta_xml)
# Convertir la cadena del xml en base64
documento_xml = open(ruta_xml, "rb").read()
xml_base64 = base64.b64encode(documento_xml)

# Crear un cliente para hacer la petición al WS.
cliente = zeep.Client(wsdl = wsdl_url)

try:
  # llamar el metodo timbrar_cfdi
  respuesta = cliente.service.timbrar_cfdi(usuario, contrasena, xml_base64).encode("utf-8")
  print(respuesta)
except Exception as exception:
  # Imprimir los datos de la excepcion
  print("Message: %s" % exception)

