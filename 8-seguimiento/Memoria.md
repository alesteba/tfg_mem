Esta memoria se incluye como un entregable del proyecto debido a las explicaciones y esquemas que contiene (principalmente para el modelo relacional). Para poder mejorar el flujo de trabajo, ciertos conceptos necesitan ser entendidos por los desarrolladores. La documentación aquí expuesta tiene un gran valor por el lenguaje ubicuo que implanta en el proyecto. 

El documento se ha escrito como notas en *Markdown* por la facilidad que da para incluir fragmentos de código relativos al proyecto y poder explicar decisiones y conceptos. Para integrar los diagramas expuestos utilizamos tecnologías como *Mermaid*, que posibilita editar los diagramas directamente en el documento, algo totalmente necesario cuando estos modelos se modifican a medida que avanzamos.

Finalmente, exportamos las notas en el orden necesario para la memoria y renderizamos el documento en HTML. El fácil acceso al documento tiene bastante relevancia por el uso que el equipo puede darle al consultar la documentación, especialmente la del modelo relacional y los servicios.

Utilizamos algunas herramientas de integración continua como *Github Actions* para automatizar este proceso. En un primer lugar convertimos el grafo de notas Markdown a un documento HTML mediante un proceso recursivo que ordena las notas y genera así la memoria del proyecto. Además, el índice se crea a partir de los nombres de las notas y sus relaciones con las que están enlazadas.

![](figures/graph.png)


Estas notas se encuentran en un repositorio separado al proyecto para poder así construir la memoria. Utilizamos *Github Actions* para definir las acciones necesarias cuando se realicen cambios en el repositorio, es decir, a medida que escribimos en las notas. En primer lugar, queremos conseguir que el documento se renderice cuando se hacen cambios en el repositorio y se publique posteriormente dicha memoria en una pequeña web bajo el dominio asociado a nuestro usuario de *Github Pages*. En segundo lugar, una vez tenemos publicada la memoria, una segunda acción convertirá el código HTML asociado al documento en el archivo PDF que está leyendo actualmente. 

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

El código anterior se corresponde con la transformación de la memoria en notas de Markdown al documento en HTML. Como podemos observar en los pasos se utiliza una máquina Ubuntu en la que se instalan librerías necesarias para transformar los diagramas en imágenes y poder trabajar con cuadernos Jupyter. Posteriormente, se transforma el cuaderno con el código de conversión de las notas en un único script, se ejecuta y se publican los resultados en otro repositorio diferente, el cual mediante *Github Pages* crea la página HTML correspondiente con la memoria final. 

![](figures/github-actions.png)
