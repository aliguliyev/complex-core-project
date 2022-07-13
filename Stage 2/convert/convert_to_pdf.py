import pdfkit

options = {
    "enable-local-file-access": None,
    'page-size':'A2',
    # 'dpi':600,
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',


    # 'disable-smart-shrinking': None,
}

config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_file(
    'C:/Users/aguli/OneDrive/Desktop/Complex Core Project/complex-core-project/Stage 2/convert/res.html', 
    'C:/Users/aguli/OneDrive/Desktop/Complex Core Project/complex-core-project/Stage 2/out_screening.pdf',
    options=options
    )