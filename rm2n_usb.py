import pysftp
import os
import subprocess

from utilities.rm_2_pdf import rm2pdf_convert

def main():
    # HOST = '10.11.99.1'
    # #HOST = '130.58.108.145'
    # USERNAME = 'root'
    # PASSWORD = 'fPsUJe8rQx'
    # cwd = os.getcwd()
    rm2pdf_convert('rm_bundles/f9299a23-adbf-4561-b14a-c57c161243de', 'generated_pdfs/generated.pdf', 'pdf_templates/A4.pdf')
    # with pysftp.Connection(host=HOST, username=USERNAME, password=PASSWORD) as sftp:
    #     print("sucessful connection")
    #     #sftp.get_r('.local/share/remarkable/xochitl/f9299a23-adbf-4561-b14a-c57c161243de',cwd)
    #     sftp.get_r('.local/share/remarkable/xochitl/f9299a23-adbf-4561-b14a-c57c161243de.thumbnails',cwd)
    
        #sftp.get('.local/share/remarkable/xochitl/f9299a23-adbf-4561-b14a-c57c161243de.pagedata')
        #sftp.get('.local/share/remarkable/xochitl/f9299a23-adbf-4561-b14a-c57c161243de.content')
        #sftp.get('.local/share/remarkable/xochitl/f9299a23-adbf-4561-b14a-c57c161243de.metadata')




main()