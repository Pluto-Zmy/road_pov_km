from PIL import ImageFont

class FontSize:
    def get_font_width(text, font, size):
        return sum([ImageFont.truetype(font, int(size), 0).getsize(char)[0] for char in text])
