Una vez tenemos un modelo que soporta las principales entidades del dominio agronómico que necesitamos, procedemos a cargar la información proveniente de distintas fuentes en la BD bajo sus correspondientes entidades y con las relaciones necesarias para las consultas. Para esta carga vamos a utilizar un pipeline de datos; veamos a qué nos referimos.

Es importante diferenciar qué tipo de estructura estamos construyendo. Existen actualmente varias arquitecturas para 'pipelines', como pueden ser ETLs u otras. Para la correcta carga y transformación de datos no utilizaremos ninguna de estas arquitecturas, sino que diseñaremos los bloques necesarios en cada paso para poblar nuestra base de datos. Este proceso puede entenderse como una canalización de datos, en la que recibimos información en diferentes fuentes y la dotamos de contexto dentro de la BD.

### Canalización de datos

Una canalización de datos hace referencia a los pasos necesarios para mover datos del sistema de origen al sistema de destino. Estos pasos incluyen copiar datos, transferirlos desde una ubicación a otra y combinarlos con otras fuentes de datos. El objetivo principal de una canalización de datos es garantizar que todos estos pasos se produzcan de forma coherente con todos los datos.

En el apartado anterior hemos visto cómo se ha diseñado el modelo de datos. Ahora nos centramos en los pequeños pasos de carga que vamos a dar para que los datos agronómicos de clientes e imágenes satelitales  persistan en dicho modelo. Valoramos la identificación de unidades atómicas de persistencia de información que puedan ejecutarse reiteradamente. Es decir, buscaremos acotar pequeños procesos de carga que puedan ejecutarse en varios puntos dependiendo del volumen de datos de clientes que maneje el equipo en un momento dado.

### Procesos de una canalización

Identificamos tres conceptos que definen la canalización de datos que vamos a llevar a cabo y exponemos qué hace el 'pipeline' de nuestra aplicación en cada uno de ellos.  

- Data Ingestion: diseñamos bloques atómicos de carga que almacenan datos de fuentes diferentes en la base de datos de la aplicación.

- Data Transformation: utilizamos los bloques de carga para almacenar los datos en nuestro modelo de Django.

- Data Storage: almacenamos los datos en el modelo a través de Django, manteniendo una base de datos relacional en la máquina en la que se encuentra la aplicación.

Como hemos dicho, hay varias formas de realizar este proceso de canalización; en nuestro caso identificaremos los bloques y diseñaremos el proceso casi de forma manual, para que se ajuste con exactitud a lo que queremos hacer. En el siguiente punto exponemos la tecnología subyacente que utilizaremos para ello. 
