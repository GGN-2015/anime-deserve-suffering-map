from PIL import Image
import os

def get_position(suffering, deserved):
    assert 5 <= suffering <= 100 and 5 <= deserved <= 100
    assert suffering % 5 == 0 and deserved % 5 == 0
    x = ((deserved / 5 - 1) + 2) * 100
    y = (20 - (suffering / 5)) * 100
    return (x, y)

def get_subimage(image_path, x, y):
    try:
        # 打开图片
        image = Image.open(image_path)

        # 确保子图在图片范围内
        width, height = image.size

        # 定义子图的边界
        left = x
        top = y
        right = min(x + 100, width)
        bottom = min(y + 100, height)

        # 裁剪子图
        sub_image = image.crop((left, top, right, bottom))

    except FileNotFoundError:
        print(f"错误: 文件 {image_path} 未找到。")
        sub_image = None

    except Exception as e:
        print(f"发生未知错误: {e}")
        sub_image = None

    return sub_image

def get_subimage_by_suffering_and_deserved(suffering, deserved):
    x, y = get_position(suffering, deserved)
    sub_image = get_subimage("raw.png", x, y)
    return sub_image

if __name__ == "__main__":
    for s in range(5, 101, 5):
        for d in range(5, 101, 5):
            print("processing s = %03d, d = %03d ..." % (s, d))
            image = get_subimage_by_suffering_and_deserved(s, d)
            folder_name = os.path.join("images", "s%03dd%03d" % (s, d))
            png_file = os.path.join(folder_name, "avatar.png")
            os.makedirs(folder_name, exist_ok=True)
            image.save(png_file)