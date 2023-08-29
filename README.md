# unix_hex_dates_explorer_script
This script searches for date values within a hexadecimal string input. It looks for sequences of 4 bytes (32 bits) in both little endian and big endian formats. Dates are then converted and displayed in the "d-m-Y H:M" format, alongside the corresponding hexadecimal substrings from where they were extracted.

Usage:
python script_name.py hex_input

Ensure that the hexadecimal input is at least 4 bytes long. If valid dates are found, the script will display them along with their corresponding hexadecimal substrings. If no dates are found, it will indicate that as well.

Please note that this script requires the input to be a valid hexadecimal string containing only hexadecimal characters (0-9, A-F).
