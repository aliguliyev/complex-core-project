from cmath import nan
import os
from typing import final
from numpy import short

import pandas as pd
import xlsxwriter as xw

import static

os.system("cls")

data = pd.read_excel("./src/core2.xlsx")

protocol = data.columns[0]
# print(data)
venue = data.iloc[0][1]
date = data.iloc[1][1]

def write_result_to_excel(final_dict, body_colors, rn_dict):
    # print(body_colors)
    results = final_dict
    colors = body_colors
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
    ws.write(3, 0, "Birth Date")
    ws.write(3, 1, rn_dict["Birth Date"])
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

    h = max(height, default=0)
    ws.write(9+h+3, 0, "Additional Information : ")
    ws.write(9+h+3, 1, str(results["Additional Information"]))

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
    

def generate_single_result(row):
    print("Generating result for row:\n", row, "\n")
    if protocol == "UEFA CORE":
        r_dict = dict.fromkeys(list(static.uefa_core.keys()) + ["Additional Information"], 0)
    elif protocol == "UEFA20":
        r_dict = dict.fromkeys(list(static.uefa_core.keys()) + list(static.uefa_20.keys()) + ["Additional Information"], 0)
    elif protocol == "CC25":
        r_dict = dict.fromkeys(list(static.uefa_core.keys()) + list(static.uefa_20.keys()) + list(static.cc25.keys()) + ["Additional Information"], 0)
    # This function shoud form the test results to an old form and perform the training recomendations calculation and writing to excel
    keys = list(r_dict.keys())
    # new_keys = list(static.tr_shorts.keys())
    common_keys = ["Name", "Birth Date", "Date", "Venue"]
    rn_dict = dict.fromkeys(common_keys, 0)
    rn_dict["Name"] = row[0]
    rn_dict["Birth Date"] = row[1]
    rn_dict["Date"] = date
    rn_dict["Venue"] = venue
    to_continue = False
    for i in range(2, len(row) - 2):
        # input("Press Enter to continue...")
        if to_continue:
            to_continue = False
            continue
        # print(i, ":", row[i])
        # shorts_set = set()
        short = data.iloc[4][i]
        # print("Short:", short)
        if short == "Additional Information":
            continue
        
        test = static.tr_shorts[short]
        if static.types[test] == "1":
            # print("\n-------------\n",i, "\n",row[i])
            rn_dict[test] = {"Score" : row[i]}
            # print("Added to", test, ":", row[i])
            to_continue = False
        elif static.types[test] == "2":
            # print("\n-------------\n",i,"\nL:", row[i])
            # print("R:", row[i+1], "\n-------------")

            rn_dict[test] = {
                "Score" : {
                    "L" : row[i],
                    "R" : row[i + 1]
                    }
                }
            # print("Added to", test, ":", row[i], "|", row[i + 1])
            to_continue = True
        # input("Press Enter to continue...")
        # print("\n-------------\n",rn_dict[test])

    print("Generated result dictionary")
    # for rk in rn_dict:
    #     print(rk, ":", rn_dict[rk])
    # print(rn_dict)
    # pasted
    final_dict = {
        "score": 0,
        "score_txt": "",
        "training": {
            "Mobility": set(),
            "Flexibility": set(),
            "Coordination & Proprioception": set(),
            "Stability & Strength": set()
        },
        "Additional Information": row[-1],
    }
    body_colors = {}
    score = 0
    
    # for key in rn_dict:
    #     print(key, ":", rn_dict[key])
    
    for key in rn_dict:
        if key in common_keys:
            continue
        elif key == "Additional Information":
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
            # print("\n-------------\n" + key)
            t_score = rn_dict[key]["Score"]
            body_part = static.body_parts[key]
            # print("Body part:", body_part)
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
                # print(body_colors[body_part])
                # print(rn_dict[key])
                body_colors[body_part]["L"].append(rn_dict[key]["Score"]["L"])
                body_colors[body_part]["R"].append(rn_dict[key]["Score"]["R"])
            else:
                body_colors[body_part] = {
                    "C" : [],
                    "L" : [rn_dict[key]["Score"]["L"]],
                    "R" : [rn_dict[key]["Score"]["R"]]
                }
        # print("\n-------------\n", body_colors[body_part])
        # input("Press Enter to continue...")
            # body_colors[body_part].append(rn_dict[key]["Score"]["L"])
            # body_colors[body_part].append(rn_dict[key]["Score"]["R"])
          
        score += t_score
        if t_score > 0:
            for t in t_protocol[key]["training"]:
                if t == 11:
                    final_dict["training"]["Flexibility"].add("Calf")
                    continue
                final_dict["training"][t_group].add(static.trainings[t_group][str(t)])
    final_dict["score"] = score
    final_dict["score_txt"] = static.get_score_txt(score, protocol)
    for key in final_dict["training"]:
        final_dict["training"][key] = list(final_dict["training"][key])
    # print(body_colors)
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
            # os.system("cls")
            # print(final_dict)
            # print(key)
            # print(max(body_colors[key]["R"]))
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
    # return final_dict, body_colors
    write_result_to_excel(final_dict, body_colors, rn_dict)
    # -----------------
    




def generate_stats(rows):
    height = len(rows)
    width = ln[protocol]
    stats = []
    # for row in rows:
    #     print(row)
    # input("Press Enter to continue...")
    for i in range(2, width + 3):
        s = 0
        for row in rows:
            # os.system("cls")
            # print(s, ",",row[i])
            s += row[i]
        stats.append(s/height)
    # print(["Stats", ""] + stats)
    return stats


ln = {
    "CC25" : 38,
    "UEFA20" : 34,
    "UEFA CORE" : 24
}

# row: [name, birthdate, tests..]
rows = []
for i in range(5, len(data)):
    
    os.system("cls")
    # continue
    tests = []
    sum_res = 0
    row = [data.iloc[i][0], data.iloc[i][1]]
    for j in range(2, 2 + ln[protocol]):
        score = data.iloc[i][j]
        
        row.append(score)
        sum_res += score
    # print(row)
    row.append(sum_res)
    row.append(static.get_score_txt(sum_res, protocol))
    row.append(data.iloc[i][2 + ln[protocol]])
    generate_single_result(row)
    rows.append(row)

stats = generate_stats(rows)
stats_list = ["STATS", ""]
for s in stats:
    stats_list.append(s)

def write_result(res):
    # This function should copy the input excel and add scores and stats
    wbname = protocol + "_" + venue + "_" + date
    wb = xw.Workbook("./results/" + wbname + ".xlsx")
    ws = wb.add_worksheet()
    # Header of the file
    ws.write(0, 0, protocol)
    ws.write(1, 0, "Venue")
    ws.write(1, 1, venue)
    ws.write(2, 0, "Date")
    ws.write(2, 1, date)
    for i in [4,5]:
        # print(res[i])
        for j in range(len(data.iloc[i])):
            to_write = data.iloc[i-1][j]
            try:
                ws.write(i, j, to_write)
            except TypeError:
                ws.write(i, j, "")
    ws.write(5, 2 + ln[protocol], "Result")
    ws.write(5, 3 + ln[protocol], "Result")
    ws.write(5, 4 + ln[protocol], "Additional Information")
    # ------------------
    for i in range(len(res)):
        for j in range(len(res[i])):
            ws.write(i + 6, j, res[i][j])
    wb.close()
fin_list = rows + [stats_list]

write_result(fin_list)


