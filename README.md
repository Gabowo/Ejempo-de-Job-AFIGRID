# Ejempo-de-Job-AFIGRID
Cancel changes
Dentro de este repositrio estan todos los archivos necesarios para enviar un job en que se lee un archivo y se crea uno nuevo.

En primer lugar necesitamos nuestro script a ejecutar, en este caso el archivo `python_test.py`. `python_test.py` tiene 2 objetivos, primero lee el contendido de un archivo `test_file.txt` e imprime el contenido en la consola, luego escribe un nuevo archivo `new_test.txt`.

A contiuacion hemos de escribir un archivo de consola (.sh) en el cual le damos las instrucciones de consola a ser ejecutadas en el cluster. En el caso de este ejemplo, dicho archivo es el llamado `testing_jobs.sh`.

Finalmente, hemos de crear nuestro archivo .xrsl, este es el archivo que le indica al cluster que archivos debe ejecutar, cuales debe guardar, etc. En el caso de este ejemplo, este archivo es llamado `testing_jobs.xrsl`. 

Como se puede apreciar en `testing_jobs.xrsl`, todo archivo .xrsl parte con el caracter "&". Por otro lado, notamos que hay una lista de instrucciones que se dan al cluster. Primero esta "executable"
