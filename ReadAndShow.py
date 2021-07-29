import cv2


#視窗名稱
cv2.namedWindow("Image",cv2.WINDOW_FREERATIO)

#讀取圖片
img = cv2.imread("image.jpg",1)

#show出圖片
cv2.imshow("Image",img)
cv2.imwrite('image1.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),70])
#等待時間(0就是你按下任意鍵前不動作)
cv2.waitKey(0)

#關閉所有視窗
cv2.destroyAllWindows()