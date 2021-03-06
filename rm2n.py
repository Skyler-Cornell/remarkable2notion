import pysftp

def main():
    HOST = '10.11.99.1'
    USERNAME = 'root'
    PASSWORD = 'fPsUJe8rQx'
    cwd = os.getcwd()

    with pysftp.Connection(host=HOST, username=USERNAME, password=PASSWORD) as sftp:
        print("sucessful connection")
        sftp.get_r('/usr/share/remarkable/', cwd)


main()