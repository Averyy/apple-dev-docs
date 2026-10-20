# IOATABusInfo

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

used to indicate the capabilities of the bus the device is connected to, PIO and DMA modes supported, etc.

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class IOATABusInfo : OSObject
```

## Topics

### Miscellaneous
- [atabusinfo](./ioatabusinfo/api-1811871-atabusinfo.md)
  factory method
- [getDMAModes](./ioatabusinfo/api-1811885-getdmamodes.md)
  bit-significant map of DMA mode(s) supported on the bus. Used by clients of ATAControllers to find out about the bus.
- [getPIOModes](./ioatabusinfo/api-1811901-getpiomodes.md)
  returns the bit-significant map of PIO mode(s) supported on the bus. Used by clients of ATAControllers to find out about the bus.
- [getSocketType](./ioatabusinfo/api-1811918-getsockettype.md)
  returns the socket type, internal fixed, media-bay, PC-Card Used by clients of ATAControllers to find out about the bus
- [getUltraModes](./ioatabusinfo/api-1811926-getultramodes.md)
  bit-significant map of Ultra mode(s) supported on the bus. Used by clients of ATAControllers to find out about the bus.
- [getUnits](./ioatabusinfo/api-1811942-getunits.md)
  How many devices are present on bus. Used by clients of ATAControllers to find out about the bus.
- [maxBlocksExtended](./ioatabusinfo/api-1811951-maxblocksextended.md)
  The maximum number of 512-byte blocks this controller supports in a single Extended LBA transfer. Some controllers may be limited to less than the maximum sector count allowed under extended LBA protocol.
- [setDMAModes](./ioatabusinfo/api-1811960-setdmamodes.md)
  Bit significant map of supported transfer modes. Set by ATAControllers.
- [setDMAQueued](./ioatabusinfo/api-1811970-setdmaqueued.md)
  Set true if supports DMA Queued Feature. Set by ATAControllers.
- [setExtendedLBA](./ioatabusinfo/api-1811982-setextendedlba.md)
  Set true for supports 48-bit LBA. Set by ATAControllers.
- [setMaxBlocksExtended](./ioatabusinfo/api-1811988-setmaxblocksextended.md)
  value set by controllers to indicate the maximum number of blocks allowed in a single transfer of data. Some dma engines may not be capable of supporting the full 16-bit worth of sector count allowed under 48 bit extended LBA. Default is 256 blocks, same as standard ATA.
- [setOverlapped](./ioatabusinfo/api-1811995-setoverlapped.md)
  Set true for supports overlapped packet feature set. Set by ATAControllers.
- [setPIOModes](./ioatabusinfo/api-1812001-setpiomodes.md)
  Bit significant map of supported transfer modes. Set by ATAControllers.
- [setSocketType](./ioatabusinfo/api-1812008-setsockettype.md)
  internal fixed, media-bay, PC-Card. Set by ATAControllers.
- [setUltraModes](./ioatabusinfo/api-1812012-setultramodes.md)
  Bit significant map of supported transfer modes. Set by ATAControllers.
- [setUnits](./ioatabusinfo/api-1812016-setunits.md)
  set to indicate how many devices are on this bus. Set by ATAControllers.
- [supportsDMA](./ioatabusinfo/api-1812021-supportsdma.md)
  True = DMA supported on bus - inferred by looking at the DMA mode bits. Used by clients of ATAControllers to find out about the bus.
- [supportsDMAQueued](./ioatabusinfo/api-1812025-supportsdmaqueued.md)
  Supports DMA Queued Feature set if true. Used by clients of ATAControllers to find out about the bus.
- [supportsExtendedLBA](./ioatabusinfo/api-1812028-supportsextendedlba.md)
  Supports 48-bit LBA if true. Used by clients of ATAControllers to find out about the bus.
- [supportsOverlapped](./ioatabusinfo/api-1812032-supportsoverlapped.md)
  Supports overlapped packet feature set if true. Used by clients of ATAControllers to find out about the bus.
- [zeroData](./ioatabusinfo/api-1812035-zerodata.md)
  set this object to a blank state.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./ioatabusinfo/reserved.md)
### Instance Methods
- [- getDMAModes](./ioatabusinfo/api-1401320-getdmamodes.md)
- [- getMetaClass](./ioatabusinfo/api-1401326-getmetaclass.md)
- [- getPIOModes](./ioatabusinfo/api-1401337-getpiomodes.md)
- [- getSocketType](./ioatabusinfo/api-1401308-getsockettype.md)
- [- getUltraModes](./ioatabusinfo/api-1401314-getultramodes.md)
- [- getUnits](./ioatabusinfo/api-1401299-getunits.md)
- [- init](./ioatabusinfo/api-1401344-init.md)
- [- maxBlocksExtended](./ioatabusinfo/api-1401348-maxblocksextended.md)
- [- setDMAModes](./ioatabusinfo/api-1401335-setdmamodes.md)
- [- setDMAQueued](./ioatabusinfo/api-1401304-setdmaqueued.md)
- [- setExtendedLBA](./ioatabusinfo/api-1401328-setextendedlba.md)
- [- setMaxBlocksExtended](./ioatabusinfo/api-1401310-setmaxblocksextended.md)
- [- setOverlapped](./ioatabusinfo/api-1401306-setoverlapped.md)
- [- setPIOModes](./ioatabusinfo/api-1401324-setpiomodes.md)
- [- setSocketType](./ioatabusinfo/api-1401342-setsockettype.md)
- [- setUltraModes](./ioatabusinfo/api-1401331-setultramodes.md)
- [- setUnits](./ioatabusinfo/api-1401339-setunits.md)
- [- supportsDMA](./ioatabusinfo/api-1401333-supportsdma.md)
- [- supportsDMAQueued](./ioatabusinfo/api-1401346-supportsdmaqueued.md)
- [- supportsExtendedLBA](./ioatabusinfo/api-1401302-supportsextendedlba.md)
- [- supportsOverlapped](./ioatabusinfo/api-1401312-supportsoverlapped.md)
- [- zeroData](./ioatabusinfo/api-1401322-zerodata.md)
### Type Methods
- [+ atabusinfo](./ioatabusinfo/api-1401316-atabusinfo.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

## See Also

### Base Types
- [ATAOperationType](./ataoperationtype.md)
- [ATARequestIdentifier](./atarequestidentifier.md)
- [IOExtendedLBA](./ioextendedlba.md)
  If 48-bit LBAs are supported, IOExtendedLBA is used to represent a 48-bit LBA. The driver examines the ATA identify data to determine if 48-bit addressing is supported.
- [IOATADevConfig](./ioatadevconfig.md)
  used for configuring and communicating the desired transfer modes of a device. A disk driver would typically use this object in conjunction with the 512-bytes of identification data from the drive and the IOATABusInfo object for the bus it is connected to. This object will determine the best matching transfer speeds available. the device driver will then send a series of Set Features commands to configure the drive and this object to the bus through the IOATADevice nub in order to configure the optimum transfer mode. The driver for the disk drive may choose to populate this object with whatever transfer mode desired, in the event that a different mode is required.
- [IOATACompletionFunction](./ioatacompletionfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatabusinfo)*