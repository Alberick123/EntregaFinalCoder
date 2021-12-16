# Entrega intermedia del proyecto final de Coderhouse
_**Objetivos generales:** Desarrollar una WEB Django con patrón MVT subida a GitHub._

_**Se debe entregar:**_

_Link de GitHub con el proyecto totalmente subido a la plataforma._

_Proyecto Web Django con patrón MVT que incluya:_

* Herencia de HTML.
* Por lo menos 3 clases en 'models'.
* Un formulario para ingresar datos a todas las clases de los 'models'.
* Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

## Comenzando...

_Es necesario realizar una copia del repositorio del proyecto en tu maquina local con el propósito de realizar el testeo y la visualización de la página web._ 

_Para lograr esto puedes clonar el repositorio utilizando GIT, para más información revisa el siguiente enlace: https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository_

### Requisitos para la visualización de los archivos de proyecto:

_Se recomienda el uso de un IDE (como por ejemplo **VSCode**) para la visualización de los elementos del proyecto. Además, se necesitará tener instalados en tu maquina local tanto Python como Django (puedes consultar el siguiente enlace para realizar estas instalaciones: https://tutorial.djangogirls.org/es/installation/#create-a-pythonanywhere-account)_

## Pruebas de la web

_Una vez completados los pasos anteriores nos encontramos en condiciones de ejecutar en la consola de nuestro IDE (estando ubicados sobre el directorio de nuestro proyecto) el comando:_

```
python manage.py runserver
```

_Si se cumplieron correctamente todos los requisitos debería de generarse con normalidad una URL similar a la siguiente:_

```
Starting development server at http://127.0.0.1:8000/
```

_Abriendo dicha URL en nuestro navegador deberíamos de ver un mensaje de error en nuestra pantalla con el mensaje 'Page not found (404)'._

_Si al final de la URL agregamos '/AppClub/inicio' veremos la pantalla de Home de la página con un mensaje que nos da la bienvenida._

_En la parte superior se encuentra un menú que permite el acceso a las 3 páginas con los formularios que permiten cargar datos en la DB (Database) de los modelos. Los modelos son: 'Disciplinas', 'Estadio' y 'Plantel'. Se cuenta además en el menú un acceso al formulario de contacto._

_Si se clickea en la opción de 'AppClub' ubicada en la parte superior izquierda se puede regresar a la página Home. Por otra En la parte inferior del sitio se agregaron los accesos con las opciones 'Privacy · Terms · FAQ' para ser implementadas en la entrega final del proyecto._

_Para acceder a las páginas de los formularios y cargar los datos en la DB de cada modelo con sus URLs se deben utilizar las siguientes direcciones:_

* Para Disciplinas: '/AppClub/disciplinas'.
* Para Estadio: '/AppClub/estadio'.
* Para Estadio: '/AppClub/plantel'.

## Archivos en el directorio del proyecto

_Dentro del directorio del proyecto es importante destacar los ubicados dentro del directorio AppClub. En este directorio se encuentra Templates, el cual contiene los archivos HTML para las vistas en el sitio web, se parte de un archivo base llamado 'base.html' y utilizando herencias de HTML se generan los archivos de cada vista del sitio los cuales son: 'incio.html', 'disciplinas.html', 'estadio.html' y 'plantel.html'._

_En el directorio AppClub son de destacar los archivos 'views.py' y 'urls.py' que permiten el acceso a cada uno de los archivos HTML para cada vista del sitio web. En 'models.py' se define cada modelo y los elementos que lo forman. El último elemento a destacar en este directorio es 'forms.py' encargado de generar los formularios para la carga de datos de los modelos en la DB._

_La base de datos que almacena los datos generados con los formularios se encuentra en el directorio y se llama 'db.sqlite3'._

## Construido con:

_Para la implementación del sitio se trabajó con las siguientes herramientas informáticas:_

* Django - Framework de desarrollo web utilizado.
* VSCode - IDE utilizado.

## Autores:

_Aguirre Agustín._
_Gon Alan._
_Gutiérrez Agustín._


