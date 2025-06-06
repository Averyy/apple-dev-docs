# Consoles

**Framework**: Virtualization

Configure a device that manages multiport console communication with the guest system.

## Topics

### Configurations
- [class VZConsoleDeviceConfiguration](vzconsoledeviceconfiguration.md)
  The base class for a console device configuration.
- [class VZConsolePortConfiguration](vzconsoleportconfiguration.md)
  The base class for a console port configuration.
- [class VZVirtioConsoleDeviceConfiguration](vzvirtioconsoledeviceconfiguration.md)
  A console device that enables communication between the host and the guest using console ports through a Virtio interface.
- [class VZVirtioConsolePortConfiguration](vzvirtioconsoleportconfiguration.md)
  A class that represents the configuration options you can set on a Virtio console port.
- [class VZVirtioConsolePortConfigurationArray](vzvirtioconsoleportconfigurationarray.md)
  A class that represents a collection of Virtio console port configurations.
### Console ports
- [class VZVirtioConsolePort](vzvirtioconsoleport.md)
  A class that represents a Virtio console port in a VM.
- [class VZVirtioConsolePortArray](vzvirtioconsoleportarray.md)
  A class that represents a collection of Virtio console ports.
### Devices
- [class VZConsoleDevice](vzconsoledevice.md)
  A class that represents a console device in a VM.
- [class VZVirtioConsoleDevice](vzvirtioconsoledevice.md)
  A class that represents a Virtio console device in a virtual machine.

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
- [Sockets](sockets.md)
  Configure a device that manages port-based communication with the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/consoles)*