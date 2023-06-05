# El Comilón - Prototipo de Sistema de Restaurante

Este repositorio contiene el prototipo funcional del sistema de restaurante "El Comilón", desarrollado como parte de la asignatura de Ingeniería de Software.

## Descripción del proyecto

"El Comilón" es un sistema de restaurante diseñado para facilitar la gestión de pedidos y el control de inventario. Este prototipo presenta funcionalidades básicas como un catálogo de productos y un carrito de compras no funcionales. Además, incluye un sistema de autenticación y un panel de administración completamente funcional.
## Características

Catálogo de productos: Muestra una lista de los platos y bebidas disponibles en el restaurante.
Carrito de compras: Permite a los usuarios agregar productos al carrito, pero no realiza el proceso de compra.
Autenticación: Permite a los usuarios iniciar sesión y protege las funcionalidades del panel de administración.
Panel de administración: Permite a los usuarios administradores gestionar los productos, pedidos y usuarios del sistema.

# Vista previa

![catalogo restaurant](/Documentos/preview.gif)

## Tecnologías utilizadas

- Django: Framework de desarrollo web de alto nivel basado en Python.
- SQLite3: Base de datos liviana y fácil de usar utilizada para almacenar la información del sistema.

## Instalación y ejecución

1. Clona este repositorio en tu máquina local:

   > <code>git clone https://github.com/keaguirre/elComilon</code>

2. Navega al directorio del proyecto:

   > <code>cd elComilon</code>

3. Crea y activa un entorno virtual (opcional pero recomendado):

    > <code>python -m venv env</code><br>
    > <code>source env/bin/activate</code>

4. Instala las dependencias del proyecto:

    > <code>pip install -r requirements.txt</code>

5. Inicia el servidor de desarrollo:

    > <code> python manage.py runserver </code>

6. Accede al sistema en tu navegador web utilizando la URL: <br> 
    > [http://localhost:8000](http://localhost:8000)
## Contribución

Si deseas contribuir a este proyecto, sigue los siguientes pasos:

1. Haz un fork de este repositorio.
2. Crea una rama nueva para tu contribución:
    > <code>git checkout -b feature/nueva-funcionalidad</code>

3. Realiza tus cambios y realiza los commits:

   > <code>git add .</code><br>
   > <code>git commit -m "Descripción de tus cambios"</code>

4. Sube tus cambios a tu repositorio fork:

    > <code>git push origin feature/nueva-funcionalidad</code>

5. Abre un pull request en este repositorio para revisar tus cambios.