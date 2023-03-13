## Getting Started

Las siguientes instrucciones premiten obtener una copia del proyecto y poder correrlo localmente para desarollo de nuevas funcionalidades o testing.

### Consideraciones solicitadas del challenge
> - Se utilizo selenium con python para la realizacion del proyecto
> - A su vez se añadio la libreria de pytest_bdd para el uso de gherkin 
> - La version de python utilizada es la 3.9.7
> - Las demas versiones referidas a las librerias utilizadas estan dentro del archivo requirements.txt
> - Las pruebas se diseñaron bajo el sistema operativo Windows
> - Se utilizo el browser Chrome en la version 109.0.54..

### Consideraciones extras y Prerequisitos para ejecutar el proyecto

> #### Python 
>
> - Tener descargada la última version de Python.
> - Instalar Python y setear las variables de entorno.
> - Verificar que se haya instalado correctamenete con *python --version* desde cualquier consola/terminal (PowerShell, CMD, bash).

> #### Entorno virtual de Python
>
> - Ubicado desde una consola en la raíz del proyecto, ejecutar el siguiente comando:
> ```
> python -m venv .venv
> ```
> - Al finalizar, se debería haber creado una carpeta con nombre ".venv" la raíz del proyecto.
> - Para acitvar el entorno virtual, ejecutar el siguiente comando:
> -- En Linux bash/zsh -> ``` $ source .venv/bin/activate ```
> -- En Windows cmd.exe -> ``` .\.venv\Scripts\activate.bat ```
> -- En Windows PowerShell -> ``` .\.venv\Scripts\Activate.ps1 ```

> #### WebDriver 
>
> - Se necesitan descargar los WebDrivers para poder ejecutar los test localmente.
> - Descargar el WebDriver que soporte la versión del browser instalado. 
>   - [ChromeDriver](https://chromedriver.chromium.org/downloads)
> - Crear una carpeta llamada *drivers* en la raíz del proyecto, y guardar los ejecutables *.exe* dentro de esta.

### Instalación
>
> #### Python Libs
> - Es necesario instalar en el proyecto los módulos/librerías que se usan como dependencias desde el archivo *requirements.txt*.
> ```
> PS C:\Users\you_user\you_workspace\project_name> pip install -r requirements.txt
> ```
> - Finalizada la instalación, se puede verificar la instalación de las librerias con el comando *pip freeze*

## Ejecución de tests
> El framework está basado en *pytest*, por lo que las distintas formas de ejecutar los test. Para ejecutar un test específico se debe correr el siguiente comando:
> ```
> python -m pytest -s --alluredir=report ./src/steps/xxxxx.py
> ```

> #### Allure 
> Se necesita instalar Allure en el sistema.
> - Ingresar a [allure release](https://github.com/allure-framework/allure2/releases/).
> - Descargar la versión zip: **2.13.3**.
> - Descomprimir en el directorio que prefieras
> - Agregar la carpeta *bin* de allure a las Variables de Entorno *PATH*.
> - Verificar la instalación de Allure ejecutando el comando *allure --version* desde cualquier consola/terminal.

### Reporte Allure
> Para acceder al reporte allure se debe utilizar el siguiente comando:
> ```
> allure serve .\report\
> ```
> **Advertencia:** el directorio donde se busca el reporte con el comando anterior, debe coincidir con el especificado en el comando con el que se ejecutó el script del test.