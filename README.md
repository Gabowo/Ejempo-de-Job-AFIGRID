# Ejempo-de-Job-AFIGRID
Cancel changes
Dentro de este repositrio estan todos los archivos necesarios para enviar un job en que se lee un archivo y se crea uno nuevo.

En primer lugar necesitamos nuestro script a ejecutar, en este caso el archivo `python_test.py`. `python_test.py` tiene 2 objetivos, primero lee el contendido de un archivo `test_file.txt` e imprime el contenido en la consola, luego escribe un nuevo archivo `new_test.txt`.

A contiuacion hemos de escribir un archivo de consola (.sh) en el cual le damos las instrucciones de consola a ser ejecutadas en el cluster. En el caso de este ejemplo, dicho archivo es el llamado `testing_jobs.sh`.

Finalmente, hemos de crear nuestro archivo .xrsl, este es el archivo que le indica al cluster que archivos debe ejecutar, cuales debe guardar, etc. En el caso de este ejemplo, este archivo es llamado `testing_jobs.xrsl`. 

Como se puede apreciar en `testing_jobs.xrsl`, todo archivo .xrsl parte con el caracter "&". Por otro lado, notamos que hay una lista de instrucciones que se dan al cluster. Primero está `executable` en donde debemos dar el path a nuestro archivo .sh, luego tenemos `jobName` que nos permite poner nombre a nuestro job para despues poder reconocerlo (al hacer `arcstat -a`, por ejemplo), `stdout` donde indicamos como se llamara el archivo en que se guardara el output de consola del job, `stderr` donde indicamos como se llamara el archivo en que se guardara el error de consola del job, `inputfiles` y `outputfiles` que nos permiten indicar que archivos son necesarios para la ejecucion del job (en este caso `test_file.txt`) y cuales son el output (en este caso `new_test.txt`), `memory` que nos permite indicar la cantidad de RAM que necesitaremos y `queue` donde indicamos a que nodo deseamos enviar el job.

Notese que `inputfiles` y `outputfiles` tienen 2 entradas en lugar de 1, esto es porque el primer path entregado es el path que el archivo tiene o tendra en el cluster, mientras que el segundo es el que tiene o tendra en el computador personal. En particular para `outputfiles` podemos dejar el segundo path vacio y esto hace que el archivo de llegada tenga el mismo path relativo que en el cluster.

Se puede apreciar en la carpeta `OutputEsperado` como se debe recuperar un archivo de output de consola (`testing_jobs.txt`), uno de error de consola (`testing_jobs.err`) y el archivo que se escribio con `python_test.py` (`new_test.txt`).
