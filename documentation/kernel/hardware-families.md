# Hardware Families

**Framework**: Kernel

Add support for specific hardware protocols such as USB, and for standard network, serial, audio, and graphics interfaces. 

## Topics

### Hardware Interconnects
- [ATA](hardware_families/ata.md)
  Implement a driver that supports Advanced Technology Attachment (ATA) devices.
- [Bluetooth](hardware_families/bluetooth.md)
  Implement a driver that supports Bluetooth devices.
- [FireWire](hardware_families/firewire.md)
  Implement a driver that supports FireWire devices. 
- [PCI](hardware_families/pci.md)
  Implement a driver that supports Thunderbolt devices or PCI cards.
- [USB](hardware_families/usb.md)
  Implement a driver that supports Universal Serial Bus (USB) devices.
### Interfaces
- [Audio](hardware_families/audio.md)
  Implement a driver that interacts with audio hardware. 
- [Graphics and Displays](hardware_families/graphics_and_displays.md)
  Implement a driver that interacts with graphics and video hardware. 
- [HID](hardware_families/hid.md)
  Implement a driver that interacts with human interface devices, such as mice and keyboards.
- [Network](hardware_families/network.md)
  Implement a driver that interacts with network interfaces such as Ethernet adaptors. 
- [SCSI](hardware_families/scsi.md)
  Implement a driver that supports Small Computer System Interface (SCSI) protocols.
- [Mass Storage](hardware_families/mass_storage.md)
  Implement a driver that communicates with CD, DVD, or other mass storage devices.

## See Also

- [IOKit Fundamentals](iokit_fundamentals.md)
  Implement a driver for your custom hardware using a third-party kernel extension. 
- [Driver Support](driver_support.md)
  Explore the device registry and access power-management utilities and other shared driver features. 
- [libkern](libkern.md)
  Access the runtime support and base classes of the kernel library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families)*