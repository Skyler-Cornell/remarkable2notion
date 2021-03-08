from rmapy.api import Client
from rmapy.document import Document

def main():
    rmapy = Client()
    rmapy.renew_token()
    print("rM Authenticated:", rmapy.is_auth())
    collection = rmapy.get_meta_items()
    for item in collection:
        if item.VissibleName == "DSP Scratch Pad":
            print(item.ID)
            zippy = rmapy.download(item)
            print(zippy.metadata)
            


main()