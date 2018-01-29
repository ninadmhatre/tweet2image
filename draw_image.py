from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import time
import logging

MAX_W, MAX_H = 1980, 1080
LINE_LENGTH = 90  
QUOTE_TEXT_SIZE, HEADER_TEXT_SIZE = 36, 48
GAP_BETWEEN_LINES = QUOTE_TEXT_SIZE / 3
FONT = 'arial.ttf'


def make_image(user, quote, outdir='.', verbose=False):
    para = textwrap.wrap(quote, width=LINE_LENGTH)
    num_of_lines = len(para)
    height_of_para = (num_of_lines * QUOTE_TEXT_SIZE) + ((num_of_lines - 1) * GAP_BETWEEN_LINES)

    im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT, QUOTE_TEXT_SIZE)

    current_h = (MAX_H / 2) - (height_of_para / 2)

    header_font = ImageFont.truetype(FONT, HEADER_TEXT_SIZE)
    h_w, h_h = draw.textsize(user, font=font)
    h_w += 2 * HEADER_TEXT_SIZE

    draw.text(((MAX_W - h_w) / 2, current_h), user, font=header_font, fill='white')
    current_h += h_h + GAP_BETWEEN_LINES + 20

    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill='white')
        current_h += h + GAP_BETWEEN_LINES

    out_file = os.path.join(os.path.abspath(outdir), '%d.png' % time.time())

    while os.path.isfile(out_file):
        time.sleep(1)
        out_file = os.path.join(os.path.abspath(outdir), '%d.png' % time.time())

    if verbose:
        print('saving image [%s]...' % out_file)
    im.save(out_file)
