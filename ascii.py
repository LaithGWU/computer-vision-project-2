from PIL import Image
import math

#FONT_SIZE = 20
ASCII_CHARACTERS = " `.-':_,^=;><+!rc*/z?sLTv)J7(|FiC}{fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

def greyscale_to_ascii(ascii_string, greyscale_value):
    step = 255 / (len(ascii_string) - 1)
    index = math.floor(greyscale_value / step)
    return ascii_string[index]

def resize_tuple(width, height, percentage):
    return math.floor(width * percentage), math.floor(height * percentage)

# Opening image
while True:
    try:
        image_file = input("Please specify an image: ")
        img = Image.open(image_file)
    except FileNotFoundError:
        print("File not found, try again")
        continue
    break

file_name = image_file.split(".")[0]

# Converting to greyscale
img = img.convert('L')

width, height = img.size
while True:
    try:
        ratio = float(input("Enter ratio scaler: "))
    except ValueError:
        print("Please enter a float")
        continue
    break

img = img.resize(resize_tuple(width, height, ratio))

img.save(file_name + "-resized.png")

# Getting image as array
pix = img.load()
print(img.size)
#pix_normalized = pix / 255

#ascii_pix = np.interp(pix_normalized,[0, 1], [0, len(ASCII_CHARACTERS) - 1]).astype(int)
width, height = img.size

ascii_text = "\n".join(
    "".join(greyscale_to_ascii(ASCII_CHARACTERS, pix[x, y]) for x in range(width)) 
    for y in range(height))

print(ascii_text)
print(len(ascii_text))
file = open(file_name + "-ascii-art.txt", "w+")
file.write(ascii_text)
file.close()

#print(str(img.width) + ", " + str(img.height))
#ascii_art = Image.new("RGB", (img.width * FONT_SIZE, img.height * FONT_SIZE), "white")
#draw = ImageDraw.Draw(ascii_art)
#font = ImageFont.load_default(FONT_SIZE)
#margin = FONT_SIZE
#x, y = margin, margin

#for line in ascii_text.split("\n"):
#    print("processing...")
#    draw.text((x, y), line, font=font, fill="black")
#    y += FONT_SIZE + 5

#ascii_art.save("ascii_art.png")