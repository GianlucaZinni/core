# Proyecto Votechain

¡Bienvenido al Proyecto Votechain! Este proyecto es una aplicación que simula un servicio de votación electrónica segura.

## Instalación del entorno

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/GianlucaZinni/core
    ```

2. Navega al directorio del proyecto Votechain CORE:

    ```bash
    cd core
    ```

3. Crea un entorno virtual (se recomienda utilizar `venv`):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    En Windows desde CMD
    ```bash
    .\venv\Scripts\activate
    ```

    En Linux/macOS
    ```bash
    source venv/bin/activate
    ```

4. Instala las dependencias del proyecto desde el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```



## Configurar la aplicación
En la carpeta principal `Project` se encuentra el archivo `.env` que contiene las variables a modificar:

`DATABASE_URI`

`MYSQL_HOST`

`MYSQL_USER`

`MYSQL_PASSWORD`

## Iniciar la aplicación

Una vez que el entorno esté configurado, puedes iniciar la aplicación, la cual se encargará de generar y llenar las bases de datos, 
además de iniciar el servicio de Core. 

Para iniciar la aplicación, dentro del *venv* navega al directorio del proyecto /Project

```bash
(venv) cd Project
```


Y luego, ejecuta el siguiente comando:

```bash
(venv) uvicorn main:votechain_app --reload
```
