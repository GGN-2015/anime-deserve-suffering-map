from PIL import Image, ImageDraw

def draw_grid_on_image(image_path, grid_size=100):
    try:
        # 打开图片
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        width, height = image.size

        # 绘制水平网格线
        for y in range(0, height, grid_size):
            draw.line((0, y, width, y), fill=(255, 0, 0))

        # 绘制垂直网格线
        for x in range(0, width, grid_size):
            draw.line((x, 0, x, height), fill=(255, 0, 0))

        # 保存修改后的图片
        new_image_path = image_path.rsplit('.', 1)[0] + '_with_grid.png'
        image.save(new_image_path)
        print(f"已绘制网格并保存到 {new_image_path}")
    except FileNotFoundError:
        print(f"错误: 文件 {image_path} 未找到。")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    image_path = 'raw.png'  # 请替换为实际的图片路径
    draw_grid_on_image(image_path)
    