# initWithSpecification

**Framework**: Kernel  
**Kind**: instm

Primary initializer for the DMA command object.

## Declaration

```swift
virtual bool initWithSpecification(
 SegmentFunction outSegFunc, 
 UInt8 numAddressBits, 
 UInt64 maxSegmentSize, 
 MappingOptions mappingOptions = kMapped, 
 UInt64 maxTransferSize = 0, 
 UInt32 alignment = 1, 
 IOMapper *mapper = 0, 
 void *refCon = 0);
```

#### Return_value

Can fail if the mapping type is not recognised, if one of the 3 mandatory parameters are set to 0, if a 32 bit output function is selected when more than 32 bits of address is required or, if kBypassed is requested on a machine that doesn't support bypassing. Returns true otherwise.

## Parameters

- `outSegFunc`: SegmentFunction to call to output one physical segment. A set of nine commonly required segment functions are provided.
- `numAddressBits`: Number of bits that the hardware uses on its internal address bus. Typically 32 but may be more on modern hardware. A 0 implies no-restriction other than that implied by the output segment function.
- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0 which means any size.
- `mappingOptions`: The type of mapping that is required to translate an IOMemoryDescriptor into the desired number of bits. For instance if your hardware only supports 32 bits but must run on machines with > 4G of RAM some mapping will be required. Number of bits will be specified in numAddressBits, see below.This parameter can take 3 values:- kNonCoherent - used for non-coherent hardware transfers, Mapped - Validate that all I/O bus generated addresses are within the number of addressing bits specified, Bypassed indicates that bypassed addressing is required, this is used when the hardware transferes are into coherent memory but no mapping is required. See also prepare() for failure cases.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restriction, in bytes, on I/O bus addresses. Defaults to single byte alignment.
- `mapper`: For mapping types kMapped & kBypassed mapper is used to define the hardware that will perform the mapping, defaults to the system mapper.

## See Also

- [withSpecification](iodmacommand/1811330-withspecification.md)
  Creates and initializes a DMA command in one operation.
- [+ withSpecification](iodmacommand/1547758-withspecification.md)
  Creates and initializes an DMA command in one operation.
- [+ withSpecification](iodmacommand/3516452-withspecification.md)
  Creates and initializes an DMA command in one operation.
- [- initWithSpecification](iodmacommand/1547748-initwithspecification.md)
  Primary initializer for the DMA command object.
- [- initWithSpecification](iodmacommand/3516450-initwithspecification.md)
  Primary initializer for the DMA command object.
- [weakWithSpecification](iodmacommand/1811323-weakwithspecification.md)
  Creates and initializes an DMA command object in one operation if this version of the operating system supports it.
- [+ withRefCon](iodmacommand/1547747-withrefcon.md)
- [- initWithRefCon](iodmacommand/1547754-initwithrefcon.md)
- [cloneCommand](iodmacommand/1811059-clonecommand.md)
  Creates a new command based on the specification of the current one.
- [- cloneCommand](iodmacommand/1547732-clonecommand.md)
  Creates a new command based on the specification of the current one.
- [- init](../driverkit/iodmacommand/3645796-init.md)
- [- free](iodmacommand/1547725-free.md)
- [MappingOptions](iodmacommand/mappingoptions.md)
  Mapping types to indicate the desired mapper type for translating memory descriptors into I/O DMA Bus addresses.
- [SynchronizeOptions](iodmacommand/synchronizeoptions.md)
  Options for the synchronize method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811207-initwithspecification)*