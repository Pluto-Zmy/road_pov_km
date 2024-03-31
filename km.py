from PIL import Image, ImageDraw, ImageFont
from utils.font_size import *


left_cx = 120
right_cx = 336

top_cy = 60
mid_cy = 64
bottom_cy = 138

font_path = 'resources/B_PIL.ttf'


def draw_text(bg, seq, sub_seq, km, bm):
    image = bg.copy()
    draw = ImageDraw.Draw(image)

    big_km_font = ImageFont.truetype(font_path, 100)
    big_km_width = FontSize.get_font_width(km, font_path, 100)
    big_km_pos = (left_cx - big_km_width / 2, top_cy - 100 / 2)
    draw.text(big_km_pos, km, font=big_km_font, fill=(255, 255, 255))

    small_km_font = ImageFont.truetype(font_path, 48)
    small_km_width = FontSize.get_font_width(km, font_path, 48)
    small_km_pos = (right_cx - small_km_width / 2, bottom_cy - 48 / 2)
    draw.text(small_km_pos, km, font=small_km_font, fill=(0, 128, 0))

    bm_font = ImageFont.truetype(font_path, 128)
    bm_width = FontSize.get_font_width(bm, font_path, 128)
    bm_pos = (right_cx - bm_width / 2, mid_cy - 128 / 2)
    draw.text(bm_pos, bm, font=bm_font, fill=(255, 255, 255))

    seq_font = ImageFont.truetype(font_path, 48)
    seq_width = FontSize.get_font_width(seq, font_path, 48)
    sub_seq_font = ImageFont.truetype(font_path, 32)
    sub_seq_width = FontSize.get_font_width(sub_seq, font_path, 32)

    seq_sum_width = seq_width + sub_seq_width
    seq_x = left_cx - seq_sum_width / 2
    seq_y = bottom_cy - 60 / 2
    seq_pos = (seq_x, seq_y)

    sub_seq_x = seq_x + seq_width
    sub_seq_y = bottom_cy - 40 / 2 + 8 / 2
    sub_seq_pos = (sub_seq_x, sub_seq_y)

    draw.text(seq_pos, seq, font=seq_font, fill=(255, 255, 255))
    draw.text(sub_seq_pos, sub_seq, font=sub_seq_font, fill=(255, 255, 255))

    return image


if __name__ == '__main__':
    bg = Image.open('bg.png')
    seq = 'G50'
    sub_seq = '13'
    begin = 58
    end = 254

    count = 0
    for km in range(begin, end + 1):
        for bm in range(0, 10):
            image = draw_text(bg, seq, sub_seq, str(km), str(bm))
            image.save('output/{}.png'.format(count))
            count += 1