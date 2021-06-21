import cv2

image=cv2.imread("smt.jpg")
smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml") 
print(smile_cascade)
smiles=smile_cascade.detectMultiScale(image,scaleFactor=1.8,minNeighbors=20)

for(sx, sy, sw, sh) in smiles:
    cv2.rectangle( image, (sx,sy), ((sx+sw), (sy+sh)), (8,8,255), 7)

cv2.imshow("Smile Detected", image)
print(cv2.imshow)

cv2.waitKey(0)
cv2.destroyAllWindows()