# Roberto Martinez Bailon   Vision Artificial 
# 21310216 6E

import cv2 # importasmos la libreria cv2
import numpy as np # numpy as np se convierte  que convierte un archivo a un tipo de dato

def clasificador (imagen): # Creamos la funcion de clasificador
    m,n,c = imagen.shape # .shape es para que agarre el tamaño original de la imagen
    imagen_b=np.zeros((m,n))
    for x in range (m):
        for y in range (n):
            if 16<imagen[x,y,0]<180 and imagen[x,y,1]<170 and imagen[x,y,2]<240:
                imagen_b[x,y]=255
                    
    
    return imagen_b


imagen = cv2.imread("manos.jpg") #se guarda la imagen que elegimos en la variable imagen
imagen_b = clasificador(imagen)
cv2.imwrite("imagen_b1.jpg",imagen_b) # guardamos con imwrite
cv2.imshow("manos binarias",imagen_b) # mostramos resultado con imshow
cv2.imshow("Imagen OG mano", imagen) # mostramos resultado con imshow
cv2.waitKey(0) # espera la instruccion presionando x
cv2.destroyAllWindows() # se eliminan las ventanas

