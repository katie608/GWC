from PIL import Image

#defining colors
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("FullSizeRender.jpg")
#im.show()
pixles=im.getdata()
pixel_color=[]
size=im.size

for elm in pixles:
    intensity=sum(elm)

    if intensity<=182:
        pixel_color.append(darkBlue)
    elif intensity>182 and intensity<=364:
        pixel_color.append(red)
    elif intensity>364 and intensity<546:
        pixel_color.append(lightBlue)
    elif intensity>=546:
        pixel_color.append(yellow)
        
new_image=Image.new("RGB", (size), "white")
new_image.putdata(pixel_color)
new_image.show()


'''im.getdata()
im.putdata(data)
im.putdata(data, scale, offset)
pixel = value * scale + offset
Image.new(mode, size) ⇒ image
Image.new(mode, size, color) ⇒ image'''


#im = Image.new("RGB", (512, 512), "white")
#im.size ⇒ (width, height)



#new_image.save("output.jpg", "jpeg")


