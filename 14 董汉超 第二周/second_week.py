import cv2
import numpy as np
img = cv2.imread(r"C:\Users\lenovo\Desktop\lenna.jpg")
import matplotlib.pyplot as plt
new_img = np.zeros([200,200,1],img.dtype)

#手工实现RGB2GRAY
for i in range(200):
    for j in range(200):
        new_img[i,j]=img[i,j,0]*0.11+img[i,j,1]*0.59+img[i,j,2]*0.3
print(new_img)
cv2.imwrite(r"C:\Users\lenovo\Desktop\new_lenna.jpg",new_img)

#调接口实现RGB2GRAY
new_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(new_img,cmap='gray')
plt.show()

#二值化
new_img = np.where(new_img/255 >=0.5,1,0)
plt.imshow(new_img,cmap="gray")
plt.show()