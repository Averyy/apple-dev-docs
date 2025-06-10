# prepareWithSpecification

**Framework**: Kernel  
**Kind**: instm

Prepare the memory for an I/O transfer with a new specification.

## Declaration

```swift
virtual IOReturn prepareWithSpecification(
 SegmentFunction outSegFunc, 
 UInt8 numAddressBits, 
 UInt64 maxSegmentSize, 
 MappingOptions mappingOptions = kMapped, 
 UInt64 maxTransferSize = 0, 
 UInt32 alignment = 1, 
 IOMapper *mapper = 0, 
 UInt64 offset = 0, 
 UInt64 length = 0, 
 bool flushCache = true, 
 bool synchronize = true);
```

#### Return_value

An IOReturn code. Can fail if the mapping type is not recognised, if one of the 3 mandatory parameters are set to 0, if a 32 bit output function is selected when more than 32 bits of address is required or, if kBypassed is requested on a machine that doesn't support bypassing.

#### Overview

Allocate the mapping resources neccessary for this transfer, specifying a sub range of the IOMemoryDescriptor that will be the target of the I/O. The complete() method frees these resources. Data may be copied to buffers for kIODirectionOut memory descriptors, depending on hardware mapping resource availabilty or alignment restrictions. It should be noted that the this function may block and should only be called on the clients context, i.e never call this routine while gated; also the call itself is not thread safe though this should be an issue as each IODMACommand is independant.

## Parameters

- `outSegFunc`: SegmentFunction to call to output one physical segment. A set of nine commonly required segment functions are provided.
- `numAddressBits`: Number of bits that the hardware uses on its internal address bus. Typically 32 but may be more on modern hardware. A 0 implies no-restriction other than that implied by the output segment function.
- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0 which means any size.
- `mappingOptions`: is the type of mapping that is required to translate an IOMemoryDescriptor into the desired number of bits. For instance if your hardware only supports 32 bits but must run on machines with > 4G of RAM some mapping will be required. Number of bits will be specified in numAddressBits, see below.This parameter can take 3 values:- kNonCoherent - used for non-coherent hardware transfers, Mapped - Validate that all I/O bus generated addresses are within the number of addressing bits specified, Bypassed indicates that bypassed addressing is required, this is used when the hardware transferes are into coherent memory but no mapping is required. See also prepare() for failure cases.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restriction, in bytes, on I/O bus addresses. Defaults to single byte alignment.
- `mapper`: For mapping types kMapped & kBypassed mapper is used to define the hardware that will perform the mapping, defaults to the system mapper.
- `offset`: defines the starting offset in the memory descriptor the DMA command will operate on. genIOVMSegments will produce its results based on the offset and length passed to the prepare method.
- `length`: defines the ending position in the memory descriptor the DMA command will operate on. genIOVMSegments will produce its results based on the offset and length passed to the prepare method.
- `flushCache`: Flush the caches for the memory descriptor and make certain that the memory cycles are complete. Defaults to true for kNonCoherent and is ignored by the other types.
- `synchronize`: Copy any buffered data back from the target IOMemoryDescriptor. Defaults to true, if synchronize() is being used to explicitly copy data, passing false may avoid an unneeded copy.

## See Also

- [prepare](iodmacommand/1811284-prepare.md)
  Prepare the memory for an I/O transfer.
- [- prepare](iodmacommand/1547728-prepare.md)
  Prepare the memory for an I/O transfer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811291-preparewithspecification)*