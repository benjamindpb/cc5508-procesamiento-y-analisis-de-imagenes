import cv2
import numpy as np

if __name__== '__main__':
    
    img1 = cv2.imread('../img/caso_2/1a.jpg')
    img2 = cv2.imread('../img/caso_2/2a.jpg')

    gray= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray)
    print("n_kp: {}".format(len(kp)))
    #kp, des = sift.compute(gray, kp)
    cv2.drawKeypoints(gray,kp, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("img1", img1)

    cv2.waitKey()
    cv2.destroyAllWindows()

    

