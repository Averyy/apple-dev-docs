# Serial ports

**Framework**: Virtualization

Configure the serial devices that you use to communicate with the guest system.

## Topics

### Configurations
- [class VZVirtioConsoleDeviceSerialPortConfiguration](vzvirtioconsoledeviceserialportconfiguration.md)
  A configuration object that requests the creation of a console device to communicate with the guest system.
- [class VZSerialPortConfiguration](vzserialportconfiguration.md)
  The common configuration traits for serial port requests.
### Attachment points
- [class VZFileHandleSerialPortAttachment](vzfilehandleserialportattachment.md)
  An attachment point that allows bidirectional communication using file handles.
- [class VZFileSerialPortAttachment](vzfileserialportattachment.md)
  An attachment point that writes data from the guest system to a file.
- [class VZSerialPortAttachment](vzserialportattachment.md)
  The common behaviors for the serial attachment points of your virtual machine.

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

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/serial-ports)*