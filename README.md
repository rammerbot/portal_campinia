##### Español:
### Portal Apacuana, La campiña  
<div align="center">
<img src="https://raw.githubusercontent.com/rammerbot/files/main/Captura%20de%20pantalla%202024-05-26%20182134.png?token=GHSAT0AAAAAACRF553ITT3OAW27XXQSAYOMZSTW2GQ" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Portal de la comunidad la campiña, Bolivar, Venezuela</div>  
  #### Descripcion.
  
> El portal web Apacuana es una pagina dinamica de actualidades e informacion sobre las actividades de la comunidad 'La Campiña' el cual tambien cuenta con formulario para presentar inquietudes y mensajes de propuestas o solicitudes, con un panel administrativo para colocar las noticias de manera facil y sencilla.

#### Características
- Presentar a la comunidad informacion reciente de los eventos en la comunidad.
- Presentar a los dirigentes de la comunidad.
- Listar las actividades que estan proximas a presentarse.
- Formulario de contacto para mensajes.
- Direccion en google map.
- panel administrativo.
- cuenta de administradores.

#### Instalación

##### Crear entorno virtual:
```
python -m venv portal_campinia
```

##### Entrar en el entorno
```
cd portal_campinia
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd portal_campinia/Script
```
```
activate
```
> en Lunix:
```
source portal_campinia/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/portal_campinia.git
```

> Navegar al directorio del proyecto:

```
cd portal_campinia
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## Caja System
<div align="center">
<img src="https://raw.githubusercontent.com/rammerbot/files/main/Captura%20de%20pantalla%202024-05-26%20182134.png?token=GHSAT0AAAAAACRF553ITT3OAW27XXQSAYOMZSTW2GQ" align="center" style="width: 100%" />
</div>  
<div align="center">System for Centralizing Daily Report Flow</div>

 ### Description
 
 > The Apacuana portal is a dynamic web for news and informations about the activities of the 'La Campiña' comunity. It also includes a form to sumit concerns and messages for proposals or requests, along with an administrative panel to post news easily and simply.

#### Features

- Present recent information about comunity events.
- Introduce the comunity leaders.
- List upcoming activities.
- Conctact form for messages.
- Address from Google Maps.
- Administrative panel.
- Administrator account.
  
#### Installation
#### Create a virtual environment:

```
python -m venv portal_campinia
```

#### Enter the environment
```
cd portal_campinia
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd portal_campinia/Scripts
```
```
activate
```
> Linux:
```
source portal_campinia/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/portal_campinia.git
```

> Navigate to the project directory:

```
cd portal_campinia
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
