# README

Este ejemplo presenta una gramática con una sola producción (*parsing rule*) y la
definición de dos *tokens* (*lexer rules*).

La generación de código a partir de esta gramática utilizando ANTLR tuvo como resultado
la creación de las clases `HelloLexer.py`, `HelloListener.py` y `HelloParser.py`.

El archivo `main.py` ejemplifica la forma de utilizar estas clases para procesar
un archivo de entrada definido mediante la ejecución en línea de comando:

```
python main.py archivo-de-entrada.txt
```

Adicionalmente, la clase `TestListener.py` muestra un ejemplo de cómo constuir e
involucrar una clase que realiza una acción concreta cuando se visita una producción.

Finalmente `cli.py` muestra un ejemplo de lectura de comandos a partir de la consola,
en donde verifica que la sintaxis recibida sea o no válida.
