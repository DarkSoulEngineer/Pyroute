# Pyroute
**A Python routing algorithm that finds the optimal path between two MAC addresses in a nested JSON hierarchy.**

[![License: GPL v3](https://img.shields.io/github/license/DarkSoulEngineer/Pyroute)](LICENSE)
![Python](https://img.shields.io/badge/language-Python%203.x-3776AB)

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

Pyroute is a Python script that finds routes between network devices using their MAC addresses. It reads a network topology defined as a nested JSON hierarchy, traces devices and their parent chains, and calculates the route between two devices — including common parents — through complex network structures.

### Features

- **Search Devices**: Locate a device by its MAC address in the network hierarchy.
- **Parent Chain**: Track the parent chain of a device.
- **Route Calculation**: Find the route between two devices, including common parents.

## Requirements

- **Python 3.x**

No third-party packages are required; the script uses only the standard library.

## Installation

Clone the repository and use the code directly:

```bash
git clone https://github.com/DarkSoulEngineer/Pyroute.git
cd Pyroute
```

## Usage

Run the script with the network topology provided in `network.json`:

```bash
python main.py
```

The script reads `network.json`, computes the route between the start and end MAC addresses defined in `main.py`, and prints the routing list along with the number of hops.

### Example Network

The provided `network.json` describes the following topology:

```
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
```

## License

GPL-3.0 — see [LICENSE](LICENSE).
