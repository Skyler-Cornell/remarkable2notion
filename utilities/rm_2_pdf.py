import subprocess

def rm2pdf_convert(rm_source, pdf_dest, pdf_template):
    """
    Converets a bundle of rM files into a standard PDF and saves to destination
    rm_source: relative path to folder containing all notebook files
    pdf_dest: relative path (including file name) to where the generated pdf will be placed
    """
    subprocess.run(['./rm2pdf', '-t', pdf_template, rm_source, pdf_dest])
