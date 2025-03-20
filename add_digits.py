from PIL import Image, ImageDraw, ImageFont
from split import get_position

if __name__ == "__main__":
    image = Image.open("raw.png")
    font = ImageFont.load_default(size=20)
    draw = ImageDraw.Draw(image)

    for s in range(5, 101, 5):
        for d in range(5, 101, 5):
            x, y = get_position(s, d)
            draw.text((x, y), "s%dd%d" % (s, d), font=font, fill=(192,0,0))
    
    image.save("with_digits.png")