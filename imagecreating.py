Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Priyanka_Varma\\AppData\\Local\\Programs\\Python\\Python38-32'
>>> from PIL import ImageColor
>>> ImageColor.getColor('red', 'RGBA')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ImageColor.getColor('red', 'RGBA')
AttributeError: module 'PIL.ImageColor' has no attribute 'getColor'
>>> os.chdir("C:\\Users\\Priyanka_Varma\\Desktop\\Folder1")
>>> os.getcwd()
'C:\\Users\\Priyanka_Varma\\Desktop\\Folder1'
>>> from PIL import ImageColor
>>> ImageColor.getcolor('red', 'RGBA')
(255, 0, 0, 255)
>>> ImageColor.getcolor('black','RGBA')
(0, 0, 0, 255)
>>> from PIL import Image
>>> img = Image.open('imgage.jpeg')
>>> img.size
(1200, 900)
>>> width, height = img.size
>>> print("The Image Width is :: ", width, " and the height is : ", height)
The Image Width is ::  1200  and the height is :  900
>>> img.filename
'imgage.jpeg'
>>> img.format_Description
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    img.format_Description
AttributeError: 'JpegImageFile' object has no attribute 'format_Description'
>>> img.format_description
'JPEG (ISO 10918)'
>>> img.save('image.jpeg')
>>> im = Image.new('RGBA', (100,200),'purple')
>>> im.save('purpleimage.jpg')
Traceback (most recent call last):
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\site-packages\PIL\JpegImagePlugin.py", line 612, in _save
    rawmode = RAWMODE[im.mode]
KeyError: 'RGBA'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    im.save('purpleimage.jpg')
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\site-packages\PIL\Image.py", line 2134, in save
    save_handler(self, fp, filename)
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\site-packages\PIL\JpegImagePlugin.py", line 614, in _save
    raise OSError("cannot write mode %s as JPEG" % im.mode)
OSError: cannot write mode RGBA as JPEG
>>> im.save('purpleimage.jpeg')
Traceback (most recent call last):
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\site-packages\PIL\JpegImagePlugin.py", line 612, in _save
    rawmode = RAWMODE[im.mode]
KeyError: 'RGBA'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    im.save('purpleimage.jpeg')
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\site-packages\PIL\Image.py", line 2134, in save
    save_handler(self, fp, filename)
  File "C:\Users\Priyanka_Varma\AppData\Local\Programs\Python\Python38-32\lib\site-packages\PIL\JpegImagePlugin.py", line 614, in _save
    raise OSError("cannot write mode %s as JPEG" % im.mode)
OSError: cannot write mode RGBA as JPEG
>>> im.save('purpleimage.png')
>>> im2 = Image.new('RGBA', (1080,1920), 'blue')
>>> im2.save('blueimage.png')
>>> croppedImage = im2.crop((335,345,565,560))
>>> croppedImage.save()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    croppedImage.save()
TypeError: save() missing 1 required positional argument: 'fp'
>>> croppedImage.save('cropped.png')
>>> img = Image.open('image.jpeg')
>>> img_copy = img.copy()
>>> cropped_image = img.crop((365,345,565,560))
>>> img_copy.paste(cropped_image, (0,0))
>>> img_copy.save('pasted.png')
>>> 