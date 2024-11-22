from pyroute import create_routing_list
import json

def main():
    try:
        with open("network.json", "r") as f:
            network = json.load(f)
    except FileNotFoundError:
        print("Network file not found.")
        exit()

    # Sample usage
    start_mac = "50:6B:AC:44:23:10"
    end_mac = "50:6B:AC:44:23:11"

    print("START: ", start_mac)
    print("END: ", end_mac)
    # Create and display the routing list

    route, error = create_routing_list(network, start_mac, end_mac)
    hops = len(route) - 1
    route.append(hops)

    if error:
        print(f"Error: {error}")
    else:
        print("Routing list:")
        for node in route[:-1]:
            print(f"  - {node}")

    print("Route:", route)

if __name__ == '__main__':
    main()
