
Hacemos uso de Vagrant para crear en una máquina virtual Unix (Ubuntu), el entorno de desarrollo necesario para el proyecto. De esta forma conseguimos que los entornos de pruebas y producción sean muy similares, permitiendo automatizar el despliegue de la aplicación mediante técnicas de infraestructura como código. Una de las ventajas de tener una máquina Ubuntu, es que, mediante scripts .sh, instalamos todas las dependencias necesarias para dejar dicha máquina lista para el despliegue de la aplicación.

Para el entorno de desarrollo virtualizamos con Vagrant una una máquina Ubuntu 20.04. El archivo *Vagrantfile* nos permite provisionarla con el código del proyecto y el script que deja a dicha máquina con las librerías necesarias para el correcto funcionamiento de este.

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

El primero de los entregables, 'start.sh', hace referencia a esta parte del proceso. El siguiente script automatiza la creación de una máquina con las librerías necesarias, el cual, una vez ejecutado, deja dicha máquina lista para el despliegue de la aplicación.

```bash

#!/bin/bash
sudo rm -f /etc/apt/trusted.gpg.d/postgresql.gpg
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

sudo apt update
sudo apt upgrade -y

sudo apt install -y postgresql-14 
sudo apt install -y postgresql-14-postgis-scripts

sudo service postgresql start

sudo -u postgres createuser agrai_user
sudo -u postgres createdb -O agrai_user agrai_db
sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" agrai_db
sudo -u postgres psql -c "ALTER USER agrai_user PASSWORD 'password';"

# gdal native:
sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
sudo apt-get update

sudo apt autoremove -y python3

# python repositories

sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa

# python concrete installation

sudo apt install -y python3.10 # version concreta 
sudo apt install -y python3.10-dev python3.10-venv
sudo apt install -y virtualenv
sudo apt install -y build-essential
sudo apt install -y python3.10-tk

# python env var

export PYTHONPATH="/usr/local/bin/python3.10:/usr/local/lib/python3.10/lib-dynload:/usr/local/lib/python3.10/site-packages"
alias py=python3.10
alias python=python3.10
alias python3=python3.10

#Tkinter
sudo apt install -y python3-tk

# GDAL
sudo apt install -y libgdal-dev
sudo apt install -y gdal-bin

# env gdal lib variables
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

```

