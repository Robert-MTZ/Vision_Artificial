import cv2
import numpy as np

def clasificador_color (imagen,titulo_imagen):# Se crea la funcion de clasificador
    #Se mapea la imagen para poder clasificar cada pixel conrespecto a los valores de RGB obtenidos
    #191,94,88
    #231,117,137
    #211,92,93
    m,n,c = imagen.shape
    imagen_proc=np.zeros((m,n))

    for x in range (m):
        for y in range (n):
            if 20<imagen[x,y,0]<200 and imagen[x,y,1]<200 and imagen[x,y,2]<255:
                imagen_proc[x,y]=255
                    
    cv2.imwrite(titulo_imagen+".jpg",imagen_proc)
    cv2.imshow(titulo_imagen,imagen_proc)
    return imagen_proc

def clasificador_whitepatch (imagen,titulo_imagen):# Se crea la funcion de clasificador
    #Se mapea la imagen para poder clasificar cada pixel conrespecto a los valores de RGB obtenidos de las imagenes generadas por white patch
    #218,180,168
    #192,135,98
    #236,191,171
    #241,206,186
    #237,223,224
    m,n,c = imagen.shape
    imagen_proc=np.zeros((m,n))

    for x in range (m):
        for y in range (n):
            if 50<imagen[x,y,0]<210 and imagen[x,y,1]<220 and imagen[x,y,2]<245:
                imagen_proc[x,y]=255
                    
    cv2.imwrite(titulo_imagen+".jpg",imagen_proc)
    cv2.imshow(titulo_imagen,imagen_proc)
    return imagen_proc

def white_patch (imagen,titulo_imagen): # Se crea la funcion de white patch para realizar el balanceo de blancos en la imagenes procesada
    imagen_LAB = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB)
    avg_a = np.average(imagen_LAB[:,:,1])
    avg_b = np.average(imagen_LAB[:,:,2])
    imagen_LAB[:,:,1] = imagen_LAB[:,:,1] - ((avg_a - 128)*(imagen_LAB[:,:,0]/255.0)*1.2)
    imagen_LAB[:,:,2] = imagen_LAB[:,:,2] - ((avg_b - 128)*(imagen_LAB[:,:,0]/255.0)*1.2)
    balanced_image = cv2.cvtColor(imagen_LAB, cv2.COLOR_LAB2BGR)
    cv2.imshow(titulo_imagen, balanced_image)
    cv2.imwrite(titulo_imagen+".jpg",balanced_image)
    return balanced_image

def RGB (imagen,titulo_imagen,coordenada): #funcion para crear las imagenes con diferentes tonalidades RGB
    imagen[:,:,coordenada] = imagen[:,:,coordenada]*0.75

    cv2.imshow(titulo_imagen, imagen)
    cv2.imwrite(titulo_imagen+".jpg",imagen)
    return imagen

imagen_original =cv2.imread("manos.jpg")

imagen_color1 = imagen_original.copy()
imagen_color2 = imagen_original.copy()
imagen_color3 = imagen_original.copy()

#-------- Se crean las imagenes con ganancias RGB--------
cv2.imshow("imagen original",imagen_original)
imagen_color1 = RGB(imagen_color1,"imagen_G",0)
imagen_color2 = RGB(imagen_color2,"imagen_R",1)
imagen_color3 = RGB(imagen_color3,"imagen_B",2)


#------ Se procesan las imagenes RGB con el white patch
imagen_blanco_01 = white_patch(imagen_original,"White_Patch_imagen_original")
imagen_blanco_02 = white_patch(imagen_color1,"white_patch_imagen_G")
imagen_blanco_03 = white_patch(imagen_color2,"white_patch_imagen_R")
imagen_blanco_04 = white_patch(imagen_color3,"white_patch_imagen_B")

#----Se someten a clasificador las imagenes RGB
clasificador_color(imagen_original,"clasificador_original")
clasificador_color(imagen_color1,"clasificador_G")
clasificador_color(imagen_color2,"clasificador_R")
clasificador_color(imagen_color3,"clasificador_B")

# #----Se someten a clasificador las imagenes procesadas con white patch
clasificador_whitepatch(imagen_blanco_01,"clasificador_white_patch_01")
clasificador_whitepatch(imagen_blanco_02,"clasificador_white_patch_02")
clasificador_whitepatch(imagen_blanco_03,"clasificador_white_patch_03")
clasificador_whitepatch(imagen_blanco_03,"clasificador_white_patch_04")

cv2.waitKey(0)
