import os
import glob
from PIL import Image, ImageDraw, ImageFont
from utils.font_size import FontSize

# 布局中心坐标
LEFT_CENTER_X = 120
RIGHT_CENTER_X = 336
TOP_CENTER_Y = 60
MID_CENTER_Y = 64
BOTTOM_CENTER_Y = 138

# 字体路径与大小
FONT_PATH = 'resources/B_PIL.ttf'
KM_LARGE_FONT_SIZE = 100
KM_SMALL_FONT_SIZE = 48
HM_FONT_SIZE = 128
SEQ_FONT_SIZE = 48
SUB_SEQ_FONT_SIZE = 32

# 颜色
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

# 预加载字体
km_large_font = ImageFont.truetype(FONT_PATH, KM_LARGE_FONT_SIZE)
km_small_font = ImageFont.truetype(FONT_PATH, KM_SMALL_FONT_SIZE)
hm_font = ImageFont.truetype(FONT_PATH, HM_FONT_SIZE)
seq_font = ImageFont.truetype(FONT_PATH, SEQ_FONT_SIZE)
sub_seq_font = ImageFont.truetype(FONT_PATH, SUB_SEQ_FONT_SIZE)


def _get_text_width(text, font_size):
    return FontSize.get_font_width(text, FONT_PATH, font_size)


def _centered_pos(center_x, center_y, text_width, font_size):
    return (center_x - text_width / 2, center_y - font_size / 2)


def draw_marker(bg, seq, sub_seq, km_text, hm_text):
    image = bg.copy()
    draw = ImageDraw.Draw(image)

    # 左上：大字公里数
    km_large_width = _get_text_width(km_text, KM_LARGE_FONT_SIZE)
    km_large_pos = _centered_pos(LEFT_CENTER_X, TOP_CENTER_Y, km_large_width, KM_LARGE_FONT_SIZE)
    draw.text(km_large_pos, km_text, font=km_large_font, fill=WHITE)

    # 右下：小字公里数
    km_small_width = _get_text_width(km_text, KM_SMALL_FONT_SIZE)
    km_small_pos = _centered_pos(RIGHT_CENTER_X, BOTTOM_CENTER_Y, km_small_width, KM_SMALL_FONT_SIZE)
    draw.text(km_small_pos, km_text, font=km_small_font, fill=GREEN)

    # 右中：百米桩
    hm_width = _get_text_width(hm_text, HM_FONT_SIZE)
    hm_pos = _centered_pos(RIGHT_CENTER_X, MID_CENTER_Y, hm_width, HM_FONT_SIZE)
    draw.text(hm_pos, hm_text, font=hm_font, fill=WHITE)

    # 左下：路线编号 + 子编号
    seq_width = _get_text_width(seq, SEQ_FONT_SIZE)
    sub_seq_width = _get_text_width(sub_seq, SUB_SEQ_FONT_SIZE)
    total_width = seq_width + sub_seq_width

    seq_x = LEFT_CENTER_X - total_width / 2
    seq_y = BOTTOM_CENTER_Y - 60 / 2
    draw.text((seq_x, seq_y), seq, font=seq_font, fill=WHITE)

    sub_seq_x = seq_x + seq_width
    sub_seq_y = BOTTOM_CENTER_Y - 40 / 2 + 8 / 2
    draw.text((sub_seq_x, sub_seq_y), sub_seq, font=sub_seq_font, fill=WHITE)

    return image


if __name__ == '__main__':
    output_dir = 'output'
    if os.path.exists(output_dir):
        for f in glob.glob(os.path.join(output_dir, '*')):
            os.remove(f)
    else:
        os.makedirs(output_dir)

    bg = Image.open('resources/bg.png')
    seq = 'G15'
    sub_seq = '23'
    km_start = 1699
    km_end = 1720

    count = 0
    for km in range(km_start, km_end + 1):
        for hm in range(10):
            image = draw_marker(bg, seq, sub_seq, str(km), str(hm))
            image.save(f'output/{count}.png')
            count += 1