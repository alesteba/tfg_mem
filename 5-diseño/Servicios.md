Ahora tenemos un modelo relacional que soporta la gestión de grandes volúmenes de datos. En este punto tenemos que diseñar las diferentes operaciones que necesitamos hacer sobre los datos almacenados. Discutimos cómo tiene que ser la implementación de las operaciones más frecuentes y por qué en un modelo de datos sin estado, con información histórica, es más importante diseñar estas operaciones sobre el modelo relacional como servicios.

El término servicio está sobrecargado y su significado adquiere diferentes matices según el contexto en que estemos. Como resultado, existe una nube de confusión en torno a la noción de servicios cuando se trata de distinguir entre servicios de aplicación, servicios de dominio, servicios de infraestructura, servicios SOA, etc. Las funciones de estos son diferentes y pueden abarcar todas las capas de una aplicación.

De hecho, un servicio es un título un tanto genérico para un bloque de creación de una aplicación porque implica muy poco. En primer lugar, un servicio implica un cliente para cuyas solicitudes está diseñado. Otra característica de una operación de servicio es la de entrada y salida: se proporcionan argumentos  como entrada a una operación y se devuelve un resultado. Ms allá de esta implicación suelen estar los supuestos de "statelessness" y la idea de "pure fabrication", según GRASP:

**When a significant process or transformation in the domain is not a natural responsibility of an ENTITY or VALUE OBJECT, add an operation to the model as standalone interface declared as a SERVICE. Define the interface in terms of the language of the model and make sure the operation name is part of the UBIQUITOUS LANGUAGE. Make the SERVICE stateless.**

**Eric Evans** Domain-Driven Design

El tipo de servicios que estamos diseñando e implementando para nuestra aplicación forman parte de la capa de dominio. Estos servicios de dominio a menudo se pasan por alto como bloques de construcción clave, confundidos por el enfoque de las entidades del modelo (o value objects).

Cumpliendo con los principios mencionados, los servicios conforman la siguiente capa de abstracción del modelo de datos implementado. Colocaremos aquellas operaciones que dependan o relacionen más de una entidad en su módulo correspondiente de servicios y no como un método de la clase del modelo. Este tipo de diseño en el que dejamos el modelo casi sin métodos propios puede llegar a entenderse como un anti-patrón, [anemic domain model](http://martinfowler.com/bliki/AnemicDomainModel.html), pero que en nuestro caso, tras buscar la forma más sencilla de acceder a la información, será de gran utilidad.

Justificamos la implementación de gran parte de los métodos sobre la capa de servicios por el tipo de información histórica sobre la que necesitamos hacer las consultas. La mayoría de entidades necesitan de una relación con otra segunda o tercera entidad para devolver la información pertinente. **Como el modelo está orientado a manejar información histórica y sin estado**, optamos por colocar casi todos los métodos de acceso a los datos en un módulo de servicios aparte. Miremos el siguiente ejemplo sobre los históricos fenológicos en el parcelario registrado.

```python

class ParcelaCultivos_Service():

	def get_cultivo(parcela_p):

		""" último cultivo que se está cultivando en una parcela """

		mirar_feno = Mirar_Fenologico.objects.filter(parcela = parcela_p.idx)
	
		if (mirar_feno.count() > 0):
	
			return mirar_feno.order_by('fecha')[0].cultivo
	
		else:
	
			return None

	def get_historico_fenologicos(parcela_p):
	
		""" todos los estados fenológicos por los que ha pasado una parcela """
	
		return Mirar_Fenologico.objects.filter(parcela = parcela_p.referencia)
	
	def get_historico_range(fecha_inicio, fecha_end):
	
		""" histórico de todas las parcelas en un rango de fechas """
	
		return Mirar_Fenologico.objects.filter(fecha__range=[fecha_inicio, fecha_end])
	
	def get_historico_parcela(parcela1):
	
		""" todo el histórico de una parcela """
	
		return Mirar_Fenologico.objects.filter(parcela = parcela1)
	
	def get_historico_parcela_range(parcela1, fecha_inicio, fecha_end):
	
		""" hostórico de una parcela en un rango de fechas """
	
		historico = ParcelaCultivos_Service.get_historico_range(fecha_inicio, fecha_end)
	
		return historico.filter(parcela = parcela1)
	
	def get_historico_mismo_fenologico(valor_fenologico):
	
		""" todo los cultivos que están en un mismo estado fenológico """
	
		return Mirar_Fenologico.objects.filter(estado = valor_fenologico)

```

[Adjuntamos](https://github.com/alesteba/tfg/tree/main/entregables/services) como entregables del proyecto algunos de los servicios diseñados y usados más frecuentemente. El código de estos servicios es utilizado por el resto de miembros del equipo para otras tareas de la aplicación, como puede ser la presentación de los datos en la interfaz web.

El pipeline que vamos a diseñar es posible gracias a la factorización en módulos de la aplicación y a la sencillez y versatilidad del modelo relacional de datos. Los servicios que ahora implementamos abstraen al resto del equipo de la funcionalidad subyacente y me permiten crear diferentes interfaces con propósitos distintos. Son muy importantes, ya que nos acercan al flujo de trabajo de integración continua que estamos buscando.

Por otro lado, tenemos métodos más clásicos en los que hacemos uso de las entidades registradas para obtener valores concretos. La siguiente función es una de las más usadas debido a la integración directa con el proceso de descarga de imágenes satelitales del cultivo. Fijémonos en cómo utilizamos las entidades creadas anteriormente para acceder a la información de la BD, el ORM subyacente nos abstrae de otras consultas complejas que podríamos hacer en lenguajes como SQL.

```python

def get_indice_func(parcela, indice_p, fecha_p, func, filtro):

	"""Método que encapsula el uso de una función agregada junto con un filtro """

	indice_p = Indice.objects.get(nombre=indice_p) 
	
	if ParcelaIndices_Service.is_parcela_filter(parcela, filtro):
	
		pixels = parcela.get_pixeles()
		
		indices_pixels = Mirar_Indice.objects.filter(
		
			pixel__in = pixels, 
			indice = indice_p, 
			fecha = fecha_p
		)
		
		if ParcelaIndices_Service.get_indice_filter(indices_pixels, filtro):
		
			array_valores = list(indices_pixels.values_list('valor', flat=True))
			
			return func(array_valores)

```