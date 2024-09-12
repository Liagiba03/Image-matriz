from PIL import Image
import numpy as np
import plotly.express as px

#Cargar el path de la imagen
image_path = '7.jpeg'

# Cargar la imagen
imagen = Image.open(image_path)

#Mostrar imagen
#fig = px.imshow(imagen)
#fig.show()

# Convertir la imagen a escala de grises (opcional, si quieres simplificar la matriz)
imagen_gris = imagen.convert('L')

# Convertir la imagen en una matriz de números
matriz = np.array(imagen_gris)

# Mostrar la matriz resultante
print(matriz)

# Guardar los datos en un archivo de texto

# Convertir la matriz a una cadena
matriz_str = '\n'.join(' '.join(map(str, fila)) for fila in matriz)

# Guardar los datos en un archivo de texto
with open("image_matrix.txt", "w") as file_convert:
    file_convert.write(matriz_str)


#Mostrar imagen ya convertida a matriz
#fig = px.imshow(matriz)
#fig.show()
