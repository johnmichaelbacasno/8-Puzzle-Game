# Colors

BLACK = '#23272a'
WHITE = '#ffffff'
PURPLE = '#4e5d94'
RED = '#f04747'
GREY = '#2c2f33'

# Widget Properties

BASIC_FRAME_PROPERTIES = {
    'background': BLACK
}

HEADING_LABEL_PROPERTIES = {
    'text': '8-Puzzle Game',
    'font': ('Tw Cen MT', 50, 'bold'),
    'background': BLACK,
    'foreground': WHITE
}

SUBHEADING_LABEL_PROPERTIES = {
    'text': 'solved using bfs algorithm',
    'font': ('Nunito', 15, 'italic'),
    'background': BLACK,
    'foreground': WHITE
}

TEXT_LABEL_PROPERTIES = {
    'font': ('Tw Cen MT', 20, 'bold'),
    'background': BLACK,
    'foreground': WHITE
}

PRIMARY_BUTTON_PROPERTIES = {
    'font': ('Tw Cen MT Condensed', 18, 'bold'),
    'background': PURPLE,
    'foreground': WHITE,
    'activebackground': GREY,
    'activeforeground': WHITE,
    'width': 8,
    'border': 0,
    'relief': 'raised'
}

SECONDARY_BUTTON_PROPERTIES = {
    'font': ('Tw Cen MT Condensed', 18, 'bold'),
    'background': RED,
    'foreground': WHITE,
    'activebackground': GREY,
    'activeforeground': WHITE,
    'width': 8,
    'border': 0,
    'relief': 'raised'
}

TILES_BUTTON_PROPERTIES = {
    'background': BLACK,
    'foreground': BLACK,
    'activebackground': BLACK,
    'activeforeground': BLACK,
    'disabledforeground': BLACK,
    'border': 0
}