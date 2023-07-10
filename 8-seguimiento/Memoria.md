Esta memoria se incluye como un entregable del proyecto debido a las explicaciones y esquemas que contiene (principalmente para el modelo relacional). Para poder mejorar el flujo de trabajo, ciertos conceptos necesitan ser entendidos por los desarrolladores. La documentación aquí expuesta tiene un gran valor por el lenguaje ubicuo que implanta en el proyecto. 

El documento se ha escrito como notas en *Markdown* por la facilidad que da para incluir fragmentos de código relativos al proyecto y poder explicar decisiones y conceptos. Para integrar los diagramas expuestos utilizamos tecnologías como *Mermaid*, que posibilita editar los diagramas directamente en el documento, algo totalmente necesario cuando estos modelos se modifican a medida que avanzamos.

Finalmente, exportamos las notas en el orden necesario para la memoria y renderizamos el documento en HTML. El fácil acceso al documento tiene bastante relevancia por el uso que el equipo puede darle al consultar la documentación, especialmente la del modelo relacional y los servicios.

Utilizamos algunas herramientas de integración continua como *Github Actions* para automatizar este proceso. En un primer lugar convertimos el grafo de notas Markdown a un documento HTML mediante un proceso recursivo que ordena las notas y genera así la memoria del proyecto. Además, el índice se crea a partir de los nombres de las notas y sus relaciones con las que están enlazadas.

![Imagen del grafo asociado a las notas en las que se ha escrito esta memoria.](figures/graph.png)


El principal interés de que la redacción se realice de esta forma es que al comienzo del proyecto no había una idea clara de cómo se tenían que desarrollar los contenidos. Escribir un capítulo o tema en una nota es algo más sencillo (por lo tanto, se puede terminar) que pensar desde el principio dónde colocar esta sección que quiero escribir en la memoria. Utilizando Obsidian como gestor de las notas, podemos definir relaciones entre ellas simplemente conectando palabras claves, de esta forma conseguimos un esquema mental del proyecto visualizando el grafo generado. Finalmente, a medida que nos acercamos al cierre del proyecto, escribimos en un notebook una serie de algoritmos que nos permiten presentar el resultado de la memoria de la forma que deseamos. En ellos implementamos los pasos necesarios para transformar cada nota a HTML, integrar aquellos *snipets* de código que pueda contener, representar tablas y diagramas, etc. Muy importante, el grafo permite generar los niveles de indentación asociados a cada capítulo o sección del documento. A continuación, mostramos algunas de las funciones utilizadas en el cuaderno para obtener el resultado que está leyendo.

```python
def rec_note_prcs(G, start='TFG', ident='1'):

	""" recursive note building """
	
	ident = ident + '.0'
	
	neigh = list(G.neighbors(start))
	
	if (len(neigh) == 0):
	
		return note_decorate(start,ident[:-2])
		
	end_doc =  note_decorate(start,ident)
    
	  for con in neigh:
	    
	    ident = ident[:-1] + str(int(ident[-1])+1)
	    
	    end_doc = end_doc + rec_note_prcs(G, con, ident)
	    
	  return end_doc
```

Estas celdas de código son parte del proceso de transformación de Markdown a HTML. Aunque existen librerías con funciones para realizar dicha transformación, necesitamos realizar un gran trabajo de procesado para que el documento enlace las notas en el orden correcto y se tengan en cuenta conceptos como la indentación en los distintos apartados. El grafo que conforman las notas pasa a una estructura de árbol en la que es fácil crear enlaces entre los puntos a los que pertenece cada nota.

```python
def mermaid_process(text):
	
	""" transforms any mermaid diagrams to images in png format """
	
	global parent_directory
	
	result = re.findall('```mermad(?s:.*?)```', text, re.M)
	
	if len(result) <= 0:
	
		return text
	
	sub_text = result[0][len('```mermad'):-3]
	
	mermaid_dir = os.path.join(parent_directory, "mermad")
	
	text = re.sub(
		'```mermad(?s:.*?)```', 
		mmd_to_img(sub_text, mermaid_dir) ,
		text, 1
	)
	
	return mermaid_process(text)
```

Estas notas se encuentran en un repositorio separado al proyecto para poder así construir la memoria. Utilizamos *Github Actions* para definir las acciones necesarias cuando se realicen cambios en el repositorio, es decir, a medida que escribimos en las notas. En primer lugar, queremos conseguir que el documento se renderice al hacer un *commit* en el repositorio y se publique posteriormente dicha memoria en una pequeña web bajo el dominio asociado a nuestro usuario de *Github Pages* [https://alesteba.github.io/tfg/](https://alesteba.github.io/tfg/). En segundo lugar, una vez tenemos publicada la memoria, una segunda acción convertirá el código HTML asociado al documento en el archivo PDF que está leyendo actualmente. 

```yaml
  build_notes:
  
    name: Building web notes from graph
    runs-on: ubuntu-latest

    steps:

      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'
          cache: 'pip'      

      - name: Install Dependencies
        run: pip install -r requirements.txt   

      - name: Install Jupyter
        run: sudo -H pip install jupyter

      - name: Install Mermaid Converter
        run: |
          npm install -g @mermaid-js/mermaid-cli

      - name: Run Script and Build Notes
        run: |
          cd _k.pcs.zen/
          jupyter nbconvert --to script ./automate_md.ipynb
          python ./automate_md.py      
          
      - name: Pushes to another repository
        uses: cpina/github-action-push-to-another-repository@main
        env:
          API_TOKEN_GITHUB: ${{ secrets.API_TOKEN_GITHUB }}
        with:
          source-directory: '_k.pcs.zen/publish'
          destination-github-username: 'alesteba'
          destination-repository-name: 'tfg'
          user-email: alesteba@unirioja.es
          target-branch: main

```

El código anterior se corresponde con la infraestructura como código necesaria para transformar las notas de Markdown al documento en HTML. Como podemos observar en los pasos se utiliza una máquina Ubuntu en la que se instalan librerías necesarias para transformar los diagramas en imágenes y poder trabajar con cuadernos Jupyter. Posteriormente, se transforma el cuaderno con el código de conversión de las notas en un único script, se ejecuta y se publican los resultados en otro repositorio diferente, el cual mediante *Github Pages* crea la página HTML correspondiente con la memoria final. 

![Ejemplo construcción de la memoria desde Github Actions.](figures/github-actions.png)
