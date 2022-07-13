final_dict = {
    'score': 12,  # overall-score-num
    'score_txt': 'Excellent',  # overall-score-text
    'training': {
        'Mobility': ['Thoracic spine', 'Hip (Flexion/Extension)'], # mobility-<n>
        'Flexibility': ['Hamstrings'], # flex-<n>
        'Coordination & Proprioception': [], # cap-<n>
        'Stability & Strength': ['Leg axis', 'Hip abductors', 'Hip extensors'] # sas-<n>
    },
    'Additional Information': 'Taro'
}

body_colors = {
    1: 'green',
    2: {'L': 'green', 'R': 'orange'},
    3: {'L': 'orange', 'R': 'green'},
    4: {'L': 'green', 'R': 'green'},
    6: 'green',
    8: {'L': 'green', 'R': 'green'},
    9: 'green',
    10: {'L': 'green', 'R': 'orange'},
    11: 'green',
    12: 'green',
    13: {'L': 'green', 'R': 'green'},
    14: {'L': 'green', 'R': 'green'},
    15: {'L': 'green', 'R': 'orange'}
}
rn_dict = {
    'Name': 'Taro Netzer',  # name-surname +
    'Birth Date': '24-07-1968', # --
    'Date': '18-06-2022',  # screening-date +
    'Venue': 'UEFA', # --
    'Shoulder flexion': {'Score': 0},  # shoulder-flexion-score +
    'T-spine extension': {'Score': 0},  # t-spine-extension-score +
    'T-spine rotation': {'Score': {'L': 0, 'R': 3}}, #t-spine-rot-l, t-spine-rot-r --
    'Hip flexion': {'Score': {'L': 0, 'R': 0}}, # hip-flex-l, hip-flex-r --
    'Hip extension': {'Score': {'L': 3, 'R': 0}}, # hip-ext-l, hip-ext-r --
    'Hip exorotation': {'Score': {'L': 0, 'R': 0}}, # hip-exorot-l, hip-exorot-r -- 
    'Hip endorotation': {'Score': {'L': 0, 'R': 0}}, # hip-endo-l, hip-endo-r --
    'Ankle dorsiflexion': {'Score': {'L': 0, 'R': 0}}, # ankle-dorsi-l, ankle-dorsi-r --
    'Pectoralis': {'Score': 0}, # pectoralis-score -
    'Hip flexor': {'Score': {'L': 0, 'R': 0}}, # hip-flexor-l, hip-flexor-r
    'Quadriceps': {'Score': {'L': 0, 'R': 0}}, # quadriceps-l, quadriceps-r
    'Adductors': {'Score': 0}, # adductors-score -
    'Hamstrings': {'Score': {'L': 0, 'R': 3}}, # hamstrings-l, hamstrings-r --
    'Sit & Reach': {'Score': 0}, # sit-reach-score -
    'Sit/Wall test': {'Score': 0}, # sit-wall-test-score -
    '1-leg stand': {'Score': {'L': 0, 'R': 0}}, # 1-leg-stand-l, 1-leg-stand-r --
    'Ventral core': {'Score': 0},  # ventral-core-score + 
    'Dorsal core': {'Score': 0}, # dorsal-core-score -
    'Lateral core': {'Score': {'L': 0, 'R': 0}}, # lateral-core-l, lateral-core-r --
    'Hip abductors 1': {'Score': {'L': 0, 'R': 0}},  # hip-abductors-1-l, hip-abductors-1-r +-
    'Hip abductors 2': {'Score': {'L': 0, 'R': 0}},  # hip-abductors-2-l, hip-abductors-2-r --
    'Hip extensors': {'Score': {'L': 0, 'R': 0}}, # hip-extensors-l, hip-extensors-r +-
    'Leg axis': {'Score': {'L': 0, 'R': 3}} # leg-axis-l, leg-axis-r --
}


# ToDo:

# 1. Find corresponding tspan elements in svg and assign id to them --- done
# 2. replace dummy data with actual data
# 3. generate pdfs
# 4. zip pdfs
# 5. delete pdfs

