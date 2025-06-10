# setUltraModes

**Framework**: Kernel  
**Kind**: instm

Bit significant map of supported transfer modes. Set by ATAControllers.

## Declaration

```swift
void setUltraModes(
 UInt8 inModeBitMap );
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatabusinfo/1812012-setultramodes)*