import os

import pandas as pd
import XlsxWriter as xw

import static

os.system("cls")

data = pd.read_excel("./src/cc25_2.xlsx")

protocol = data.iloc[0][0]
venue = data.iloc[1][0]
date = data.iloc[2][0]
def generate_single_result(row):
    # This function shoud form the test results to an old form and perform the training recomendations calculation and writing to excel
    pass


def generate_stats(rows):
    height = len(rows)
    width = len(rows[0])
    stats = []
    for i in range(2, width):
        s = 0
        for row in rows:
            s += row[i]
        stats.append(s/height)
    return stats


ln = {
    "CC25" : 38,
    "UEFA20" : 34,
    "UEFA CORE" : 24
}

# row: [name, birthdate, tests..]
rows = []
for i in range(6, len(data)):
    tests = []
    sum_res = 0
    row = [data.iloc[i][0], data.iloc[i][1]]
    for j in range(2, ln[protocol]):
        score = data.iloc[i][j]
        row.append(score)
        sum_res += score
    generate_single_result(row)
    row.append(sum_res)
    row.append(static.get_score_txt(sum_res))
    rows.append(row)

stats = generate_stats(rows)
stats_list = ["STATS", ""]
for s in stats:
    stats_list.append(s)

def write_result(res):
    # This function should copy the input excel and add scores and stats
    wbname = protocol + "_" + venue + "_" + date
    wb = xw.Workbook("./results/" + wbname)
    ws = wb.add_worksheet()
    # Header of the file
    ws.write(0, 0, protocol)
    ws.write(1, 0, venue)
    ws.write(2, 0, date)
    for i in range([5,6]):
        for j in range(len(ln(protocol)) + 3):
            ws.write(i, j, res[i][j])
    # ------------------
    for i in range(len(res)):
        for j in range(len(res[i])):
            ws.write(i + 6, j, res[i][j])
fin_list = rows + stats_list

write_result(fin_list)


