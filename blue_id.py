import bluetooth


def discover_connected_device():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        if bluetooth.lookup_name(addr) is not None:
            print("Bluetooth ID of the connected device:", addr)
            return addr
    print("No connected Bluetooth devices found.")
    return None


if __name__ == "__main__":
    discover_connected_device()
