import argparse
import sys
import socket
import serial

def setup_client(address, port):
    """ Sets up a client on a specific IP/port """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {address}:{port}")
    client.connect((address, port))
    return client


def read_one(client):
    """ Read a single byte from the client """
    return client.recv(1)

def read_loop(client):
    while True:
        print(read_one(client))

def main():
    """ Hi Lewis!!! """
    parser = argparse.ArgumentParser(
        description="Reads from the TCP bridge server")

    parser.add_argument("--address", required="True",
                        help="Address to connect to for data")
    parser.add_argument("--port", type=int, default=7000,
                        help="Port number to host over")
    args = parser.parse_args()

    client = None
    try:
        client = setup_client(args.address, args.port)
        read_loop(client)

    except ValueError:
        print(f"Invalid port: {sys.argv[1]}. Use: 1000 - 60000.")
    except Exception as exc:
        print(f"{exc}")
    finally:
        if client is not None:
            try:
                client.shutdown(socket.SHUT_RDWR)
            except:
                pass
            try:
                client.close()
            except:
                pass

if __name__ == "__main__":
    main()