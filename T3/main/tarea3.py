import cv2
import numpy as np

if __name__== '__main__':
    
    img1 = cv2.imread('../img/caso_3/3a.jpg')
    img2 = cv2.imread('../img/caso_3/3b.jpg')

    gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    """
    xfeatures2d.SIFT_create()
    creacion de un objeto de tipo SIFT
    """
    sift = cv2.xfeatures2d.SIFT_create()
    """
    sift.detect()
    funcion que encuentra los keypoints en la imagen.

    Cada keypoint es una estructura especial que contiene muchos atributos
    como sus coordenadas (x,y), el tamaño significativo del vecindario, el
    angulo que especifica la orientacion, etc.
    """
    kp1 = sift.detect(gray1)
    kp2 = sift.detect(gray2)

    #kp, des = sift.compute(gray, kp)
    """
    cv2.drawKeypoints() dibuja los pequeños ciorculos donde se ubican 
    los keypoints.
    DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS es una flag que dibujará 
    un círculo con el tamaño del keypoint e incluso mostrará su orientación
    """
    img_whit_kp1 = cv2.drawKeypoints(gray1,kp1, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img_whit_kp2 = cv2.drawKeypoints(gray2,kp2, img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite("..\imgOut\sift_kp1.jpg", img_whit_kp1)
    cv2.imwrite("..\imgOut\sift_kp2.jpg", img_whit_kp2)



    

    

