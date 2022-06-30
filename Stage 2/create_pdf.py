from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
drawing = svg2rlg("./assets/Result sheets-UEFA.svg")
renderPDF.drawToFile(drawing, "file.pdf")


result_color = {
    0: "",
    3: "",
    5: ""
}
