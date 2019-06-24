from PIL import Image, ImageFilter, ImageDraw, ImageFont
from num_to_words import say_the_words
BASE_DIR = '/Users/alikhundmiri/Desktop/'
import re

buffer_size = 45
'''
DONE 1. Create image of size 1080 width by 1350 height
DONE 2. get the text from num_to_words, and
DONE 3. write it on image with justified
'''

bold_font_location = '/Users/alikhundmiri/Downloads/fonts/Montserrat/Montserrat-Black.ttf'
extra_light_font_location = '/Users/alikhundmiri/Downloads/fonts/Montserrat/Montserrat-ExtraLight.ttf'
# font_location = 'https://fonts.googleapis.com/css?family=Montserrat:900&display=swap'


def create_image():
    # Take two is a code from stackoverflow, it detects the size of image, and assigns the proper font size.
    image = Image.new("RGB",(1080, 1350), color=(246,240,240))
    draw = ImageDraw.Draw(image)
    followers = say_the_words(4040090)

    txt_before = 'Yes, I finally have'
    txt_main = followers
    txt_after = 'followers on my Instagram'
    txt_end = 'Follow me @{}'.format("AliCoderMaker")
    
    text_list = generate_text_list(txt_main)

    w_i, h_i = image.size
    h = buffer_size # setting the initial height to be 25
    tot_h = 0

    print("writing pre text")
    text_color = (169,169,169,255)
    h, tot_h = write_text(txt_before, h,tot_h, extra_light_font_location, w_i, draw, text_color)

    print("writing number of followers")
    for t in text_list:
        text_color = (120,120,120,255)
        h, tot_h = write_text(t, h,tot_h, bold_font_location, w_i, draw, text_color)
    
    print("writing post text")
    text_color = (69,69,69,255)
    h, tot_h = write_text(txt_after, h,tot_h, extra_light_font_location, w_i, draw, text_color)

    print("writing exit text")
    text_color = (69,69,69,255)
    h, tot_h = write_text(txt_end, h,tot_h, extra_light_font_location, w_i, draw, text_color)

    image.save(BASE_DIR+'take_eight.png')  # save it

def write_text(t, h,tot_h, bold_font_location, w_i, draw, text_color):
    font, fontsize = font_adjustment(t, bold_font_location, w_i)
    w_f, h_f = font.getsize(str(fontsize))
    draw.text((10, h), t, font=font, fill=(69,69,69,255))  # put the text on the image
    h += (h_f + buffer_size)
    tot_h += h
    return h, tot_h

def generate_text_list(txt):
    # This will split the text in to many lines after every 16 character
    text_list = []
    if len(txt) < 16:
        text_list = txt.split(",.|")
    else:
        text_list.append(txt)
    text_list = re.findall(r'.{1,16}(?:\s+|$)', txt.title())
    return text_list

def font_adjustment(text, font_location, image_width):
    fontsize = 1  # starting font size
    # portion of image width you want text width to be
    img_fraction = 0.95
    font = ImageFont.truetype(font_location, fontsize)
    while font.getsize(text)[0] < img_fraction * image_width:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(font_location, fontsize)
    # optionally de-increment to be sure it is less than criteria
    fontsize -= 2
    font = ImageFont.truetype(font_location, fontsize)
    return font, fontsize

if __name__ == "__main__":
    create_image()