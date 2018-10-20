def addBackground():
    from PIL import Image
    foreground = Image.open('filtered.png', 'r')
    img_w, img_h = foreground.size
    background = Image.open('../space_background_still2.gif','r')
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(foreground, offset)

    background.save('out.png')
