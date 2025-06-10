# prepare

**Framework**: Kernel  
**Kind**: instm

Prepare the memory for an I/O transfer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn prepare(UInt64 offset, UInt64 length, bool flushCache, bool synchronize);
```

#### Return_value

An IOReturn code.

#### Discussion

Allocate the mapping resources neccessary for this transfer, specifying a sub range of the IOMemoryDescriptor that will be the target of the I/O. The complete() method frees these resources. Data may be copied to buffers for kIODirectionOut memory descriptors, depending on hardware mapping resource availabilty or alignment restrictions. It should be noted that the this function may block and should only be called on the clients context, i.e never call this routine while gated; also the call itself is not thread safe though this should be an issue as each IODMACommand is independant.

## Parameters

- `offset`: defines the starting offset in the memory descriptor the DMA command will operate on. genIOVMSegments will produce its results based on the offset and length passed to the prepare method.
- `length`: defines the ending position in the memory descriptor the DMA command will operate on. genIOVMSegments will produce its results based on the offset and length passed to the prepare method.
- `flushCache`: Flush the caches for the memory descriptor and make certain that the memory cycles are complete. Defaults to true for kNonCoherent and is ignored by the other types.
- `synchronize`: Copy any buffered data back from the target IOMemoryDescriptor. Defaults to true, if synchronize() is being used to explicitly copy data, passing false may avoid an unneeded copy.

## See Also

- [prepare](iodmacommand/1811284-prepare.md)
  Prepare the memory for an I/O transfer.
- [prepareWithSpecification](iodmacommand/1811291-preparewithspecification.md)
  Prepare the memory for an I/O transfer with a new specification.
- [- prepareWithSpecification](iodmacommand/1547733-preparewithspecification.md)
  Prepare the memory for an I/O transfer with a new specification.
- [- prepareWithSpecification](iodmacommand/3516451-preparewithspecification.md)
  Prepare the memory for an I/O transfer with a new specification.
- [complete](iodmacommand/1811081-complete.md)
  Complete processing of DMA mappings after an I/O transfer is finished.
- [- complete](iodmacommand/1547730-complete.md)
  Complete processing of DMA mappings after an I/O transfer is finished.
- [synchronize](iodmacommand/1811316-synchronize.md)
  Bring IOMemoryDescriptor and IODMACommand buffers into sync.
- [- synchronize](iodmacommand/1547719-synchronize.md)
  Bring IOMemoryDescriptor and IODMACommand buffers into sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547728-prepare)*