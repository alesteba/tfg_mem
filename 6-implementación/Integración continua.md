Una vez hemos identificado los pasos atómicos que queremos ejecutar de forma secuencial, utilizamos la herramienta de integración continua, Jenkins, para ejecutar estos pasos de forma ordenada y ver poco a poco el proceso. 

El siguiente script reproduce el flujo de uso común de la aplicación desde su creación, pasando por todos los pasos de carga de datos en el modelo, hasta la vista minable sobre la cual se obtiene el modelo de producción de kg de cultivo. 

La ejecución del siguiente pipeline tiene lugar tras lanzar la máquina Vagrant sobre la que corre el proyecto. En el comienzo de la memoria habíamos hablado de que dicha máquina se provisiona con los scripts necesarios para instalar las dependencias del proyecto. En este punto con la máquina en dicho estado, los primeros pasos del pipeline descargan la última versión estable del código del proyecto y crean un entorno virtual que hace uso del las librerías correctas. 

Los siguientes pasos ejecutan uno a uno los comandos definidos anteriormente, cargando así en la base de datos los datos provenientes de las distintas fuentes (en este caso excels) y procesando su vista minable. El proceso se realiza de forma ordenada para las 25 parcelas de muestra con las que estamos trabajando, remarcamos que el proceso tiene una alta escalabilidad debido a que podemos reproducir aquellos 'stages' necesarios en los momentos que nos interese. Es decir, podemos comenzar con un pipeline para insertar la información de 25 parcelas, pero posteriormente podríamos añadir más pasos a medida que dispongamos de más información. Por otra parte, la infraestructura como código que conseguimos posibilita definir el flujo concreto que un cliente puede tener con la aplicación. 

```jenkins

pipeline {
    agent any

    stages {
        stage('git') {
            steps {
                git url: '/home/vagrant/agrai/.git'
            }
        }
        stage('env') {
            steps {
                sh('python3.10 -m venv ./tfg_venv')
                sh('. ./tfg_venv/bin/activate')
                sh('pip install -r ./unix-dep/requirements.txt')
                sh('pip install --upgrade numpy')
            }
        }
        stage('migrate')
        {
           steps {
                sh('python3.10 manage.py makemigrations core')
                sh('python3.10 manage.py migrate')
                sh('python3.10 manage.py flush --no-input')
            }
       }    
        stage('qgis') {
            steps {
                sh('python3.10 manage.py 1-load-qgis --parcelas "data/parcelas/25/parcelas.shp" --pixels "data/parcelas/25/pixeles.shp" ')
            }
        }
        stage('parcela') {
            steps {
                sh('python3.10 manage.py 2-load-parcela-data -xls "data/excels/datos-test-2.xls" ')
            }
        }
	stage('cultivos') {
            steps {
                sh('python3.10 manage.py 3-load-cultivos -xls "data/excels/datos-test-2.xls" ')
            }
        }
        stage('indices') {
            steps {
                sh('python3.10 manage.py 4-download_img -a "20220601" -b "20220701" -p "data/parcelas/25/pixeles.shp" -i ndvi ndre' )
            }
        }
        stage('vista') {
            steps {
                sh('python3.10 manage.py 5-load_range')
            }
        }
    }
}

```

Además de este último, podemos crear varios entornos con tuberías diferentes que den como resultado bases de datos con estados distintos. Como mencionábamos anteriormente, esto es muy útil debido al funcionamiento del equipo en relación con el procesamiento de datos con varios clientes. La aplicación puede trabajar con instancias diferentes de la misma base de datos dependiendo del proyecto en el que se encuentre; por ejemplo, la misma instancia de la BD sirve tanto para una bodega con variedades de vino como para una cooperativa que contempla varios cultivos como guisantes, olivas, peras, etc. Por ello, definir scripts como el anterior utilizando los mismos comandos con distintas fuentes de datos es una forma clara y ordenada de automatizar los procesos.