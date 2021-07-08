# Desarrollador Backend

## Fases del desarrollo de este proyecto.

#### 1. Requerimientos:
- Crear un sistema en Python que cargue la información de un Excel en una base de datos, posteriormente obtener la información en un JSON a través de un servicio REST.
- Se deben de poder cargar Excels de diferentes estructuras.
- Se pueden tener varios formatos de salida.
- El servicio REST debe recibir dos parametros el Excel y el formato de salida.
- Todo debe ir encapsulado en un contenedor Docker y listo para ejecutarse con docker-compose.

#### 2. Definición de las tareas y las iteraciones:
##### 2.1 Investigación de las tecnologías que desconozco
- ¿Qué es Docker y cómo se utiliza? :ok:
- ¿Cómo encapsulo un proyecto? :ok:
- ¿Qué es docker-compose y como se utiliza? :ok:
- ¿Cómo leo un Excel y extraigo su información en Python? :ok:
- ¿Cómo configuro y encapsulo un proyecto Django en Docker? :ok:

##### 2.2 Configuración del proyecto en Docker
- Crear los archivos Dockerfile, docker-compose y requirements.txt :ok:
- Crear el proyecto Django :ok:
- Configurar el proyecto Django para usar PostgreSQL :ok:

##### 2.3 Crear la página web para cargar el Excel
- Crear una plantilla básica para cargar el Excel y leer su información.
- Crear una plantilla que permita seleccionar el formato de salida de la información.

##### 2.4 Leer un archivo Excel y guardar la información
- Crear el método que se encargará de leer el archivo Excel
- Guardar la información del Excel en la base de datos.
- Comprobar su funcionamiento

##### 2.5 Creación del servicio REST
- Crear el método que reciba los 2 parametros necesarios.
- Obtener la información correcta en el formato requerido.
- Comprobar que funcione para cualquier estructura de Excel

##### 2.6 Encapsular el proyecto
- Encapsular el proyecto con Docker.
- Verificar que funcione como fue solicitado usando docker-compose.
