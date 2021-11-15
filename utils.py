from TheQuest import WHITE


def create_text(font, text, rect_option, rect_coor):
    txt = font.render(text, True, WHITE)
    txt_rect = txt_rect_option(txt, rect_option, rect_coor)
    return [txt, txt_rect]


def txt_rect_option(txt_rendered, rect_option, rect_coor):
    txt_rect = txt_rendered.get_rect()
    if rect_option == 'center':
        txt_rect.center = rect_coor
    elif rect_option == 'midbottom':
        txt_rect.midbottom = rect_coor
    elif rect_option == 'midtop':
        txt_rect.midtop = rect_coor
    elif rect_option == 'topleft':
        txt_rect.topleft = rect_coor
    elif rect_option == 'topright':
        txt_rect.topright = rect_coor
    return txt_rect
