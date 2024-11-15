# Opencv Tutorial by campusx
- Opencv is a C++ package for image processing
- We need to install the following packages
```
pip install opencv-python numpy
```
``` python
import cv2
import numpy
``` 
## Reading image 
- Opencv reads an image as a numpy array
``` python
img=cv2.imread("images/Subu photo.jpg")
print(type(img))
```
o/p: <class 'numpy.ndarray'>
- Let's find out the resolution of the image
``` python
print(img.shape)
```
o/p: (375, 254, 3)
- The image has 375p X 254p resolution and 3 indicates the image is a RGB image.
- To show the image, we will have to use the following syntax
``` python
cv2.imshow("window name",img)
cv2.waitKey(0) 
```
o/p:

<img src="images/Screenshot 2024-07-20 102634.png" width="200" height="">

- We set `cv2.waitKey(0)` to show our img for infinite amount of time. Otherwise the image will come for an instance and go away.

**Converting RGB image to Grayscale**

``` python
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("window name",img_gray)
```
op:

<img src="images/Screenshot 2024-07-20 104237.png" width="200" height="">

- Now we will find out the shape of the image
``` python
print(img_gray.shape)
```
O/P: (375, 254)
- The 3 is not there in Tuple since it is a grayscale image now.
## Playing with colour scaling
- If we want to set the blue component to zero
``` python
img[:,:,0]=0
```
<img src="images/Screenshot 2024-07-20 110016.png" width="200" height="">

- If we want to remove green and red components
``` python
img[:,:,1]=0 #Removing green component
img[:,:,2]=0 #Removing red component
```
**Showing individual image components**
``` python
img_blue=img[:,:,0]
img_green=img[:,:,1]
img_red=img[:,:,2]
new_img=np.hstack((img_blue,img_green,img_red))
cv2.imshow("window name",new_img)
```
O/p:

<img src="images/Screenshot 2024-07-20 111654.png" width="300" height="">

## Image Resizing
``` python
img_resize=cv2.resize(img,(300,200))
cv2.imshow("window name",img_resize)
cv2.waitKey(0)
```
O/P:

<img src="images/Screenshot 2024-07-20 125633.png" width="250" height="">

- If we want to resize our image to half of its width and height without knowning it's shape
``` python
img_resize=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
# not (img.shape[0]//2,img.shape[1]//2)
cv2.imshow("window name",img_resize)
``` 
## Flipping Image
1. **Flipping in vertical axis**
``` python
img_flip=cv2.flip(img,0)
cv2.imshow("window name",img_flip)
```
O/p:

<img src="images/Screenshot 2024-07-20 141254.png" width="200" height="">

2. **Flipping in horizontal axis**
``` python
img_flip=cv2.flip(img,1)
```

<img src="images/Screenshot 2024-07-20 141627.png" width="200" height="">

- It is used to solve overfitting issues in machine learning model using data augmentation
- If we set `cv2.flip(img,-1)`the image will flip both horizontally and vertically.

<img src="images/Screenshot 2024-07-20 142142.png" width="200" height="">

## Cropping
- It is as similar as slicing in numpy array.
``` python
img_crop=img[30:175,80:170]
cv2.imshow("window name",img_crop)
```
<img src="images/Screenshot 2024-07-20 143156.png" width="150" height="">

## Saving Image
```
cv2.imwrite("cropped_img.png",img_crop)
```
O/p:

<img src="images/Screenshot 2024-07-20 175403.png" width="" height="">

## Drawing shapes and text on images
- It is used for object and face detection ML models.
- Let us consider a blank image
``` python
img=np.zeros((512,512,3))
cv2.imshow("window name",img)
```
O/P:

<img src="images/Screenshot 2024-07-20 180706.png" width="300" height="">


1. **Rectangle**:\
Syntax:
``` python
cv2.rectangle(img,pt1=(x1,y1),pt2=(x2,y2),color=(B,G,R),thickness=)
```
- If we want to fill the rectangle or any shape 
we will set `thickness=1`
- p1 and p2 represent the following points of the rectangle.

<img src="images/cdm.drawio (1).png" width="350" height="">

2. **Circle**:
``` python
cv2.circle(img,centre=(x,y),radius=,color=(B,G,R),thickness=)
```
3. **Line**:
``` python
cv2.line(img,pt1=(x1,y1),pt2=(x2,y2),color=(B,G,R),thickness=)
```
4. **Text**:
``` python
cv2.putText(img,org=(x1,y1), fontScale=4,color=(B,G,R), thickness=2,lineType=cv2.LINE_AA,text="Hello",fontFace=cv2.FONT_ITALIC)
```
## Holding Screen for unlimited time
``` python
```




















