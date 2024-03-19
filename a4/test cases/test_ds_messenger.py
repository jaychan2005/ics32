# Test code for part 2

import ds_messenger


def main():
    server = "168.235.86.101"
    username = "saitama"
    password = "opm"
    msg = ds_messenger.DirectMessenger(server, username, password)

    print(msg.retrieve_new())
    print(msg.retrieve_all())


if __name__ == '__main__':
    main()
