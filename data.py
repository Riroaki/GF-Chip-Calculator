# Color of each troop
COLORS = {
    'bgm-71': '1',
    'ags-30': '2',
    '2b14': '2',
    'm2': '1',
    'at4': '1',
    'qlz-04': '2'
}

# Upper bounds of attributes
ATTR_UPPER_BOUND = {
    'bgm-71': [190, 329, 191, 46],
    'ags-30': [106, 130, 120, 233],
    '2b14': [227, 58, 90, 107],
    'm2': [206, 60, 97, 148],
    'at4': [169, 261, 190, 90],
    'qlz-04': [122, 143, 132, 233]
}

# Shapes
# Heavy fire shape
SHAPE_SLOT = {
    'bgm-71': [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ],
    'ags-30': [
        [0, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
    ],
    '2b14': [
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0]
    ],
    'm2': [
        [1, 1, 1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 1]
    ],
    'at4': [
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0]
    ],
    'qlz-04': [
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0]
    ]
}

# Chip shape
SHAPE_CHIP = {
    '551-11': [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
    ],
    '551-12': [
        [1, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
    ],
    '551-21': [
        [1, 1, 1, 0],
        [0, 0, 1, 1]
    ],
    '551-22': [
        [0, 1, 1, 1],
        [1, 1, 0, 0]
    ],
    '551-31': [
        [0, 1],
        [1, 1],
        [0, 1],
        [0, 1]
    ],
    '551-32': [
        [1, 0],
        [1, 1],
        [1, 0],
        [1, 0]
    ],
    '551-4': [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    '551-5': [
        [0, 1, 1],
        [1, 1, 0],
        [1, 0, 0]
    ],
    '551-6': [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    '56-1': [
        [1, 1, 1],
        [1, 1, 1]
    ],
    '56-2': [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 0]
    ],
    '56-3': [
        [1, 1, 1, 1],
        [0, 1, 1, 0]
    ],
    '56-41': [
        [1, 1, 1, 0],
        [0, 1, 1, 1]
    ],
    '56-42': [
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ],
    '56-5': [
        [1, 1, 0],
        [0, 1, 1],
        [1, 1, 0]
    ],
    '56-6': [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    '56-7': [
        [1],
        [1],
        [1],
        [1],
        [1],
        [1]
    ],
    '56-8': [
        [1, 1, 1, 1],
        [1, 0, 0, 1]
    ],
    '56-9': [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
}

# M2 only
SHAPE_M2 = {
    '551-81': [
        [1, 0],
        [1, 1],
        [1, 1]
    ],
    '551-82': [
        [0, 1],
        [1, 1],
        [1, 1]
    ],
    '551-9': [
        [1],
        [1],
        [1],
        [1],
        [1]
    ],
    '551-10': [
        [1, 1],
        [1, 0],
        [1, 1]
    ],
    '551-111': [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ],
    '551-112': [
        [0, 1, 1],
        [0, 1, 0],
        [1, 1, 0]
    ],
    '551-120': [
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ],
    '551-131': [
        [1, 1, 1, 1],
        [1, 0, 0, 0]
    ],
    '551-132': [
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]
}
