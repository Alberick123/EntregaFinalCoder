# Curso Python: Proyecto Final
_**Objetivos generales:** En equipos (3 o 4 estudiantes, asignados por el tutor), se deberá crear una aplicación web libre, realizando todo lo explicado en los vivos por el docente y que este programada en Python utilizando Django. Esta web tendrá admin, perfiles, registro, páginas y formularios._

### _**Se debe entregar:**_

_Un video de menos de 10 minutos mostrando el correcto funcionamiento de la web._

_Se deberá entregar el link del repositorio de github con la última versión del proyecto. TODOS los integrantes del grupo deben tener algún commit en el proyecto._

_TODOS deberán entregar por la plataforma, ya que la performance en el github y la participación en el video pueden generar diferencias entre las notas de los integrantes._

_Observación: No se evalúa la estética de la web, solamente las funciones._

### _**Requisitos base:**_

_Los requisitos base serán parte de los criterios de evaluación para aprobar el proyecto._

* Inicio: Al momento de ingresar a la app en la ruta base '/'.
* Visualizar el home del blog.
* Poder listar todas las páginas, poder ver en detalle cada una, poder crear, editar o borrar contenido de las páginas.
* Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario está compuesto por: email - contraseña - nombre de usuario.
* Tener una app de login en el route accounts/login/ la cual permite loggearse con los datos de administrador o de usuario normal.
* Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen - nombre - descripción -  un link a una página web - email y contraseña
* Contar con un admin en route admin/ donde se puedan manejar las apps y los datos en las apps.

## Comenzando...

_Es necesario realizar una copia del repositorio del proyecto en tu maquina local con el propósito de realizar el testeo y la visualización de la página web._ 

_Para lograr esto puedes clonar el repositorio utilizando GIT, para más información puedes revisar el siguiente enlace: https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository_

### Requisitos para la visualización de los archivos de proyecto:

_Se recomienda el uso de un IDE (como por ejemplo **VSCode**) para la visualización de los elementos del proyecto. Además, se necesitará tener instalados en tu maquina local tanto Python como Django (puedes consultar el siguiente enlace para realizar estas instalaciones: https://tutorial.djangogirls.org/es/installation/#create-a-pythonanywhere-account)_

## Desarrollo del proyecto

_A grandes rasgos el proyecto fue implementado en segmentos por los miembros del grupo de trabajo. Dentro de las actividades realizadas por cada miembro son de destacar:_

* _Agustín Aguirre se encargo de la creación de modelos, vistas y sus urls asociadas y el CRUD de los modelos._
* _Alan Gon se encargo de la creación de los formularios, creación, edición y eliminación de perfiles._
* _Agusín Gutiérrez se encargo de los templates HTML, Login, Signup y Logout del sitio y la opción de mensajería._


## Pruebas de la web

_Una vez completados los pasos anteriores nos encontramos en condiciones de ejecutar en la consola de nuestro IDE (estando ubicados sobre el directorio de nuestro proyecto) el comando:_

```
python manage.py runserver
```

_Si se cumplieron correctamente todos los requisitos debería de generarse con normalidad una URL similar a la siguiente:_

```
Starting development server at http://127.0.0.1:8000/
```

_Abriendo dicha URL en nuestro navegador se debería de ver la página de inicio de nuestra web con un mensaje de bienvenida. El sitio web tiene como función registrar las disciplinas, estadios y jugadores de un club deportivo, permitiendo además visualizar, editar o borrar estos datos._

_En la parte superior se encuentra un menú que permite el acceso a las 3 páginas con los formularios que permiten cargar datos en la DB (Database) de los modelos. Los modelos son: 'Disciplinas', 'Estadio' y 'Plantel'. En este menú también se brinda la opción de login, la cual funcionara de forma dinámica, permitiendo logearnos o registrarnos en caso de no estar logueados o editar nuestro perfil y cerrar la sesión en caso de si estarlo. Se cuenta además en el menú un acceso al formulario de contacto con los administradores del sitio, en donde se desplegará una vista solicitando datos de contacto y se podrá redactar un mensaje._

_El requisito de logearse en el sitio se lleva a cabo para restringir el acceso a los usuarios. Cualquier usuario puede cargar un formulario pero solo aquellos que se encuentren loguaedos podrán ver el detalle de los valores cargados, editar estos valores o borrarlos. En caso de no haberse registrado nunca en el sitio se brinda la opción de llevar a cabo el registro para el usuario, donde deberá completar un formulario con información básica sobre él, luego de lo cual ya estará habilitado para registrarse en el sitio._

_Si se clickea en la opción de 'AppClub' ubicada en la parte superior izquierda se puede regresar a la página Home. Por otra en la parte inferior del sitio se agregaron los accesos con las opciones 'Privacidad · Términos de uso · FAQ · Sobre nosotros', las cuales redirigen a vistas en donde se detalla un aviso de privacidad integral, los términos y condiciones de uso del sitio, el repositorio de GitHub donde se detalla el funcionamiento del sitio y una pequeña descripción de la función del sitio y quienes son sus autores._

_Para acceder a las páginas de los formularios y cargar los datos en la DB de cada modelo con sus URLs se pueden utilizar también las siguientes direcciones:_

* Para Disciplinas: '/AppClub/disciplinas'.
* Para Estadio: '/AppClub/estadio'.
* Para Estadio: '/AppClub/plantel'.

_En cada una de las vistas de los formularios se encuentra un acceso para poder ver en detalle los valores cargados, editarlos o borrarlos, pero para acceder a estas secciones se solicitara al usuario que se encuentre logueado._

_La URL http://127.0.0.1:8000/admin permite el acceso al menú de control implementado por Django. Para poder acceder a esta opción será requisito indispensable contar con los datos de logueo de un superusuario._

## Archivos en el directorio del proyecto

_Dentro del directorio del proyecto es importante destacar los ubicados dentro del directorio AppClub. En este directorio se encuentra Templates, el cual contiene los archivos HTML para las vistas en el sitio web, se parte de un archivo base llamado 'base.html' y utilizando herencias de HTML se generan los archivos de cada vista del sitio

_En el directorio AppClub son de destacar los archivos 'views.py' y 'urls.py' que permiten el acceso a cada uno de los archivos HTML para cada vista del sitio web. En 'models.py' se define cada modelo y los elementos que lo forman, mientras que en 'forms.py' se declaran los formularios para cada clase. En el directorio 'Static' es almacenado todo lo relativo a CSS y JS para el funcionamiento de la página web. El último elemento a destacar en este directorio es 'forms.py' encargado de generar los formularios para la carga de datos de los modelos en la DB._

_La base de datos que almacena los datos generados con los formularios se encuentra en el directorio y se llama 'db.sqlite3'._

## Construido con:

_Para la implementación del sitio se trabajó con las siguientes herramientas informáticas:_

* Django - Framework de desarrollo web utilizado.
* VSCode - IDE utilizado.

## Autores:

_**Aguirre Agustín.**_
_**Gon Alan.**_
_**Gutiérrez Agustín.**_
