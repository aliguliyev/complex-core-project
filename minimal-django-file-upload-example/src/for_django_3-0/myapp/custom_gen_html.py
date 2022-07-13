from bs4 import BeautifulSoup
import os
# print curren dir
print(os.getcwd())
html_file = "myapp/convert/cc25_template.html"
with open(html_file, 'r') as f:
    soup = BeautifulSoup(f, 'xml')
out_file = "media/html/output.html"

colors = {
    'green': '#50bf79',
    'orange': '#eb6d0d',
    'red': '#c41e1e'
}

training_ids = {
    'cc25': {
        'Mobility': ['mobility-1', 'mobility-2', 'mobility-3', 'mobility-4', 'mobility-5'],
        'Flexibility': ['flex-1', 'flex-2', 'flex-3', 'flex-4', 'flex-5', 'flex-6'],
        'Coordination & Proprioception': ['cap-1'],
        'Stability & Strength': ['sas-1', 'sas-2', 'sas-3', 'sas-4', 'sas-5', 'sas-6', 'sas-7']
    }
}
circle_ids = {
    'cc25': {
        'Mobility': 'mobility-circle',
        'Flexibility': 'flex-circle',
        'Coordination & Proprioception': 'cap-circle',
        'Stability & Strength': 'sas-circle'
    }
}


def generate_html(final_dict, body_colors, rn_dict):
    # header
    soup.find('tspan', id='name-surname').string = rn_dict['Name']
    soup.find('tspan', id='screening-date').string = rn_dict['Date']
    # score values
    soup.find(
        'tspan', id='overall-score-num').string = str(final_dict['score'])
    soup.find(
        'tspan', id='overall-score-text').string = str(final_dict['score_txt'])
    # score colors
    # --------------------
    # soup.find('text', id='score-text-color').attrs['fill'] = body_colors['score_color'] # change color of score text
    # soup.find('text', id='score-num-color').attrs['fill'] = body_colors['score_color'] # change color of score num
    # --------------------
    # initial scores
    soup.find(
        'tspan', id='shoulder-flexion-score').string = str(rn_dict['Shoulder flexion']['Score'])
    soup.find('tspan', id='t-spine-extension-score').string = str(
        rn_dict['T-spine extension']['Score'])
    soup.find(
        'tspan', id='t-spine-rot-l').string = str(rn_dict['T-spine rotation']['Score']['L'])
    soup.find(
        'tspan', id='t-spine-rot-r').string = str(rn_dict['T-spine rotation']['Score']['R'])
    soup.find(
        'tspan', id='hip-flex-l').string = str(rn_dict['Hip flexion']['Score']['L'])
    soup.find(
        'tspan', id='hip-flex-r').string = str(rn_dict['Hip flexion']['Score']['R'])
    soup.find(
        'tspan', id='hip-ext-l').string = str(rn_dict['Hip extension']['Score']['L'])
    soup.find(
        'tspan', id='hip-ext-r').string = str(rn_dict['Hip extension']['Score']['R'])
    soup.find(
        'tspan', id='hip-exorot-l').string = str(rn_dict['Hip exorotation']['Score']['L'])
    soup.find(
        'tspan', id='hip-exorot-r').string = str(rn_dict['Hip exorotation']['Score']['R'])
    soup.find(
        'tspan', id='hip-endo-l').string = str(rn_dict['Hip endorotation']['Score']['L'])
    soup.find(
        'tspan', id='hip-endo-r').string = str(rn_dict['Hip endorotation']['Score']['R'])
    soup.find('tspan', id='ankle-dorsi-l').string = str(
        rn_dict['Ankle dorsiflexion']['Score']['L'])
    soup.find('tspan', id='ankle-dorsi-r').string = str(
        rn_dict['Ankle dorsiflexion']['Score']['R'])
    soup.find(
        'tspan', id='pectoralis-score').string = str(rn_dict['Pectoralis']['Score'])
    soup.find(
        'tspan', id='hip-flexor-l').string = str(rn_dict['Hip flexor']['Score']['L'])
    soup.find(
        'tspan', id='hip-flexor-r').string = str(rn_dict['Hip flexor']['Score']['R'])
    soup.find(
        'tspan', id='quadriceps-l').string = str(rn_dict['Quadriceps']['Score']['L'])
    soup.find(
        'tspan', id='quadriceps-r').string = str(rn_dict['Quadriceps']['Score']['R'])
    soup.find(
        'tspan', id='adductors-score').string = str(rn_dict['Adductors']['Score'])
    soup.find(
        'tspan', id='hamstrings-l').string = str(rn_dict['Hamstrings']['Score']['L'])
    soup.find(
        'tspan', id='hamstrings-r').string = str(rn_dict['Hamstrings']['Score']['R'])
    soup.find(
        'tspan', id='sit-reach-score').string = str(rn_dict['Sit & Reach']['Score'])
    soup.find(
        'tspan', id='sit-wall-test-score').string = str(rn_dict['Sit/Wall test']['Score'])
    soup.find(
        'tspan', id='1-leg-stand-l').string = str(rn_dict['1-leg stand']['Score']['L'])
    soup.find(
        'tspan', id='1-leg-stand-r').string = str(rn_dict['1-leg stand']['Score']['R'])
    soup.find(
        'tspan', id='ventral-core-score').string = str(rn_dict['Ventral core']['Score'])
    soup.find(
        'tspan', id='dorsal-core-score').string = str(rn_dict['Dorsal core']['Score'])
    soup.find(
        'tspan', id='lateral-core-l').string = str(rn_dict['Lateral core']['Score']['L'])
    soup.find(
        'tspan', id='lateral-core-r').string = str(rn_dict['Lateral core']['Score']['R'])
    soup.find('tspan', id='hip-abductors-1-l').string = str(
        rn_dict['Hip abductors 1']['Score']['L'])
    soup.find('tspan', id='hip-abductors-1-r').string = str(
        rn_dict['Hip abductors 1']['Score']['R'])
    soup.find('tspan', id='hip-abductors-2-l').string = str(
        rn_dict['Hip abductors 2']['Score']['L'])
    soup.find('tspan', id='hip-abductors-2-r').string = str(
        rn_dict['Hip abductors 2']['Score']['R'])
    soup.find(
        'tspan', id='hip-extensors-l').string = str(rn_dict['Hip extensors']['Score']['L'])
    soup.find(
        'tspan', id='hip-extensors-r').string = str(rn_dict['Hip extensors']['Score']['R'])
    soup.find(
        'tspan', id='leg-axis-l').string = str(rn_dict['Leg axis']['Score']['L'])
    soup.find(
        'tspan', id='leg-axis-r').string = str(rn_dict['Leg axis']['Score']['R'])

    # --------------------
    # trainings
    for group in final_dict['training']:
        group_l = final_dict['training'][group].__len__()
        if group_l == 0:
            t_id = training_ids['cc25'][group][0] + '-text'
            soup.find('tspan', id=t_id).string = 'No recommendations'
            t_id = circle_ids['cc25'][group]
            soup.find('circle', id=t_id).attrs['style'] = 'display: none;'
        else:
            for i in range(group_l):
                training_id = training_ids['cc25'][group][i] + '-text'
                # print(training_id)
                soup.find('tspan', id=training_id).string = str(
                    final_dict['training'][group][i])
            for i in training_ids['cc25'][group][group_l:]:
                soup.find('g', id=i).attrs['style'] = 'display: none;'
    # --------------------
    # colors
    # overall score
    scores_colors = {
        "Excellent": '#50bf79',
        "Very good": '#50bf79',
        "Good": '#eb6d0d',
        "Poor": '#c41e1e',
        "Very poor": '#c41e1e',
    }

    score_num_x = {
        1: 58.083,
        2: 45.083,
    }

    if len(str(final_dict['score'])) == 3:
        pass
    else:
        soup.find('text', id='score-num-x').attrs['transform'] = 'translate(' + str(
            score_num_x[len(str(final_dict['score']))]) + ' 137.379)'

    for text, rect in zip(soup.find_all("text", class_='score-color'), soup.find_all("g", class_='score-color')):
        rect.attrs['stroke'] = scores_colors[final_dict['score_txt']]
        text.attrs['fill'] = scores_colors[final_dict['score_txt']]
    # bodychart

    def col_sort(col_l, col_r):
        if 'red' in [col_l, col_r]:
            return 'red'
        elif 'orange' in [col_l, col_r]:
            return 'orange'
        else:
            return 'green'
    for key in body_colors:
        if type(body_colors[key]) == str:
            try:
                soup.find('path', id=str(
                    key)).attrs['style'] = 'fill: ' + colors[body_colors[key]] + ';'
            except:
                soup.find('path', id=str(
                    key)+'-l').attrs['style'] = 'fill: ' + colors[body_colors[key]] + ';'
                soup.find('path', id=str(
                    key)+'-r').attrs['style'] = 'fill: ' + colors[body_colors[key]] + ';'
        elif type(body_colors[key]) == dict:
            s3 = soup.find('path', id=str(key))
            if s3 is not None:
                soup.find('path', id=str(key)).attrs['style'] = 'fill: ' + colors[col_sort(
                    body_colors[key]['L'], body_colors[key]['R'])] + ';'
            else:
                soup.find(id=str(
                    key)+'-l').attrs['style'] = 'fill: ' + colors[body_colors[key]['L']] + ';'
                soup.find(id=str(
                    key)+'-r').attrs['style'] = 'fill: ' + colors[body_colors[key]['R']] + ';'

    # additional info
    print(final_dict['Additional Information'])
    recommendations_list = final_dict['Additional Information'].split('|')
    str_limit = int()
    for recommendation in recommendations_list:
        if len(recommendation) < str_limit:
            # write to the i-th tspan
            pass

    with open(out_file, 'w') as f:
        f.write(str(soup))

    return out_file
