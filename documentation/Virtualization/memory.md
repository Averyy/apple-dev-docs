# Memory

**Framework**: Virtualization

Configure a memory balloon device to change the allocated memory for the guest system.

## Topics

### Configuration
- [class VZVirtioTraditionalMemoryBalloonDeviceConfiguration](vzvirtiotraditionalmemoryballoondeviceconfiguration.md)
  A configuration object that provides a way to reclaim memory from the guest system.
- [class VZMemoryBalloonDeviceConfiguration](vzmemoryballoondeviceconfiguration.md)
  The common configuration traits for memory balloon devices.
### Memory balloon devices
- [class VZVirtioTraditionalMemoryBalloonDevice](vzvirtiotraditionalmemoryballoondevice.md)
  The object you use to change the amount of memory allocated to the guest system.
- [class VZMemoryBalloonDevice](vzmemoryballoondevice.md)
  The common behavior for memory devices.

## See Also

- [Audio](audio.md)
  Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.
- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
- [Keyboards and pointing devices](keyboards-and-pointing-devices.md)
  Configure devices that connect a mouse and keyboard to the guest system.
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
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/memory)*