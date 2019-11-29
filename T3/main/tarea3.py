import cv2
import numpy as np

if __name__== '__main__':
    
    img1 = cv2.imread('../img/caso_1/1a.jpg')
    img2 = cv2.imread('../img/caso_1/1b.jpg')

    gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    #creacion de un objeto de tipo SIFT
    sift = cv2.xfeatures2d.SIFT_create()

    #Detects keypoints and computes the descriptors
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    pts = np.array(cv2.KeyPoint_convert(kp1))
    
    #imagenes con los keypoints y sus respectivas orientaciones
    img_whit_kp1 = cv2.drawKeypoints(gray1,kp1, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img_whit_kp2 = cv2.drawKeypoints(gray2,kp2, img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    #Match de descriptores de puntos de interes
    bf = cv2.BFMatcher()
    matches = bf.match(des1,des2)
    #ordenamos de menor a mayor las distancias 
    matches = sorted(matches, key = lambda x:x.distance)
    n_kp = len(matches)
    #para tener una buena muestra, y que no aparezcan todos los kp
    N = int(n_kp * 0.25) 
    matching = cv2.drawMatches(gray1, kp1, gray2, kp2, matches[:N], None, flags=2)

    #Se guardan las imagenes de salida
    cv2.imwrite("../img_out/sift_kp1.jpg", img_whit_kp1)
    cv2.imwrite("../img_out/sift_kp2.jpg", img_whit_kp2)
    cv2.imwrite("../img_out/matching.png", matching)

    

    

    



    

    

