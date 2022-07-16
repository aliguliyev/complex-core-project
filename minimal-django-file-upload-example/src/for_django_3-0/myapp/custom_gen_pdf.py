import pdfkit
from django.conf import settings
import os
proot = settings.BASE_DIR
"""
"media/html/output.html"
"""


def generate_pdf(html):
    print("project_root: ", proot)
    print(html)
    pdf = os.path.join(proot, "media/results/" +
                       html.replace('.html', '.pdf').split("/")[-1])
    html = os.path.join(proot, html)
    options = {
        "enable-local-file-access": None,
        'page-size': 'A2',
        # 'dpi':600,
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',


        # 'disable-smart-shrinking': None,
    }

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file(html, pdf, options=options)
    return pdf
