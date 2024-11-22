# Function to find a device and its parent chain
def find_device(network, start_mac, parents=None):
    """
    Find a device in the network hierarchy and return the device along with its parent chain.

    Args:
        network (dict): The network hierarchy represented as a dictionary.
        start_mac (str): The MAC address of the device to find.
        parents (list, optional): A list to keep track of the parent devices in the chain. Defaults to None.

    Returns:
        tuple: A tuple containing:
            - The device dictionary if found, otherwise None.
            - A list of parent devices leading to the found device, or None if not found.
    """

    if parents is None:
        parents = []  # Initialize the parents list

    # Check if the current device's MAC address matches start_mac
    if network["mac_address"] == start_mac:
        return network, parents
    
    # Recursively search through the children
    for child in network["children"]:
        result, parent_list = find_device(child, start_mac, parents + [network])
        if result:
            return result, parent_list
    
    # If no match is found, return None 
    return None, None

def route_to_parent(network, mac, common_parent_mac):
    """
    Find the route from a device (mac) to the common parent (common_parent_mac).
    
    Args:
        network (dict): The network hierarchy.
        mac (str): The MAC address of the starting device.
        common_parent_mac (str): The MAC address of the common parent.
        
    Returns:
        list: The route from the device to the common parent as a list of MAC addresses.
    """
    # Find the device and its parent chain
    device, parents = find_device(network, mac)

    if not device:
        return None  # Device not found
    
    # Add the current device's MAC to the route
    route_to_parent = [device["mac_address"]]
    
    # Traverse the parent chain until the common parent is found
    for parent in reversed(parents):
        route_to_parent.append(parent["mac_address"])
        if parent["mac_address"] == common_parent_mac:
            break
    return route_to_parent

# Function to create a routing list between two devices
def create_routing_list(network, start_mac, end_mac):
    # Return an empty list if the start_mac and end_mac are the same
    if start_mac == end_mac:
        return [start_mac], None

    # Find the start and end devices along with their parent chains
    start_device, start_parents = find_device(network, start_mac)
    end_device, end_parents = find_device(network, end_mac)

    # If either device is not found, return an error
    if not start_device or not end_device:
        return None, "One or both devices not found."

    # If start or end device is root (no parents), treat it as its own parent
    if not start_parents:  # The start device is the root device
        start_parents = [start_device]  # Treat root as its own parent

    if not end_parents:  # The end device is the root device
        end_parents = [end_device]  # Treat root as its own parent

    # Find the common parent(s) of the start and end devices
    common_parents = []
    for parent in start_parents:
        if parent in end_parents:
            common_parents.append(parent["mac_address"])
    print("Last Common parent: ", common_parents[-1])

    start_parent_route = route_to_parent(network, start_mac, common_parents[-1])
    end_parent_route = route_to_parent(network, end_mac, common_parents[-1])
    raw_route = start_parent_route + end_parent_route[2::-1]
    seen = set()
    route = [mac for mac in raw_route if not (mac in seen or seen.add(mac))]

    return route, None
