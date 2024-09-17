from PIL import Image
import numpy as np

#Cargar el path de la imagen
image_path = '7.jpeg'

# Cargar la imagen
img = Image.open(image_path)

# Convertir la imagen a una matriz numpy y obtener los valores RGB
img_data = np.array(img)
rgb_data = img_data[:, :, :3]  # Obtener solo los canales RGB

# Crear el canal W (blanco) como el promedio de los valores RGB
rgbw_data = np.mean(rgb_data, axis=2, keepdims=True)
rgbw_data = np.concatenate((rgb_data, rgbw_data), axis=2)

# Imprimir la matriz RGBW en consola
print("Matriz RGBW:")
print(rgbw_data)

# Convertir la matriz a una cadena
matriz_str = '\n'.join(' '.join(map(str, fila)) for fila in rgb_data)

# Guardar los datos en un archivo de texto
with open("image_matrix.txt", "w") as file_convert:
    file_convert.write(matriz_str)