from rmapy.api import Client

def main():
    rmapy = Client()
    rmapy.is_auth()
    rmapy.register_device('rpympnla')


    rmapy.is_auth()
main()