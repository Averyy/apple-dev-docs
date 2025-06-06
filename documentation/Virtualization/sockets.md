# Sockets

**Framework**: Virtualization

Configure a device that manages port-based communication with the guest system.

## Topics

### Configurations
- [class VZVirtioSocketDeviceConfiguration](vzvirtiosocketdeviceconfiguration.md)
  A configuration object that requests the creation of a socket device to communicate with the guest system.
- [class VZSocketDeviceConfiguration](vzsocketdeviceconfiguration.md)
  The common configuration traits for socket device requests.
### Devices
- [class VZVirtioSocketDevice](vzvirtiosocketdevice.md)
  A device that manages port-based connections between the guest system and the host computer.
- [class VZSocketDevice](vzsocketdevice.md)
  The common behavior of socket devices.
### Connection management
- [class VZVirtioSocketListener](vzvirtiosocketlistener.md)
  An object that listens for port-based connection requests from the guest operating system.
- [class VZVirtioSocketConnection](vzvirtiosocketconnection.md)
  A port-based connection between the guest operating system and the host computer.

## See Also

- [Audio](audio.md)
  Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.
- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
- [Keyboards and pointing devices](keyboards-and-pointing-devices.md)
  Configure devices that connect a mouse and keyboard to the guest system.
- [Memory](memory.md)
  Configure a memory balloon device to change the allocated memory for the guest system.
- [Network](network.md)
  Configure the devices that connect the guest system to the network.
- [Randomization](randomization.md)
  Configure a device for the guest system to use to generate random numbers.
- [Serial ports](serial-ports.md)
  Configure the serial devices that you use to communicate with the guest system.
- [Shared directories](shared-directories.md)
  Configure devices that share directories from the host into the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/sockets)*