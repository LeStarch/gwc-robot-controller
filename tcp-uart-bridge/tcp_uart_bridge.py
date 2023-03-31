import argparse
import sys
import socket
import serial

def setup_server(port, address="0.0.0.0"):
    """ Stets up a server on a specific IP/port """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, port))
    print(f"Listening on port {address}:{port}")
    server.listen(1)
    return server

def setup_serial(device):
    """ Open the serial port """
    serial_port = serial.Serial(timeout=0.0100)
    serial_port.port = device
    serial_port.baudrate = 115200
    serial_port.timeout = 0.010
    serial_port.write_timeout = 0.010
    serial_port.inter_byte_timeout = 0.010
    return serial_port

def send_loop(server: socket.socket, serial_port: serial.Serial):
    """ Loop to send data until CTRL-C """
    try:
        while True:
            print(f"Opening {serial_port.port} at rate {serial_port.baudrate} bps")
            serial_port.open()

            print(f"Awaiting client connection")
            (client, _) = server.accept()
            try:
                while True:
                    one_byte = serial_port.read(1)
                    client.send(one_byte)
            except BrokenPipeError:
                pass
            except serial.SerialException:
                pass
            finally:
                try:
                    client.shutdown(socket.SHUT_RDWR)
                except:
                    pass
                try:
                    client.close()
                except:
                    pass
                try:
                    serial_port.close()
                except:
                    pass
    finally:
        try:
            server.shutdown(socket.SHUT_RDWR)
        except:
            pass
        try:
            server.close()
        except:
            pass
        try:
            serial.close()
        except:
            pass

def main():
    """ Hi Lewis!!! """
    parser = argparse.ArgumentParser(
        description="Bridge the data read on a UART socket to a TCP client")
    parser.add_argument("--port", type=int, default=7000,
                        help="Port number to host over")
    parser.add_argument("--device", default="/dev/ttyACM0",
                        help="TTY serial device of source data")
    args = parser.parse_args()


    try:
        server = setup_server(args.port)
        serial = setup_serial(args.device)

        send_loop(server, serial)

    except ValueError:
        print(f"Invalid port: {sys.argv[1]}. Use: 1000 - 60000.")
    except Exception as exc:
        print(f"{exc}")
        raise

if __name__ == "__main__":
    main()