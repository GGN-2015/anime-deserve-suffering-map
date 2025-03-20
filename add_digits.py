from PIL import Image, ImageDraw, ImageFont
from split import get_position
import os

if __name__ == "__main__":
    image = Image.open("raw.png")
    font = ImageFont.load_default(size=20)
    draw = ImageDraw.Draw(image)

    for s in range(5, 101, 5):
        for d in range(5, 101, 5):
            x, y = get_position(s, d)
            color = (192,0,0)
            if os.path.isfile(os.path.join("images", "s%03dd%03d" % (s, d), "name-anime.txt")): # 绿色标出已经知道的名字
                color = (0,192,0)
            draw.text((x, y), "s%dd%d" % (s, d), font=font, fill=color)
    
    image.save("with_digits.png")