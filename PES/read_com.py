import serial
import time
import serial.tools.list_ports as port_list

# List available ports
ports = list(port_list.comports())
print("Available ports:", ports)

# List of common baud rates to try
baud_rates = [19200, 38400, 57600, 115200]
# baud_rates = [9600, 19200, 38400, 57600, 115200]
port = 'COM4'  # Replace with your serial port (e.g., /dev/ttyUSB0 on Linux)

def test_baud_rate(port, baud_rate):
    """Attempt to connect to the specified port with a given baud rate."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        if ser.isOpen():
            print(f"Successfully connected at baud rate: {baud_rate}")
            return ser
    except serial.SerialException as e:
        print(f"Failed to connect at baud rate {baud_rate}: {e}")
        return None

def write_to_com(ser, message):
    """Write a message to the serial port."""
    try:
        ser.write(bytes(message.encode('utf-8')))
        print(f"Sent: {message}")
    except serial.SerialException as e:
        print(f"Error writing to serial port: {e}")

# Try connecting with each baud rate
for rate in baud_rates:
    print(f"Testing baud rate {rate}...")
    ser = test_baud_rate(port, rate)
    if ser:
        # If connection is successful, read and write data
        try:
            while True:
                try:
                    # Read a line of data from the serial port
                    data = ser.readline()
                    if data:
                        try:
                            # Attempt to decode data as UTF-8
                            decoded_data = data.decode('utf-8').strip()
                            print(f"Received: {decoded_data}")
                            # for ch in decoded_data:
                            #     print(ord(ch), " "),
                        except UnicodeDecodeError as e:
                            print(f"Error decoding data: {e}. Raw data: {int.from_bytes(data, byteorder='big', signed=False)}")
                except KeyboardInterrupt:
                    print("Exiting the program.")
                    break
                except serial.SerialException as e:
                    print(f"Serial port error: {e}")
                    break
        except KeyboardInterrupt:
            print("Program interrupted.")
        finally:
            ser.close()
        break  # Exit after successful connection
    time.sleep(2)  # Wait for 2 seconds before trying next baud rate
