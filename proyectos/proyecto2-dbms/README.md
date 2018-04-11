# README

Este proyecto contiene gramáticas de ejemplo y de SQL para ser utilizadas como parte
del proyecto #2 del curso de bases de datos UVG CC3057.

Las gramáticas (archivos .g4) fueron utilizadas de base para constuir *lexers* y *parsers* utilizando
[ANTLR](http://www.antlr.org/). Los lenguajes de salida disponibles son Python2 y Python3.

El proyecto contiene también un ejemplo sencillo de *parser* y *lexer* para [una gramática
de prueba](hello-python2/Hello.g4), así como ejemplos de cómo utilizar estas clases
con un archivo de entrada o con lectura directamente de la consola.

La ejecución de estos ejemplos requiere la instalación de los *runtimes* para Python 2
o Python 3:

* https://pypi.python.org/pypi/antlr4-python2-runtime/
* https://pypi.python.org/pypi/antlr4-python3-runtime/

Los archivos tests.sql y false-tests.sql contienen queries que son correcta e incorrectamente
procesados por las clases generadas, a manera de validación.

## Referencias

De acuerdo con [esto](https://tomassetti.me/parsing-in-python/#tools), los **visitors**
son útiles cuando es necesario manipular o interactuar con el [CST](https://en.wikipedia.org/wiki/Parse_tree)
generado por durante el *parsing* del *input*.

Por otro lado los **listeners** son útiles cuando simplemente se quiere realizar una
acción a partir del *matching* de una regla.

Algunos 

## Generación de código Python 2 y 3

Tomado de from: https://github.com/antlr/antlr4/blob/4.7.1/doc/python-target.mmd

```
antlr4 -Dlanguage=Python2 MyGrammar.g4

antlr4 -Dlanguage=Python3 MyGrammar.g4
```


