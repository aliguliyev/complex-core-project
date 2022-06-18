
import pandas as pd
import static
import os
import xlsxwriter as xw
import datetime
# from . import static 
# from static import get_score_txt
os.system("cls")
files = {
    "1" : "./src/core.xlsx",
    "2" : "./src/uefa20.xlsx",
    "3" : "./src/cc25.xlsx",
}

file = files[input("Choose file (1 - core, 2 - uefa20, 3 - cc25): ")]

data = pd.read_excel(file)
protocol = data.columns[0]
print("Protocol:", protocol)
# print(data)
# input("Press Enter to continue...")

common_keys = ["Name", "Birth Day", "Date", "Venue"]

# Here we assume that the names for the protocols are UEFA CORE, UEFA20, CC25 (case sensitive)
if protocol == "UEFA CORE":
    r_dict = dict.fromkeys(common_keys + list(static.uefa_core.keys()) + ["General Information"], 0)
elif protocol == "UEFA20":
    r_dict = dict.fromkeys(common_keys + list(static.uefa_core.keys()) + list(static.uefa_20.keys()) + ["General Information"], 0)
elif protocol == "CC25":
    r_dict = dict.fromkeys(common_keys + list(static.uefa_core.keys()) + list(static.uefa_20.keys()) + list(static.cc25.keys()) + ["General Information"], 0)
# Personal data




keys = list(r_dict.keys())

rn_dict = dict.fromkeys(common_keys, 0)
rn_dict["Name"] = data.iloc[1][1]
rn_dict["Birth Day"] = data.iloc[2][1]
rn_dict["Date"] = data.iloc[3][1]
rn_dict["Venue"] = data.iloc[4][1]

count = 1
for i in range(len(data)):
    
    current_key = data.iloc[i][0]
    if current_key in common_keys:
        continue
    elif current_key == "General Information":
        rn_dict["General Information"] = data.iloc[i][1]
        continue
    elif current_key in keys:
        if static.types[current_key] == "1":
            rn_dict[current_key] = {'Score' : int(data.iloc[i][1])}
            
        elif static.types[current_key] == "2":
            rn_dict[current_key] = {'Score' : {
                            "L" : int(data.iloc[i][1].replace("L ", "")),
                            "R" : int(data.iloc[i][2].replace("R ", ""))
                        }}
print("\n\n")
for key in rn_dict:
    print(key, ":", rn_dict[key])


def generate_result():
    final_dict = {
        "score": 0,
        "score_txt": "",
        "training": {
            "Mobility": set(),
            "Flexibility": set(),
            "Coordination & Proprioception": set(),
            "Stability & Strength": set()
        },
        "General Information": rn_dict["General Information"],
    }
    body_colors = {}
    score = 0
    
    
    for key in rn_dict:
        if key in common_keys:
            continue
        elif key == "General Information":
            continue
        elif key in static.uefa_core:
            t_protocol = static.uefa_core
            t_group = static.uefa_core[key]["group"]
        elif key in static.uefa_20:
            t_protocol = static.uefa_20
            t_group = static.uefa_20[key]["group"]
        elif key in static.cc25:
            t_protocol = static.cc25
            t_group = static.cc25[key]["group"]
        
        # t_group = cc20[key]["group"]
        # t_training = cc20[key]["training"]

        

        if static.types[key] == "1":
            t_score = rn_dict[key]["Score"]
            body_part = static.body_parts[key]
            if body_part in body_colors:
                body_colors[body_part]["C"].append(t_score)
            else:
                body_colors[body_part] = {
                    "C" : [t_score],
                    "L" : [],
                    "R" : []
                }
            # body_colors[body_part].append(t_score)
        elif static.types[key] == "2":
            t_score = rn_dict[key]["Score"]["L"] + rn_dict[key]["Score"]["R"]
            body_part = static.body_parts[key]
            if body_part in body_colors:
                print(body_colors[body_part])
                print(rn_dict[key])
                body_colors[body_part]["L"].append(rn_dict[key]["Score"]["L"])
                body_colors[body_part]["R"].append(rn_dict[key]["Score"]["R"])
            else:
                body_colors[body_part] = {
                    "C" : [],
                    "L" : [rn_dict[key]["Score"]["L"]],
                    "R" : [rn_dict[key]["Score"]["R"]]
                }
            # body_colors[body_part].append(rn_dict[key]["Score"]["L"])
            # body_colors[body_part].append(rn_dict[key]["Score"]["R"])
          
        score += t_score
        if t_score > 0:
            for t in t_protocol[key]["training"]:
                final_dict["training"][t_group].add(static.trainings[t_group][str(t)])
    final_dict["score"] = score
    final_dict["score_txt"] = static.get_score_txt(score, protocol)
    for key in final_dict["training"]:
        final_dict["training"][key] = list(final_dict["training"][key])
    print(body_colors)
    for key in body_colors:
        try:
            c_color = static.colors[max(body_colors[key]["C"])]
        except:
            c_color = ""
        try:
            l_color = static.colors[max(body_colors[key]["L"])]
        except:
            l_color = ""
        try:
            r_color = static.colors[max(body_colors[key]["R"])]
        except:
            r_color = ""
        if l_color == "" and r_color == "":
            body_colors[key] = c_color
        else:
            body_colors[key] = {
            "L" : static.colors[max(body_colors[key]["L"])],
            "R" : static.colors[max(body_colors[key]["R"])]
        }

        #     C_body_color = static.colors[max(body_colors[key]["C"])]
        #     if body_colors[key]["L"] != "":
        #         L_body_color = C_body_color 
        #     body_colors[key]
        # elif static.types[key] == "2":
        #     body_colors[key] = {
        #         "L" : static.colors[max(body_colors[key]["L"])],
        #         "R" : static.colors[max(body_colors[key]["R"])]
        #     }
    return final_dict, body_colors
results, colors = generate_result()
print("\n\n")
for key in results:
    print(key, ":", results[key])
for key in colors:
    print(key, ":", colors[key])

print("Started writing to file...")
wbname = protocol + "_" + rn_dict["Name"].replace(" ", "-") + "_" + rn_dict["Date"] + ".xlsx"
print("File name:", wbname)
wb = xw.Workbook("./results/" + wbname)
ws = wb.add_worksheet()

print("Created worksheet")

ws.write(0, 0, protocol)
ws.write(1, 0, "PERSONAL DATA")
ws.write(2, 0, "Name")  
ws.write(2, 1, rn_dict["Name"])
ws.write(3, 0, "Birth Day")
ws.write(3, 1, rn_dict["Birth Day"])
ws.write(4, 0, "Date")
ws.write(4, 1, rn_dict["Date"])
ws.write(5, 0, "Venue")
ws.write(5, 1, rn_dict["Venue"])
print("Wrote personal data")
ws.write(5, 3, "Score : " + str(results["score"]) + " / " + results["score_txt"])

ws.write(7, 0, "TRAINING RECOMMENDATIONS")
ws.write(8, 0, "Mobility")
ws.write(8, 1, "FLEXIBILITY")
ws.write(8, 2, "COORDINATION & PROPRIOCEPTION")
ws.write(8, 3, "STABILITY & STRENGTH")

height = []
for i in range(len(results["training"]["Mobility"])):
    
    ws.write(9+i, 0, results["training"]["Mobility"][i])
for i in range(len(results["training"]["Flexibility"])):
    height.append(i)
    ws.write(9+i, 1, results["training"]["Flexibility"][i])
for i in range(len(results["training"]["Coordination & Proprioception"])):
    height.append(i)
    ws.write(9+i, 2, results["training"]["Coordination & Proprioception"][i])
for i in range(len(results["training"]["Stability & Strength"])):
    height.append(i)
    ws.write(9+i, 3, results["training"]["Stability & Strength"][i])

h = max(height)
ws.write(9+h+3, 0, "General Information : ")
ws.write(9+h+3, 1, str(results["General Information"]))

lh = 9+h+3

# for key in colors:
#     print(key, ":", colors[key], ":", type(colors[key]))


ws.write(lh+1, 0, "BODY COLORS")
for i, col in zip(range(len(colors)), colors):
    # print(col, ":", colors[col], ":", type(colors[col]))
    # input("Press Enter to continue...")
    if type(colors[col]) == str:
        # print(col, ":", colors[col], ":", type(colors[col]))
        ws.write(lh+2+i, 0, col)
        ws.write(lh+2+i, 1, colors[col])
    elif type(colors[col]) == dict:
        # print(col, ":", colors[col], ":", type(colors[col]))
        ws.write(lh+2+i, 0, col)
        ws.write(lh+2+i, 1, colors[col]["L"])
        ws.write(lh+2+i, 2, colors[col]["R"])
    # ws.write(lh+2+i, 0, col)
    # ws.write(lh+2+i, 1, colors[col])

wb.close()