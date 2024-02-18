# Ambiente de apoyo al aprendizaje de estructuras de datos
## Guia de Instalación
1. Descargue el repositorio en su computador
2. Ingrese desde Visual Studio Code a la carpeta principal del proyecto
3. Instale todas las dependencias necesarias. Para esto, en la terminal ejecute el siguiente comando:
_pip install -r requirements.txt_
4. Ingrese al archivo _ComponenteVisual.ipynb_ y ejecute todas las celdas. Al final del notebook encontrará la interfaz visual.

## Manual de Usuario
1.	Para cargar una estructura de datos, ingresar al Tab de la estructura que desea añadir y seleccionar la opción de carga. Esto abrirá un explorador de archivos en el cual debe seleccionar su implementación de la estructura. Si solo desea visualizar el comportamiento de una estructura de referencia puede ingresar desde el explorador de archivos a la carpeta del proyecto y ahí encontrará los archivos: 
* arbol_disc.py
* grafo_disc.py
* lista_dics.py

**Nota:**
Si se encuentra haciendo uso de la librería DISClib [1] esta librería se debe encontrar dentro de la carpeta del proyecto (el proyecto ya la incluye) pero para poder cargar una estructura de datos debe hacerlo mediante los archivos
* arbol_disc.py
* grafo_disc.py
* lista_dics.py

Que permiten la compatibilidad de la librería DISClib y el proyecto. Por tanto, si desea hacer cambios sobre la librería DISClib debe hacerlos desde la carpeta del proyecto.

2.	Si la estructura se cargó correctamente, ya puede empezar a hacer uso del aplicativo. Recuerde que si va a cambiar de una estructura a otra debe efectuar nuevamente la cargar del archivo .py de dicha estructura.

**IMPORTANTE:** No modifique los archivos de la carpeta referencias, ni de los archivos ComponenteVisual.ipynb, config.py y requirements.txt

Librería DISClib tomada de https://github.com/ISIS1225DEVS/ISIS1225-Lib/tree/main/DISClib
