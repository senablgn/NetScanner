
# NetScanner

NetScanner is a Python application that uses the Scapy library to scan devices within a specified network range. This tool allows you to discover active devices on the specified network and optionally provides a graphical output.

## Features
- Scan for active devices in the specified network range
- Optional graphical output

## Requirements
- Python 3.x
- Scapy
- (Optional) WinPcap or libpcap (for packet sniffing on Windows or Linux)

## Installation
You can install the required libraries using the following command:

```bash
pip install scapy
```
 
## Usage
To run NetScanner, use the following command in your terminal:
``` python netScanner.py -n [network_range] [-g] ```

-n or --network: Specifies the network range to scan (e.g., 192.168.1.0/24).
-g or --graph: Enables graphical output. If this parameter is not specified, graphical output will not be provided     


