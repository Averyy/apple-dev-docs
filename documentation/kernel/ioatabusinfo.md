# IOATABusInfo

**Framework**: Kernel  
**Kind**: cl

used to indicate the capabilities of the bus the device is connected to, PIO and DMA modes supported, etc.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class IOATABusInfo : OSObject
```

## Topics

### Miscellaneous
- [atabusinfo](ioatabusinfo/1811871-atabusinfo.md)
  factory method
- [getDMAModes](ioatabusinfo/1811885-getdmamodes.md)
  bit-significant map of DMA mode(s) supported on the bus. Used by clients of ATAControllers to find out about the bus.
- [getPIOModes](ioatabusinfo/1811901-getpiomodes.md)
  returns the bit-significant map of PIO mode(s) supported on the bus. Used by clients of ATAControllers to find out about the bus.
- [getSocketType](ioatabusinfo/1811918-getsockettype.md)
  returns the socket type, internal fixed, media-bay, PC-Card Used by clients of ATAControllers to find out about the bus
- [getUltraModes](ioatabusinfo/1811926-getultramodes.md)
  bit-significant map of Ultra mode(s) supported on the bus. Used by clients of ATAControllers to find out about the bus.
- [getUnits](ioatabusinfo/1811942-getunits.md)
  How many devices are present on bus. Used by clients of ATAControllers to find out about the bus.
- [maxBlocksExtended](ioatabusinfo/1811951-maxblocksextended.md)
  The maximum number of 512-byte blocks this controller supports in a single Extended LBA transfer. Some controllers may be limited to less than the maximum sector count allowed under extended LBA protocol.
- [setDMAModes](ioatabusinfo/1811960-setdmamodes.md)
  Bit significant map of supported transfer modes. Set by ATAControllers.
- [setDMAQueued](ioatabusinfo/1811970-setdmaqueued.md)
  Set true if supports DMA Queued Feature. Set by ATAControllers.
- [setExtendedLBA](ioatabusinfo/1811982-setextendedlba.md)
  Set true for supports 48-bit LBA. Set by ATAControllers.
- [setMaxBlocksExtended](ioatabusinfo/1811988-setmaxblocksextended.md)
  value set by controllers to indicate the maximum number of blocks allowed in a single transfer of data. Some dma engines may not be capable of supporting the full 16-bit worth of sector count allowed under 48 bit extended LBA. Default is 256 blocks, same as standard ATA.
- [setOverlapped](ioatabusinfo/1811995-setoverlapped.md)
  Set true for supports overlapped packet feature set. Set by ATAControllers.
- [setPIOModes](ioatabusinfo/1812001-setpiomodes.md)
  Bit significant map of supported transfer modes. Set by ATAControllers.
- [setSocketType](ioatabusinfo/1812008-setsockettype.md)
  internal fixed, media-bay, PC-Card. Set by ATAControllers.
- [setUltraModes](ioatabusinfo/1812012-setultramodes.md)
  Bit significant map of supported transfer modes. Set by ATAControllers.
- [setUnits](ioatabusinfo/1812016-setunits.md)
  set to indicate how many devices are on this bus. Set by ATAControllers.
- [supportsDMA](ioatabusinfo/1812021-supportsdma.md)
  True = DMA supported on bus - inferred by looking at the DMA mode bits. Used by clients of ATAControllers to find out about the bus.
- [supportsDMAQueued](ioatabusinfo/1812025-supportsdmaqueued.md)
  Supports DMA Queued Feature set if true. Used by clients of ATAControllers to find out about the bus.
- [supportsExtendedLBA](ioatabusinfo/1812028-supportsextendedlba.md)
  Supports 48-bit LBA if true. Used by clients of ATAControllers to find out about the bus.
- [supportsOverlapped](ioatabusinfo/1812032-supportsoverlapped.md)
  Supports overlapped packet feature set if true. Used by clients of ATAControllers to find out about the bus.
- [zeroData](ioatabusinfo/1812035-zerodata.md)
  set this object to a blank state.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](ioatabusinfo/reserved.md)
### Instance Methods
- [- getDMAModes](ioatabusinfo/1401320-getdmamodes.md)
- [- getMetaClass](ioatabusinfo/1401326-getmetaclass.md)
- [- getPIOModes](ioatabusinfo/1401337-getpiomodes.md)
- [- getSocketType](ioatabusinfo/1401308-getsockettype.md)
- [- getUltraModes](ioatabusinfo/1401314-getultramodes.md)
- [- getUnits](ioatabusinfo/1401299-getunits.md)
- [- init](ioatabusinfo/1401344-init.md)
- [- maxBlocksExtended](ioatabusinfo/1401348-maxblocksextended.md)
- [- setDMAModes](ioatabusinfo/1401335-setdmamodes.md)
- [- setDMAQueued](ioatabusinfo/1401304-setdmaqueued.md)
- [- setExtendedLBA](ioatabusinfo/1401328-setextendedlba.md)
- [- setMaxBlocksExtended](ioatabusinfo/1401310-setmaxblocksextended.md)
- [- setOverlapped](ioatabusinfo/1401306-setoverlapped.md)
- [- setPIOModes](ioatabusinfo/1401324-setpiomodes.md)
- [- setSocketType](ioatabusinfo/1401342-setsockettype.md)
- [- setUltraModes](ioatabusinfo/1401331-setultramodes.md)
- [- setUnits](ioatabusinfo/1401339-setunits.md)
- [- supportsDMA](ioatabusinfo/1401333-supportsdma.md)
- [- supportsDMAQueued](ioatabusinfo/1401346-supportsdmaqueued.md)
- [- supportsExtendedLBA](ioatabusinfo/1401302-supportsextendedlba.md)
- [- supportsOverlapped](ioatabusinfo/1401312-supportsoverlapped.md)
- [- zeroData](ioatabusinfo/1401322-zerodata.md)
### Type Methods
- [+ atabusinfo](ioatabusinfo/1401316-atabusinfo.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [ATAOperationType](ataoperationtype.md)
- [ATARequestIdentifier](atarequestidentifier.md)
- [IOExtendedLBA](ioextendedlba.md)
  If 48-bit LBAs are supported, IOExtendedLBA is used to represent a 48-bit LBA. The driver examines the ATA identify data to determine if 48-bit addressing is supported.
- [IOATADevConfig](ioatadevconfig.md)
  used for configuring and communicating the desired transfer modes of a device. A disk driver would typically use this object in conjunction with the 512-bytes of identification data from the drive and the IOATABusInfo object for the bus it is connected to. This object will determine the best matching transfer speeds available. the device driver will then send a series of Set Features commands to configure the drive and this object to the bus through the IOATADevice nub in order to configure the optimum transfer mode. The driver for the disk drive may choose to populate this object with whatever transfer mode desired, in the event that a different mode is required.
- [IOATACompletionFunction](ioatacompletionfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatabusinfo)*