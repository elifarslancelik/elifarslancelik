import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# canvas size
width, height = 800, 200

# transparent background
background_color = (0, 0, 0, 0)  # transparent

# gradient colors
colors = [
    (255, 165, 0),   # Turuncu
    (255, 20, 147),  # Pembe
    (0, 255, 127),   # Yeşil
    (30, 144, 255),  # Mavi
    (138, 43, 226)   # Mor
]

# text
text = "Full Stack AI Developer"

# font size
font_size = 50

# create frames for animation
frames = []
total_frames = len(text) * 3  # 3 frames per character

for frame in range(total_frames):
    # create new image (RGBA format with transparent background)
    img = Image.new('RGBA', (width, height), background_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # how many characters to show
    chars_to_show = frame // 3
    
    # center the text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # draw characters one by one
    current_x = x
    for i, char in enumerate(text):
        if i < chars_to_show:
            # calculate gradient color
            color_index = (i / len(text)) * (len(colors) - 1)
            color1_idx = int(color_index)
            color2_idx = min(color1_idx + 1, len(colors) - 1)
            
            # interpolate between two colors
            t = color_index - color1_idx
            color1 = colors[color1_idx]
            color2 = colors[color2_idx]
            
            r = int(color1[0] * (1 - t) + color2[0] * t)
            g = int(color1[1] * (1 - t) + color2[1] * t)
            b = int(color1[2] * (1 - t) + color2[2] * t)
            
            # draw character
            draw.text((current_x, y), char, fill=(r, g, b, 255), font=font)
            
            # next character position
            char_bbox = draw.textbbox((current_x, y), char, font=font)
            char_width = char_bbox[2] - char_bbox[0]
            current_x += char_width + 2  # space between characters
    
    # add gradient border
    border_width = 3
    for i in range(border_width):
        # top border
        color_idx = i / border_width
        color1 = colors[0]
        color2 = colors[1]
        r = int(color1[0] * (1 - color_idx) + color2[0] * color_idx)
        g = int(color1[1] * (1 - color_idx) + color2[1] * color_idx)
        b = int(color1[2] * (1 - color_idx) + color2[2] * color_idx)
        draw.line([(i, i), (width - i, i)], fill=(r, g, b, 255), width=1)
        
        # bottom border
        color1 = colors[3]
        color2 = colors[4]
        r = int(color1[0] * (1 - color_idx) + color2[0] * color_idx)
        g = int(color1[1] * (1 - color_idx) + color2[1] * color_idx)
        b = int(color1[2] * (1 - color_idx) + color2[2] * color_idx)
        draw.line([(i, height - i), (width - i, height - i)], fill=(r, g, b, 255), width=1)
    
    frames.append(img)

# save as gif
frames[0].save(
    'typewriter_banner.gif',
    save_all=True,
    append_images=frames[1:],
    duration=150,  # frame duration
    loop=0
)

print("Congratulations! 'typewriter_banner.gif' saved successfully!") 