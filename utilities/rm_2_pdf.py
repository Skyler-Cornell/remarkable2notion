import subprocess
import rmapy
import os
def rm2pdf_convert(rm_source, pdf_dest, pdf_template):
    """
    Converets a bundle of rM files into a standard PDF and saves to destination
    rm_source: relative path to folder containing all notebook files
    pdf_dest: relative path (including file name) to where the generated pdf will be placed
    """
    subprocess.run(['./rm2pdf', '-t', pdf_template, rm_source, pdf_dest])


def zipDocument2folder(zip,folder_path):
    """
    parses the raw rm document dat in a zipDocument (rmapy) and saves the contents into 
    a "remarkable bundle", which is just a folder containing everything needed for rm2pdf to 
    convert the raw notebook files to pdf
    zip: zipDocument object for the desired_notebook
    folder_path: path where the generated bundle folder should be placed
    """

    # mkdirs for rm pages folder f9299a23-adbf-4561-b14a-c57c161243de 
    #   inside there write the contents of each rm.pages page and name accordingly
    # Write contents of the outer .metadata, .content, .pages, etc

    # all of this goes into the specifiec folder_path
    newFile  = open("folder/filename.txt", "w")
    newFile.write("sup")

