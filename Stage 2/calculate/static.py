
# Screenings
# Add body part numbers to each training
uefa_core = {
    "Hip flexion": {"training":[3], "group" : "Mobility", "type": "2"},
    "Hip extension": {"training":[3], "group" : "Mobility", "type": "2"}, 
    "Hip exorotation": {"training": [4], "group": "Mobility", "type": "2"}, 
    "Hip endorotation": {"training": [4], "group": "Mobility", "type": "2"}, 
    "Ankle dorsiflexion": {"training": [5, 11], "group": "Mobility", "type": "2"},

    "Quadriceps": {"training": [8], "group": "Flexibility", "type": "2"}, 
    "Adductors": {"training": [9], "group": "Flexibility", "type": "1"}, 
    "Hamstrings": {"training": [10], "group": "Flexibility", "type": "2"}, 
    "Sit & Reach": {"training": [10], "group": "Flexibility", "type": "1"}, 
    "1-leg stand": {"training": [12], "group": "Coordination & Proprioception", "type": "2"},

    "Ventral core": {"training": [13], "group": "Stability & Strength", "type": "1"}, 
    "Dorsal core": {"training": [14], "group": "Stability & Strength", "type": "1"}, 
    "Lateral core": {"training": [15], "group": "Stability & Strength", "type": "2"}, 
    "Leg axis": {"training": [16, 17, 18], "group": "Stability & Strength", "type": "2"}, 
}



uefa_20 = {
    "T-spine extension": {"training":[2], "group" : "Mobility", "type": "1"}, 
    "T-spine rotation": {"training":[2], "group" : "Mobility", "type": "2"}, 
     

    "Pectoralis": {"training": [6, 19], "group": "Flexibility", "type": "1"}, 
    "Hip flexor": {"training": [7], "group": "Flexibility", "type": "2"}, 


    "Hip abductors 1": {"training": [16], "group": "Stability & Strength", "type": "2"}, 
    "Hip extensors": {"training": [17], "group": "Stability & Strength", "type": "2"}, 
}

cc25 = {
    "Shoulder flexion": {"training": [1], "group": "Mobility", "type": "1"},

    "Sit/Wall test": {"training": [1, 2, 19], "group": "Flexibility", "type": "1"},

    "Hip abductors 2": {"training": [16], "group": "Stability & Strength", "type": "2"},
}

tr_shorts = {
    "Shoulder FLEX": "Shoulder flexion",
    "TX EXT": "T-spine extension",
    "TX ROT L": "T-spine rotation",
    "TX ROT R": "T-spine rotation",
    "Hip FLEX L": "Hip flexion",
    "Hip FLEX R": "Hip flexion",
    "Hip EXT L": "Hip extension",
    "Hip EXT R": "Hip extension",
    "Hip EXROT L": "Hip exorotation",
    "Hip EXROT R": "Hip exorotation",
    "Hip ENROT L": "Hip endorotation",
    "Hip ENROT R": "Hip endorotation",
    "Ankle DF L": "Ankle dorsiflexion",
    "Ankle DF R": "Ankle dorsiflexion",
    "Pectoralis": "Pectoralis",
    "Hip flexor L": "Hip flexor",
    "Hip flexor R": "Hip flexor",
    "Quadr L": "Quadriceps",
    "Quadr R": "Quadriceps",
    "Add": "Adductors",
    "Hamstr L": "Hamstrings",
    "Hamstr R": "Hamstrings",
    "Sit&Reach": "Sit & Reach",
    "Sit/Wall": "Sit/Wall test",
    "1-leg L": "1-leg stand",
    "1-leg R": "1-leg stand",
    "Ventral": "Ventral core",
    "Dorsal": "Dorsal core",
    "Lateral L": "Lateral core",
    "Lateral R": "Lateral core",
    "Hip Abd1 L": "Hip abductors 1",
    "Hip Abd1 R": "Hip abductors 1",
    "Hip Abd2 L": "Hip abductors 2",
    "Hip Abd2 R": "Hip abductors 2",
    "Hip Ext L": "Hip extensors",
    "Hip Ext R": "Hip extensors",
    "Leg axis L": "Leg axis",
    "Leg axis R": "Leg axis",
}

types = {
    "Hip flexion": "2", 
    "Hip extension": "2", 
    "Hip exorotation": "2", 
    "Hip endorotation": "2", 
    "Ankle dorsiflexion": "2", 
    "Quadriceps": "2", 
    "Adductors": "1", 
    "Hamstrings": "2", 
    "Sit & Reach": "1", 
    "1-leg stand": "2", 
    "Ventral core": "1", 
    "Dorsal core": "1", 
    "Lateral core": "2", 
    "Leg axis": "2", 
    "T-spine extension": "1", 
    "T-spine rotation": "2", 
    "Pectoralis": "1", 
    "Hip flexor": "2", 
    "Hip abductors 1": "2", 
    "Hip extensors": "2", 
    "Shoulder flexion": "1", 
    "Sit/Wall test": "1", 
    "Hip abductors 2": "2", 
}


    
# Trainings
trainings = {
    "Mobility": {
        "1" : "Shoulder",
        "2" : "Thoracic spine",
        "3" : "Hip (Flexion/Extension)",
        "4" : "Hip (Rotation)",
        "5" : "Ankle (Dorsiflexion)",
    },
    "Flexibility": {
        "6" : "Pectoralis",
        "7" : "Hip flexor",
        "8" : "Quadriceps",
        "9" : "Adductors",
        "10" : "Hamstrings",
        "11" : "Calf",
    },
    "Coordination & Proprioception": {
        "12" : "Leg axis / Ankle",
    },
    "Stability & Strength": {
        "13" : "Ventral core",
        "14" : "Dorsal core",
        "15" : "Lateral core",
        "16" : "Hip abductors",
        "17" : "Hip extensors",
        "18" : "Leg axis",
        "19" : "Shoulder blade",
    },
}

colors = {
    0: "green",
    3: "orange",
    5: "red",
}

body_parts = {
   "Hip flexion": 3, 
    "Hip extension": 3, 
    "Hip exorotation": 3, 
    "Hip endorotation": 3, 
    "Ankle dorsiflexion": 4, 
    "Quadriceps": 8, 
    "Adductors": 9, 
    "Hamstrings": 10, 
    "Sit & Reach": 10, 
    "1-leg stand": 4, 
    "Ventral core": 11, 
    "Dorsal core": 12, 
    "Lateral core": 13, 
    "Leg axis": 15, 
    "T-spine extension": 2, 
    "T-spine rotation": 2, 
    "Pectoralis": 6, 
    "Hip flexor": 3, 
    "Hip abductors 1": 14, 
    "Hip extensors": 14, 
    "Shoulder flexion": 1, 
    "Sit/Wall test": 1, 
    "Hip abductors 2": 14,  
}


def get_score_txt(score, protocol):
    if protocol == "UEFA CORE":
        if score <= 5:
            return "Excellent"
        elif score <= 10:
            return "Very good"
        elif score <= 20:
            return "Good"
        elif score <= 30:
            return "Poor"
        elif score <= 100:
            return "Very poor"

    elif protocol == "UEFA20":
        if score <= 10:
            return "Excellent"
        elif score <= 20:
            return "Very good"
        elif score <= 30:
            return "Good"
        elif score <= 40:
            return "Poor"
        elif score <= 140:
            return "Very poor"
        
    elif protocol == "CC25":
        if score <= 15:
            return "Excellent"
        elif score <= 25:
            return "Very good"
        elif score <= 35:
            return "Good"
        elif score <= 45:
            return "Poor"
        elif score <= 200:
            return "Very poor"
        
        


    