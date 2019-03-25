from PIL import Image, ImageOps

pic = Image.open("mark.jpg")
pic= pic.convert("RGB")
red, green, blue = pic.split()

red_coordinates = (600, 400, 1200, 800)
blue_coordinates = (0, 0, 600, 400)

red_cropped = red.crop(red_coordinates)
blue_cropped = blue.crop(blue_coordinates)

#it makes the same size for all layers
red.thumbnail((600, 400))
green.thumbnail((600, 400))
blue.thumbnail((600, 400))

red_blended = Image.blend(red, red_cropped, 0.5)
blue_blended = Image.blend(blue, blue_cropped, 0.5)

avatar = Image.merge("RGB",(red_blended, green, blue_blended))

avatar.thumbnail((80,80))
avatar.save("avatar.jpg")
