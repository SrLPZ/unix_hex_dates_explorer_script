import struct
from datetime import datetime
import sys

def find_dates_in_hex(hex_string):
    dates_found = []

    for i in range(len(hex_string) - 3):
        date_le = int.from_bytes(hex_string[i:i+4], byteorder='little')
        date_be = int.from_bytes(hex_string[i:i+4], byteorder='big')
        
        hex_substr = hex_string[i:i+4].hex().upper()
        
        dates_found.append((date_le, date_be, hex_substr))
    
    return dates_found

def format_date(epoch_time):
    formatted_date = datetime.fromtimestamp(epoch_time).strftime('%d-%m-%Y %H:%M')
    return formatted_date

if len(sys.argv) != 2:
    print("Usage: python dates.py hex_input")
    print("Example: python dates.py 605E070864EE26F60884C146722E0AB1")
else:
    hex_string = sys.argv[1]
    hex_bytes = bytes.fromhex(hex_string)
    
    if len(hex_bytes) < 4:
        print("Error: Hexadecimal input must have at least 4 bytes.")
        sys.exit(1)
    
    dates_found = find_dates_in_hex(hex_bytes)
    
    if dates_found:
        print("Unix hex timestamps found:")
        for index, (date_le, date_be, hex_substr) in enumerate(dates_found):
            formatted_date_le = format_date(date_le)
            formatted_date_be = format_date(date_be)
            print(f"Hex: {hex_substr} (Little Endian): {formatted_date_le}")
            print(f"Hex: {hex_substr} (Big Endian)   : {formatted_date_be}")
    else:
        print("No dates found")