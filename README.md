# PyRoute: Network Device Routing

**PyRoute** is a Python script that find routes between devices using their MAC addresses. It helps trace devices and their parent chains, enabling you to calculate routes through complex network structures and nasted objects.

# Table of Contents
  - [Requirements](#requirements)
  - [Features](#features)
  - [EXAMPLE NETWORK](#example-network)
  - [Installation](#installation)
  - [Usage](#usage)
  
# Requirements
- **Python 3.x**
---

## Features

- **Search Devices**: Locate a device by its MAC address in the network hierarchy.
- **Parent Chain**: Track the parent chain of a device.
- **Route Calculation**: Find the route between two devices, including common parents.

---


## EXAMPLE NETWORK

                      +--------------------+
                      |  08:3A:8D:D1:C7:8F |
                      |  D1 Mini WEMOS     |
                      +--------------------+
                                |
              +---------------------------------+
              |                                 |
     +-------------------+            +-------------------+
     | 34:5F:45:A8:64:8C |            | 34:5F:45:AA:A4:4C |
     |  Device-1         |            | Device-2          |
     +-------------------+            +-------------------+
              |                                 |
     +-------------------+            +-------------------+
     | 50:6B:AC:44:23:10 |            | 34:5F:45:AA:A4:4C |
     |  Device-1-1       |            | Device-2-1        |
     +-------------------+            +-------------------+
                                                |
                                      +-------------------+
                                      | 60:1A:CD:55:66:77 |
                                      | Device-2-1-1      |
                                      +-------------------+

## Installation

Clone the repository and use the code directly:

```bash
git clone https://github.com/DarkSoulEngineer/pyroute.git
cd pyroute
```

## Usage

```
python main.py
```
