import cv2
import numpy as np

img = cv2.imread("./pictures/shox.png",cv2.IMREAD_GRAYSCALE)
img_blur = cv2.imread("./pictures/shox_blur.png",cv2.IMREAD_GRAYSCALE)

laplacian_var = cv2.Laplacian(img_blur, cv2.CV_64F).var()

#laplacian = cv2.Laplacian(img, cv2.CV_64F)
#cv2.imshow("Laplacian",laplacian)

if laplacian_var<5:
    print("Image is blurry")
else:
    print("Image is fine")

print(laplacian_var)
cv2.imshow("Img",img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
