from cmath import nan
import os

import pandas as pd
import xlsxwriter as xw

import static

os.system("cls")

data = pd.read_excel("./src/cc25_2.xlsx")

protocol = data.columns[0]
# print(data)
venue = data.iloc[0][1]
date = data.iloc[1][1]
def generate_single_result(row):
    # This function shoud form the test results to an old form and perform the training recomendations calculation and writing to excel
    pass


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
    # ------------------
    for i in range(len(res)):
        for j in range(len(res[i])):
            ws.write(i + 6, j, res[i][j])
    wb.close()
fin_list = rows + [stats_list]

write_result(fin_list)


