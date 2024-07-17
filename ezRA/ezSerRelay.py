programName = 'ezSerRelay240714a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezCol Serial Switcher program,
#   Switch serial relay.
# https://github.com/tedcline/ezRA

# Copyright (c) 2024, Ted Cline   TedClineGit@gmail.com

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# 240714a, for Linux serial USB relay, from Richard Cochois
#   "works on Debian 12 'Python 3.11.2' (BunsenLabs Boron)"

#########################################################################################

import serial
import argparse

# Note: No permition required excepted membership of the dialout group:
# sudo usermod -aG dialout your_login

def main():
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description="change relay state using serial port.")
    parser.add_argument('port', type=str, default="/dev/ttyUSB0", help="The relay serial port (e.g., /dev/ttyUSB0)")
    parser.add_argument('baudrate', type=int, default=9600, help="The baud rate for serial communication")
    parser.add_argument('relay', type=int, choices=range(0, 2), help="New relay state to send")

    # Predefined commands
    sw_off = b"\xA0\x01\x00\xA1"
    sw_on  = b"\xA0\x01\x01\xA2"

    args = parser.parse_args()

    try:
        # Serial connection configuration
        ser = serial.Serial(port=args.port, baudrate=args.baudrate, timeout=1)

        if not ser.is_open:
            print(f"Unable to open serial connection on {args.port}")
            return

        # Send the command
        if 1 == args.relay:
          #print(f"ON")
          ser.write(sw_on)
        else:
          #print(f"OFF")
          ser.write(sw_off)

        # Close the serial connection
        ser.close()

    except serial.SerialException as e:
        print(f"Error during switcher serial communication: {e}")

if __name__ == "__main__":
    main()

