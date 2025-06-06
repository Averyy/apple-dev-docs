# PCI

**Framework**: Kernel

Implement a driver that supports Thunderbolt devices or PCI cards.

#### Overview

For many types of PCI drivers, the use of kernel extensions is deprecated. Instead, create a DriverKit extension using [`PCIDriverKit`](https://developer.apple.com/documentation/pcidriverkit).

## Topics

### Devices
- [Implementing a PCIe Kext for a Thunderbolt Device](hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device.md)
  Create an IOKit driver to support Thunderbolt devices that implement features not supported in PCIDriverKit, such as wireless networking or audio. 
- [IOPCIDevice](iopcidevice.md)
  An IOService class representing a PCI device.
- [IOAGPDevice](ioagpdevice.md)
  An IOService class representing an AGP primary device.
### Event Source
- [IOPCIEventSource](iopcieventsource.md)

## See Also

- [ATA](hardware_families/ata.md)
  Implement a driver that supports Advanced Technology Attachment (ATA) devices.
- [Bluetooth](hardware_families/bluetooth.md)
  Implement a driver that supports Bluetooth devices.
- [FireWire](hardware_families/firewire.md)
  Implement a driver that supports FireWire devices. 
- [USB](hardware_families/usb.md)
  Implement a driver that supports Universal Serial Bus (USB) devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/pci)*