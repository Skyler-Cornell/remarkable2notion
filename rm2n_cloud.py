from rmapy.api import Client
from rmapy.document import Document
import pprint 
def main():
    rmapy = Client()
    rmapy.renew_token()
    print("rM Authenticated:", rmapy.is_auth())
    collection = rmapy.get_meta_items()

    newFile  = open("filename.txt", "w")

    newFile.write("sup")

    pp = pprint.PrettyPrinter(indent=4)
    for item in collection:
        if item.VissibleName == "DSP Scratch Pad":
            print(item.ID)
            zippy = rmapy.download(item)
            content = zippy.content
            rm = zippy.rm
            print(rm[0].page)
            #pp.pprint(content)
            

main()