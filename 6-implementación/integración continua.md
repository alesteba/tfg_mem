Una vez hemos identificado los pasos atómicos que queremos ejecutar de forma secuencial, utilizamos la herramienta de integración continua, Jenkins, para ejecutar estos pasos de forma ordenada y ver poco a poco el proceso. 

El siguiente script reproduce el flujo de uso común de la aplicación desde su creación, pasando por todos los pasos de carga de datos en el modelo, hasta la vista minable sobre la cual se obtiene el modelo de producción de kg de cultivo. 

La ejecución del siguiente pipeline tiene lugar tras lanzar la máquina Vagrant sobre la que corre el proyecto. En el comienzo de la memoria habíamos hablado de que dicha máquina se provisiona con los scripts necesarios para instalar las dependencias del proyecto. En este punto con la máquina en dicho estado, los primeros pasos del pipeline descargan la última versión estable del código del proyecto y crean un entorno virtual que hace uso del las librerías correctas. 



Hablar de los varios pipelines posibles que puede contener el proyecto.

Carga consecutiva de múltiples datos: 

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


La integración en este punto ... genera el flujo completo del caso de uso convencional de la aplicación. 


podríamos repreducir el proceso con más pasos para seguir añadiendo datos al modelo relacional y recalcular la vista con solo ejecutar alguno de los pasos propuestos por el script en el momento adecuado.

imagen con el proceso ejecutado, --->

---> explicar algún paso concreto, 

---> relación directa con lo mostrado aneriormente: 
