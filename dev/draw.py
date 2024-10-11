from PIL import Image, ImageDraw, ImageFont

text = '字'

image_size = (550, 550)
image = Image.new('RGB', image_size, 'white')
font_path = 'Cubic_11.ttf'
font_size = 500
font = ImageFont.truetype(font_path, font_size)
draw = ImageDraw.Draw(image)
position = (0, 0)
draw.text(position, text, font=font, fill="black")
image.save('output.png')
