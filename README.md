# PyRoute: Device Routing in Network Hierarchies

**PyRoute** is a Python library designed for navigating network hierarchies and finding routes between devices based on their MAC addresses. The library allows you to search for devices, track their parent-child relationships, and determine routes between two devices by finding common parents.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Find Device](#find-device)
  - [Route to Parent](#route-to-parent)
  - [Create Routing List](#create-routing-list)
  - [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

PyRoute enables you to model and query a hierarchical network structure, where devices are represented by their **MAC addresses** and **children** devices. This tool can be particularly useful for network administrators, cybersecurity professionals, or anyone who needs to analyze network structures and find paths between devices.

---

## Features

- **Device Search**: Find a device in the network hierarchy by its MAC address.
- **Parent Chain Tracking**: Trace the chain of parent devices leading to a given device.
- **Route Creation**: Find a route between two devices, including the common parent(s) and the number of hops.
- **Customizable**: Easily adaptable to different network topologies.

---

## Installation

To use **PyRoute**, simply clone the repository or install it via `pip` (if available):

### Clone the repository:

```bash
git clone https://github.com/<your-username>/pyroute.git
cd pyroute
