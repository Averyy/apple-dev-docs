# Keyboards and pointing devices

**Framework**: Virtualization

Configure devices that connect a mouse and keyboard to the guest system.

#### Overview

Configure a keyboard and a pointing device to allow people to interact with macOS or Linux VMs.

## Topics

### Keyboards
- [class VZKeyboardConfiguration](vzkeyboardconfiguration.md)
  The base class for a configuring a keyboard.
- [class VZMacKeyboardConfiguration](vzmackeyboardconfiguration.md)
  A device that defines the configuration for a Mac keyboard.
- [class VZUSBKeyboardConfiguration](vzusbkeyboardconfiguration.md)
  A device that defines the configuration for a USB keyboard.
### Pointing devices
- [class VZMacTrackpadConfiguration](vzmactrackpadconfiguration.md)
  The class that represents the configuration for a Mac trackpad.
- [class VZUSBScreenCoordinatePointingDeviceConfiguration](vzusbscreencoordinatepointingdeviceconfiguration.md)
  An object that defines the configuration for a USB pointing device that reports absolute coordinates.
- [class VZPointingDeviceConfiguration](vzpointingdeviceconfiguration.md)
  The base class for a pointing device configuration.

## See Also

- [Audio](audio.md)
  Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.
- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
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
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/keyboards-and-pointing-devices)*