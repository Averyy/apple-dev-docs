# ATA

**Framework**: Kernel

Implement a driver that supports Advanced Technology Attachment (ATA) devices.

## Topics

### Devices
- [ATADeviceNub](atadevicenub.md)
  ATADeviceNub is a concrete implementation of IOATADevice.
- [IOATADevice](ioatadevice.md)
  This object implements a relay to an ATA Bus where a drive is attached.
### Controller
- [IOATAController](ioatacontroller.md)
  The base class for ata controller family. Provides the interface common to all ata bus controllers.
### Registers
- [IOATAReg32](ioatareg32.md)
- [IOATAReg16](ioatareg16.md)
- [IOATAReg8](ioatareg8.md)
- [IOATAIOReg32](ioataioreg32.md)
- [IOATAIOReg16](ioataioreg16.md)
- [IOATAIOReg8](ioataioreg8.md)
- [IOATARegPtr32](ioataregptr32.md)
- [IOATARegPtr16](ioataregptr16.md)
- [IOATARegPtr8](ioataregptr8.md)
### Commands
- [IOATABusCommand64](ioatabuscommand64.md)
- [IOATABusCommand](ioatabuscommand.md)
- [IOATACommand](ioatacommand.md)
### Event Source
- [ATATimerEventSource](atatimereventsource.md)
  Extend the timer event source to allow checking for timer expiration from behind the workloop.
### ATAPI
- [IOATAPIProtocolTransport](ioatapiprotocoltransport.md)
  SCSI Protocol Driver Family for ATAPI Devices.
- [ATAPIClientData](atapiclientdata.md)
- [ATAPICmdPacket](atapicmdpacket.md)
### Base Types
- [ATAOperationType](ataoperationtype.md)
- [ATARequestIdentifier](atarequestidentifier.md)
- [IOExtendedLBA](ioextendedlba.md)
  If 48-bit LBAs are supported, IOExtendedLBA is used to represent a 48-bit LBA. The driver examines the ATA identify data to determine if 48-bit addressing is supported.
- [IOATABusInfo](ioatabusinfo.md)
  used to indicate the capabilities of the bus the device is connected to, PIO and DMA modes supported, etc.
- [IOATADevConfig](ioatadevconfig.md)
  used for configuring and communicating the desired transfer modes of a device. A disk driver would typically use this object in conjunction with the 512-bytes of identification data from the drive and the IOATABusInfo object for the bus it is connected to. This object will determine the best matching transfer speeds available. the device driver will then send a series of Set Features commands to configure the drive and this object to the bus through the IOATADevice nub in order to configure the optimum transfer mode. The driver for the disk drive may choose to populate this object with whatever transfer mode desired, in the event that a different mode is required.
- [IOATACompletionFunction](ioatacompletionfunction.md)
### Additional Types
- [ataDeviceType](atadevicetype.md)
- [ataEventCode](ataeventcode.md)
- [ataFlags](ataflags.md)
- [ataOpcode](ataopcode.md)
- [ataRegMask](ataregmask.md)
- [ataSocketType](atasockettype.md)
- [ataUnitID](ataunitid.md)
- [atapiConfig](atapiconfig.md)

## See Also

- [Bluetooth](hardware_families/bluetooth.md)
  Implement a driver that supports Bluetooth devices.
- [FireWire](hardware_families/firewire.md)
  Implement a driver that supports FireWire devices. 
- [PCI](hardware_families/pci.md)
  Implement a driver that supports Thunderbolt devices or PCI cards.
- [USB](hardware_families/usb.md)
  Implement a driver that supports Universal Serial Bus (USB) devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/ata)*