# complete

**Framework**: Kernel  
**Kind**: instm

Complete processing of DMA mappings after an I/O transfer is finished.

## Declaration

```swift
virtual IOReturn complete(
 bool invalidateCache = true,
 bool synchronize = true);
```

#### Return_value

kIOReturnNotReady if not prepared, kIOReturnSuccess otherwise.

#### Overview

This method should not be called unless a prepare was previously issued; the prepare() and complete() must occur in pairs, before and after an I/O transfer

## Parameters

- `invalidCache`: Invalidate the caches for the memory descriptor. Defaults to true for kNonCoherent and is ignored by the other types.
- `synchronize`: Copy any buffered data back to the target IOMemoryDescriptor. Defaults to true, if synchronize() is being used to explicitly copy data, passing false may avoid an unneeded copy.

## See Also

- [prepare](iodmacommand/1811284-prepare.md)
  Prepare the memory for an I/O transfer.
- [- prepare](iodmacommand/1547728-prepare.md)
  Prepare the memory for an I/O transfer.
- [prepareWithSpecification](iodmacommand/1811291-preparewithspecification.md)
  Prepare the memory for an I/O transfer with a new specification.
- [- prepareWithSpecification](iodmacommand/1547733-preparewithspecification.md)
  Prepare the memory for an I/O transfer with a new specification.
- [- prepareWithSpecification](iodmacommand/3516451-preparewithspecification.md)
  Prepare the memory for an I/O transfer with a new specification.
- [- complete](iodmacommand/1547730-complete.md)
  Complete processing of DMA mappings after an I/O transfer is finished.
- [synchronize](iodmacommand/1811316-synchronize.md)
  Bring IOMemoryDescriptor and IODMACommand buffers into sync.
- [- synchronize](iodmacommand/1547719-synchronize.md)
  Bring IOMemoryDescriptor and IODMACommand buffers into sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811081-complete)*