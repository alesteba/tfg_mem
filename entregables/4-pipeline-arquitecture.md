* posiblemente todos los scripts que permiten el flujo de datos * 

Adjuntamos los scripts utilizados para el desarrollo del flujo de datos con su arquitectura y diseño como pipeline. 

```python

class Command(LoggingBaseCommand):

    help = 'Carga la geometría a las parcelas y a los pixeles'

    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    PARCELA_SHAPE = BASE_DIR / 'data' / 'parcelas' / '25' / 'parcelas.shp'
    PIXEL_SHAPE = BASE_DIR / 'data' / 'parcelas' / '25' / 'pixeles.shp'
    FICHERO_PATH  = BASE_DIR / 'data' / 'excels' /  'datos-test-2.xls'
    TRILINEA_PATH = BASE_DIR / 'data' / 'trilineas' / 'PRilineas.json'

    def handle(self,  *args, **kwargs):

        self.run()

    def run(self):
    
        # execute in order:

        print(Path(self.PARCELA_SHAPE))

		call_command('1-load-qgis',parcelas=self.PARCELA_SHAPE, pixels=self.PIXEL_SHAPE)

        call_command('2-load-parcela-data', excel=str(self.FICHERO_PATH))

        call_command('3-load-cultivos', excel=str(self.FICHERO_PATH))
```
