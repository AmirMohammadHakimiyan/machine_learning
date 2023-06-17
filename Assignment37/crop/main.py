import cv2

img=cv2.imread("input/mnist.png")
rows,cols,_=img.shape
number=0
number2=0
number3=0

for row in range(rows//20):
    number+=1
    
    for col in range(cols//20):
        number3+=1
        min=img[row*20:(row+1)*20,col*20:(col+1)*20]
        name="output/"+str(number2)+"/"+str(number3)+".png"
        cv2.imwrite(name,min)
    if number%5==0:
        number2+=1