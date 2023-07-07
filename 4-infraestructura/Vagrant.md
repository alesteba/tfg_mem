
Hacemos uso de Vagrant para crear, en una máquina virtual Unix (Ubuntu), el entorno de desarrollo necesario para el proyecto. De esta forma conseguimos que los entornos de pruebas y producción sean muy similares, permitiendo automatizar el despliegue de la aplicación mediante técnicas de infraestructura como código. Una de las ventajas de tener una máquina Ubuntu, es que, mediante scripts .sh, instalamos todas las dependencias necesarias para dejar dicha máquina lista para el despliegue de la aplicación.

Para el entorno de desarrollo virtualizamos con Vagrant una máquina Ubuntu 20.04. El archivo *Vagrantfile* nos permite provisionarla con el código del proyecto y el script que deja a dicha máquina con las librerías necesarias para el correcto funcionamiento de este.

```bash
Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-20.04"
  
  config.vm.provision "file", source: "~/Desktop/agrai", destination: "$HOME/"
  config.vm.provision :shell, :path => "start.sh"
  config.vm.provision :shell, :path => "jenkins.sh"

  config.vm.define "server" do |server|
      server.vm.network "private_network", ip: "192.168.56.19"
   	   server.vm.provider "virtualbox" do |vb|
		  vb.memory = "4096"
		  vb.cpus   = "2"
      end
  end
```

Se enlazan como entregables los dos scripts con los que provisionamos dicha máquina. El primero, 'start.sh', hace referencia a la instalación de las librerías necesarias, el segundo, instala la herramienta Jenkins para la posterior ejecución de tareas dentro de un pipeline. A continuación mostramos algunas de las dependencias que más ha costado que funcionen conjuntamente.

```bash

#!/bin/bash
sudo apt install -y postgresql-14 
sudo apt install -y postgresql-14-postgis-scripts

# gdal native:
sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update

# python concrete installation
sudo apt install -y python3.10 # version concreta 
sudo apt install -y python3.10-dev python3.10-venv
sudo apt install -y virtualenv
sudo apt install -y build-essential
sudo apt install -y python3.10-tk

#Tkinter
sudo apt install -y python3-tk

# GDAL
sudo apt install -y libgdal-dev
sudo apt install -y gdal-bin

# env gdal lib variables
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

```

