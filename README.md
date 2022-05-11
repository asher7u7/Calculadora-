# CALCULADORA BÁSICA CON MENÚ

Una calculadora básica se puede realizar con condiciones. Se desea realizar alguna de las operaciones basicas con dos números "x, y". Además se desa calcular la potencia y el logaritmo. Se deben considerar los casos donde "y = 0" donde la division "x/y" NO se puede realizar y cuando "x <= 0" donde no se puede calcular el "log(x)". Se desea generar un menú para que el usuario pueda seleccionar la operacion a realizar, Una manera de hacerlo es la siguiente :

1. Se reciben los dos números "x, y" para realizar la operación.
2. Se recibe la operacion a realizar mediante la variable "opcion" la que selecciona en el menú que operación ejecuta el algoritmo.
3. Se inicializa la variable logica "bandera = False". Si la división o el algoritmo no se pueden calcular, se hace "bandera = true".
4. Mediante condiciones se realiza la operacion deseada.
    * En el caso de la división, si "y = 0", NO se puede realizar la división, se muestra un mensaje y se hace "bandera = True".
    * En el caso del logaritmo, si "x <= 0", NO se puede calcular el logaritmo, se muestra un mensaje y se hace "bandera = True".
5. Se muestra el resultado en el caso en que "bandera = False".

*Tomado de: Python con aplicaciones a las matematicas, ingenieria y finanzas.Cervantes O, Baez D.*