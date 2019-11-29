import cv2
import numpy as np

if __name__== '__main__':
    
    img1 = cv2.imread('../img/caso_1/1a.jpg')
    img2 = cv2.imread('../img/caso_1/1b.jpg')

    gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#####################################################SIFT#######################################################
    #creacion de un objeto de tipo SIFT
    sift = cv2.xfeatures2d.SIFT_create()

    #Detects keypoints and computes the descriptors
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    pts = np.array(cv2.KeyPoint_convert(kp1))
    
    #imagenes con los keypoints y sus respectivas orientaciones
    img_whit_kp1 = cv2.drawKeypoints(gray1,kp1, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    img_whit_kp2 = cv2.drawKeypoints(gray2,kp2, img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

####################################################MATCHING####################################################  
    #Match de descriptores de puntos de interes
    bf = cv2.BFMatcher()
    matches = bf.match(des1,des2)
    #ordenamos de menor a mayor las distancias 
    matches = sorted(matches, key = lambda x:x.distance)
    n_kp = len(matches)
    #para tener una buena muestra, y que no aparezcan todos los kp
    N = int(n_kp * 0.25)
    matching = cv2.drawMatches(gray1, kp1, gray2, kp2, matches[:N], None, flags=2)

#####################################################RANSAC#####################################################
    #Como nuestro conjunto de KP son del tipo DMatch los transformamos a coordenadas
    #(x, y) para que sea mas facil rabajar (?)
    list_kp1 = []
    list_kp2 = []
    for mat in matches:
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx
        # Obtenemos las coordenadas, en forma de tuplas
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt
        list_kp1.append((x1, y1))
        list_kp2.append((x2, y2))

    #se convierten las tuplas a numeros enteros para evitar problemas futuros e_e
    integer_kp1 = []
    for i in list_kp1:
        integer_kp1.append((int(i[0]), int(i[1])))

    integer_kp2 = []
    for i in list_kp2:
        integer_kp2.append((int(i[0]), int(i[1])))

    asd = cv2.line(gray2, integer_kp2[100], integer_kp2[33], (255, 0, 0), 3)

    

    #Se guardan las imagenes de salida
    cv2.imwrite("../img_out/sift_kp1.png", img_whit_kp1)
    cv2.imwrite("../img_out/sift_kp2.png", img_whit_kp2)
    cv2.imwrite("../img_out/matching.png", matching)
    cv2.imwrite("../img_out/line.png", asd)

    

    

    



    

    

