from PIL import Image, ImageFilter 


img1 = Image.open("my-image.jpg")

image_2 = img.filter(ImageFilter.Minfilter(3))
image_2.save("image_2.jpg")
image_2.show()

