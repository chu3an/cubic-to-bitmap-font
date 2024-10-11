from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2


def ascii_to_bitmap(text: str):
    image_size = (550, 550)
    pil_image = Image.new('RGB', image_size, 'white')
    font_path = 'Cubic_11.ttf'
    font_size = 500
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(pil_image)
    position = (0, 0)
    draw.text(position, text, font=font, fill='black')
    # pil_image.save('output.png')  # debug
    # pil_image.show()  # debug
    np_image = np.array(pil_image)
    cv_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2GRAY)
    BOX_SIZE = 42

    bitmap = np.zeros((13, 13))
    for x in range(13):
        for y in range(13):
            x1, x2 = x * BOX_SIZE, (x+1) * BOX_SIZE
            y1, y2 = y * BOX_SIZE, (y+1) * BOX_SIZE
            crop_image = cv_image[x1:x2, y1:y2]
            if np.sum(crop_image > 128) > 0.8 * crop_image.size:
                bitmap[x][y] = 0  # white block
            else:
                bitmap[x][y] = 1  # black block

    b = bitmap[2:, :].astype(int)
    return b[:, ~np.all(b == 0, axis=0)].tolist()

# def cut_empty_column(array):
#     for i in array:
#         if i[-1] == 1:
#             return array
#     return cut_empty_column(array[:, :-1])


def main():
    f = open('ascii_font.py', 'w', encoding='utf-8')
    f.write('ascii_font = {')
    f.write('\n')
    for i in range(93):
        bitmap = ascii_to_bitmap(chr(i+33))
        if i+33 in [34, 39, 92]:
            f.write(f'\'\\{chr(i+33)}\':{bitmap},\n')
        else:
            f.write(f'\'{chr(i+33)}\':{bitmap},\n')
    f.write('}')
    f.close()


if __name__ == '__main__':
    main()
