import subprocess

def rm2pdf_convert(rm_source, pdf_destination, template_file):
    subprocess.run(['./rm2pdf', '-t', template_file, rm_source, pdf_destination])
