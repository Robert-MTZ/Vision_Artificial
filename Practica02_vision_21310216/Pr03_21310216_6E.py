
import cv2
import numpy as np

def clasificador_croma (imagen,titulo_imagen): #Funcion para el clasificador y guardar la imagen correspondiente
    #Se mapea la imagen para poder clasificar cada pixel conrespecto a los valores de RGB obtenidos
    m,n,c = imagen.shape 
    imagen_clas=np.zeros((m,n))
    for x in range (m):
        for y in range (n):
            if 13<imagen[x,y,0]<85 and imagen[x,y,1]<100 and imagen[x,y,2]<220:
                imagen_clas[x,y]=255
                    

    cv2.imshow(titulo_imagen,imagen_clas) # se mueatra la imagen
    cv2.imwrite(titulo_imagen+".jpg",imagen_clas) # Se guarda la imagen producto
    return imagen_clas

def cromatico(imagenc,s,crom): #Funcion para crear el cromatico de cada imagen
    imagen = cv2.imread(s)
    m,n,c = imagen.shape
    imagenc = imagen.copy()
    imagenc = imagenc.astype(np.float32)
    imagen = imagen.astype(np.float32)
    for x in range(m):
        for y in range (n): #Se procesa la imagen 
            imagenc[x,y,0] = imagen[x,y,0]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
            imagenc[x,y,1] = imagen[x,y,1]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
            imagenc[x,y,2] = imagen[x,y,2]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])

    cv2.imshow(crom,imagenc)# Se muestra la imagen
    imagenc = cv2.normalize(imagenc, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U) #Se normaliza la imagen papra poder ser guardada
    cv2.imwrite(crom+".png",imagenc)#Se guarda la imagen con respecto a los valores ingresados
    return imagenc

#-----------SE CREAN LAS IMAGENES CON DIFERENTE OPACIDAD-----------
imagen_original = cv2.imread("manos.jpg")

imagen_opaca_1 = imagen_original.copy()
imagen_opaca_2 = imagen_original.copy()

cv2.imshow("Imagen Original",imagen_original)

imagen_opaca_1 = imagen_original.astype(np.float32)
imagen_opaca_2 = imagen_opaca_2.astype(np.float32)

imagen_opaca_1 = imagen_opaca_1*0.7 #se multiplica por un fator para modificar su nitidez o exposicion
imagen_opaca_1 = imagen_opaca_1.astype(np.uint8) #Al multiplicar por el numero flotante se convierte en flotante
cv2.imshow("mano obscura 1",imagen_opaca_1) #Se muestra la nueva imagen oscura
cv2.imwrite("imagen_opaca_01.jpg",imagen_opaca_1)

imagen_opaca_2 = imagen_original*0.3
imagen_opaca_2 = imagen_opaca_2.astype(np.uint8)
cv2.imshow("mano obscura 2",imagen_opaca_2) #Se muestra la nueva imagen oscura
cv2.imwrite("imagen_opaca_02.jpg",imagen_opaca_2)

imagen_croma_1 = imagen_original.copy()
imagen_croma_2 = imagen_opaca_1.copy()
imagen_croma_3 = imagen_opaca_2.copy()

#------Se crean las imagenes cromaticas a partir de la imagen origen y las imagenes con diferente opacidad
imagen_croma_1 = cromatico(imagen_original,"manos.jpg","imagen_cromatica01")
imagen_croma_2 = cromatico(imagen_opaca_1,"imagen_opaca_01.jpg","imagen_cromatica02")
imagen_croma_3 = cromatico(imagen_opaca_2, "imagen_opaca_02.jpg","imagen_cromatica03")

# #------Se somete a clasificador las imagenes cromaticas-------
imagenc = clasificador_croma(imagen_croma_1,"clasificador_cromatico_01")
imageno1 = clasificador_croma(imagen_croma_2,"clasificador_cromatico_02")
imageno2 = clasificador_croma(imagen_croma_3,"clasificador_cromatico_03")

cv2.waitKey(0)
cv2.destroyAllWindows()


