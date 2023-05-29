# **Proyect 0**
Nombres: 

Wilson Manuel Estrada Ortega, Codigo: 200098310

Maria Camila Osorno Suarez, Codigo: 200159249

Samuel Matiz García, Codigo: 200182687


## **Resumen**
En el ámbito empresarial y de las instituciones, la gestión de espacios disponibles se ha convertido en una problemática frecuente. Muchas empresas, negocios e instituciones desconocen la capacidad y el estado de las zonas disponibles para los usuarios, lo que implica un acceso poco eficiente, un mal manejo del espacio y la pérdida de oportunidades para aprovechar al máximo la infraestructura disponible.

En este sentido, surge la necesidad de crear una solución que permita gestionar y administrar los espacios disponibles de manera eficiente y sencilla. Con el objetivo de maximizar la ocupación y el aprovechamiento de las zonas disponibles por parte de los usuarios, se propone desarrollar una aplicación web con tecnologías especializadas en brindar información sobre ocupaciones en momento real.

La aplicación web permitirá a los usuarios ver la ocupación en distintos espacios de la empresa, y se enfocará en la Universidad del Norte como caso de estudio. Con esta solución, se espera resolver la problemática descrita y ofrecer una herramienta accesible y eficiente para la gestión de los espacios disponibles en empresas e instituciones. De esta manera, se podrán optimizar los procesos y mejorar la productividad de las empresas, y se ofrecerá a los usuarios una experiencia más satisfactoria en su acceso a los distintos espacios de la institución.



## **Funcionalidad**
Se implementó en Python Una pagina web para permitir ver a los usuarios la ocupación en distintos espacios de la empresa, asi como tener reportes de dichos lugares para el administrador de la aplicación. Se aplicaron conceptos de **Herencia, Encapsulación, Decoradores y Unit Test.**

## **UML**
![](https://github.com/wilsone24/Poo-Project/blob/main/UML.png)

## **Instrucciones**
1. Ingresar en el enlace del repositorio de Github: https://github.com/wilsone24/Poo-Project

2. Seleccionar la parte de code y copiar el HTTPS: https://github.com/wilsone24/Poo-Project.git

3. Ingresar a VsCode o desde gitBash y clonar el repositorio: git clone https://github.com/wilsone24/Poo-Project.git

4. Una vez dentro del codigo, crear una nueva terminal y ejecutar el siguiente comando: pip install -r "\requirements.txt", Este permitirá instalar todas las lirerias necesarias para el correcto funcionamiento del programa.

5. Abrir la carpeta src

6. Buscar el archivo app.py y ejecutarlo, o colocando en la terminal: python .\src\app.py

7. Una vez que se ejecute le aparecera donde se aloja el proyecto y esto mismo lo copiará en su navegador, por ejemplo: "http://127.0.0.1:5000"

### **Archivos y carpetas**

Una vez Clonado el repositorio se encontrará con 1 carpeta y 2 archivos, de los cuales si quiere verificar el codigo, clases, funcionalidades, entre otros aspectos, deberá ingresar a **src** y la clasificacion de las carpetas  y archivos es la siguiente:

1. **Capturas:** Se guardaran las capturas de las estadisticas de los sitios.

2. **database:** Guardara el archivo de bases de datos donde se encontrará todos los registros de la app.

3. **models:** Encontrará distintos archivos con clases necesarias para establecer los modelos en la aplicacion, acá se encontrará la clase user y todas las funciones que este puede hacer, asi como la clase admin.

4. **static:** Encontrará los archivos necesarios para cargar la pagina, tales como las imagenes, el css y el javascript.

5. **templates:** Encontrará todos los html usados para renderizar en las diferentes rutas.

6. **Unit tests:** Contiene Recursos necesarios para el correcto funcionamiento de las pruebas unitarias.

7. **app.py:** está contendrá el programa principal y permitirá ejecutar la aplicación.

8. **config.py:** Contiene Configuracion necesaria de la aplicación.

9. **correos.py:** Contiene Recursos necesarios para el correcto funcionamiento del envio de correos.

10. **Requirements.py:** Contiene todas las librerias necesarias para instalar la app.

### **Verificar Pruebas Unitarias**
Para Verificar las distintas pruebas unitarias que se le hicieron a las funciones unicamente se dirigirá a la carpeta **Unit tests** dentro de la carpeta **src**, entrara a los distintos archivos de pruebas que estan dentro de la carpeta y los ejecutará.

* El resultado de la prueba unitaria será mostrado en consola.
