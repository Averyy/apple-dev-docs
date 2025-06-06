# IOExtendedLBA

**Framework**: Kernel  
**Kind**: cl

If 48-bit LBAs are supported, IOExtendedLBA is used to represent a 48-bit LBA. The driver examines the ATA identify data to determine if 48-bit addressing is supported.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class IOExtendedLBA : OSObject
```

## Topics

### Miscellaneous
- [getCommand](ioextendedlba/1813831-getcommand.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getDevice](ioextendedlba/1813835-getdevice.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getExtendedLBA](ioextendedlba/1813840-getextendedlba.md)
  convenience method that gets a 48-bit LBA
- [getFeatures16](ioextendedlba/1813845-getfeatures16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getLBAHigh16](ioextendedlba/1813850-getlbahigh16.md)
  convenience method that gets the high 16 bits of a 48-bit LBA
- [getLBALow16](ioextendedlba/1813853-getlbalow16.md)
  convenience method that gets the lower 16 bits of a 48-bit LBA
- [getLBAMid16](ioextendedlba/1813856-getlbamid16.md)
  convenience method that gets the middle 16 bits of a 48-bit LBA
- [getSectorCount16](ioextendedlba/1813860-getsectorcount16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setCommand](ioextendedlba/1813863-setcommand.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setDevice](ioextendedlba/1813867-setdevice.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setExtendedLBA](ioextendedlba/1813870-setextendedlba.md)
  convenience method that sets the taskfile registers into a 48-bit LBA address, along with sector count, and unit selected and LBA bit set
- [setFeatures16](ioextendedlba/1813873-setfeatures16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setLBAHigh16](ioextendedlba/1813876-setlbahigh16.md)
  convenience method that sets the high 16 bits of a 48-bit LBA
- [setLBALow16](ioextendedlba/1813879-setlbalow16.md)
  convenience method that sets the lower 16 bits of a 48-bit LBA
- [setLBAMid16](ioextendedlba/1813881-setlbamid16.md)
  convenience method that sets the middle 16 bits of a 48-bit LBA
- [setSectorCount16](ioextendedlba/1813884-setsectorcount16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [zeroData](ioextendedlba/1813886-zerodata.md)
  convenience method that zeros out the lba, sector count, features, device, and command member variables
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](ioextendedlba/reserved.md)
### Instance Methods
- [- getCommand](ioextendedlba/1392162-getcommand.md)
- [- getDevice](ioextendedlba/1392071-getdevice.md)
- [- getExtendedLBA](ioextendedlba/1392177-getextendedlba.md)
- [- getFeatures16](ioextendedlba/1392160-getfeatures16.md)
- [- getLBAHigh16](ioextendedlba/1392136-getlbahigh16.md)
- [- getLBALow16](ioextendedlba/1392085-getlbalow16.md)
- [- getLBAMid16](ioextendedlba/1392164-getlbamid16.md)
- [- getMetaClass](ioextendedlba/1392121-getmetaclass.md)
- [- getSectorCount16](ioextendedlba/1392095-getsectorcount16.md)
- [- setCommand](ioextendedlba/1392081-setcommand.md)
- [- setDevice](ioextendedlba/1392149-setdevice.md)
- [- setExtendedLBA](ioextendedlba/1392107-setextendedlba.md)
- [- setFeatures16](ioextendedlba/1392128-setfeatures16.md)
- [- setLBAHigh16](ioextendedlba/1392156-setlbahigh16.md)
- [- setLBALow16](ioextendedlba/1392052-setlbalow16.md)
- [- setLBAMid16](ioextendedlba/1392175-setlbamid16.md)
- [- setSectorCount16](ioextendedlba/1392102-setsectorcount16.md)
- [- zeroData](ioextendedlba/1392147-zerodata.md)
### Type Methods
- [+ createIOExtendedLBA](ioextendedlba/1392089-createioextendedlba.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [ATAOperationType](ataoperationtype.md)
- [ATARequestIdentifier](atarequestidentifier.md)
- [IOATABusInfo](ioatabusinfo.md)
  used to indicate the capabilities of the bus the device is connected to, PIO and DMA modes supported, etc.
- [IOATADevConfig](ioatadevconfig.md)
  used for configuring and communicating the desired transfer modes of a device. A disk driver would typically use this object in conjunction with the 512-bytes of identification data from the drive and the IOATABusInfo object for the bus it is connected to. This object will determine the best matching transfer speeds available. the device driver will then send a series of Set Features commands to configure the drive and this object to the bus through the IOATADevice nub in order to configure the optimum transfer mode. The driver for the disk drive may choose to populate this object with whatever transfer mode desired, in the event that a different mode is required.
- [IOATACompletionFunction](ioatacompletionfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioextendedlba)*