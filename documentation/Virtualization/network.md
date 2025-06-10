# Network

**Framework**: Virtualization

Configure the devices that connect the guest system to the network.

## Topics

### Configurations
- [class VZVirtioNetworkDeviceConfiguration](vzvirtionetworkdeviceconfiguration.md)
  A configuration object that requests the creation of a network device for the guest system.
- [class VZNetworkDeviceConfiguration](vznetworkdeviceconfiguration.md)
  The common configuration traits for network devices.
- [class VZMACAddress](vzmacaddress.md)
  The media access control (MAC) address for a network interface in your virtual machine.
### Attachment points
- [class VZBridgedNetworkDeviceAttachment](vzbridgednetworkdeviceattachment.md)
  A network device that interacts directly with a physical network interface on the host computer.
- [class VZFileHandleNetworkDeviceAttachment](vzfilehandlenetworkdeviceattachment.md)
  A network device that transmits raw network packets and frames using a datagram socket.
- [class VZNATNetworkDeviceAttachment](vznatnetworkdeviceattachment.md)
  A device that routes network requests through the host computer and performs network address translation on the resulting packets.
- [class VZVmnetNetworkDeviceAttachment](vzvmnetnetworkdeviceattachment.md)
  A network device attachment that allows a custom network topology.
- [class VZNetworkDeviceAttachment](vznetworkdeviceattachment.md)
  The common behaviors for the network attachment points of your virtual machine.
### Hardware interfaces
- [class VZBridgedNetworkInterface](vzbridgednetworkinterface.md)
  An object that identifies the supported network interfaces of the host computer.
### Devices
- [class VZNetworkDevice](vznetworkdevice.md)
  A base class that represents a network device in a virtual machine.

## See Also

- [Audio](audio.md)
  Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.
- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
- [Keyboards and pointing devices](keyboards-and-pointing-devices.md)
  Configure devices that connect a mouse and keyboard to the guest system.
- [Memory](memory.md)
  Configure a memory balloon device to change the allocated memory for the guest system.
- [Randomization](randomization.md)
  Configure a device for the guest system to use to generate random numbers.
- [Serial ports](serial-ports.md)
  Configure the serial devices that you use to communicate with the guest system.
- [Shared directories](shared-directories.md)
  Configure devices that share directories from the host into the guest system.
- [Sockets](sockets.md)
  Configure a device that manages port-based communication with the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/network)*