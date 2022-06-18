import pandas as pd
import static
import os
import xlsxwriter as xw
import datetime


os.system("cls")

data = pd.read_excel("./src/core.xlsx")

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


rows = []
for i in range(6, len(data)):
    tests = []
    sum_res = 0
    row = [data.iloc[i][0], data.iloc[i][1]]
    for j in range(2, ln[protocol]):
        score = data.iloc[i][j]
        row.append(score)
        sum_res += score
    row.append(sum_res)
    row.append(static.get_score_txt(sum_res))
    rows.append(row)
    generate_single_result(row)

stats = generate_stats(rows)
stats_list = ["STATS", ""]
for s in stats:
    stats_list.append(s)

def write_result(res):
    # This function should copy the input excel and add scores and stats
    pass

fin_list = rows + stats_list

write_result(fin_list)


