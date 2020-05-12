# HISTOGRAM EQUALIZATION
La ecualizacion del histograma es un metodo en el procesamiento de imagenes de ajuste de contraste utilizando el histograma de la imagen.

##Archivos
Tenemos dos archivos `hitogram.py` y `subHist.py`, el primero toma una imagen y hace la ecualizacion del histograma tomando como refencia a toda la image;
el segundo archivo toma como refencia a una parte de la imagen, una subimagen, y aplica los valores obtenidos en Sn para toda la imagen.
Recomiendo usar la sub imagen para imagenes donde se quiera seraltar mas, una parte de la imagen y la otra cuando una imagen
es uniforme en contraste.

## Compilar
Antes de compilar debemos tener instalado `Python3.X`, `OpenCV`, `Matplotlib` y `Numpy`.
Tambien debemos editar el nombre de la imagen que recibira. 
### EN LINUX
Ejecutamos lo siguiente:
```bash
python histogram.py
python subHist.py

```

## Nota
Los archivos estan configurados para las imagenes en este repositorio por lo que si se desea usar otra imagen se deben cambiar valores.
