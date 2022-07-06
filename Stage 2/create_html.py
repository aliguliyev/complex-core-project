# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF
# drawing = svg2rlg("./assets/Result_sheets_UEFA.svg")
# renderPDF.drawToFile(drawing, "file.pdf")



from bs4 import BeautifulSoup
with open("./assets/convert/res.html", 'r') as f: 
    soup = BeautifulSoup(f, 'xml')
new_name = "Manema Jeff"
name_surname = soup.find("tspan", {"id":"Name_Surname"})
name_surname.string = new_name
with open("./assets/convert/res2.html", 'w') as f:
    f.write(str(soup))
# new_sheet = soup
# svg_text = new_sheet.text
# name = "New Name".replace(" ", "_")

# file_name = "./assets/convert/" + name + "_result_sheet.svg"
# with open(file_name, "w") as rf:
#     rf.write(svg_text)


