import cv2

path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(path)

try:
    image = cv2.imread('image/person.jpg')
    image = cv2.resize(image, (400, 300), interpolation=cv2.INTER_AREA)


    faces = faceCascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

    imgheight = image.shape[0]
    imgwidth = image.shape[1]

    cv2.rectangle(image,(10,imgheight-20),(110,imgheight),(0,0,0),-1)

    cv2.putText(image,"Find{}".format(str(len(faces)))+" faces",(10,imgheight-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255))

    counts = 1
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(128,255,0),1)
        filename = 'image/{}.jpg'.format(str(counts))
        image_coordinate = image[y+1:y+h,x+1:x+w]
        resize_image = cv2.resize(image_coordinate,(100,100))
        cv2.imwrite(filename,resize_image)
        counts += 1

    cv2.namedWindow("faceidentify")

    cv2.imshow("faceidentify",image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

except:
    print('file is not found or error')