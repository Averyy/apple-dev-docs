# MappingOptions

**Framework**: Kernel  
**Kind**: tdef

Mapping types to indicate the desired mapper type for translating memory descriptors into I/O DMA Bus addresses.

## Declaration

```swift
enum MappingOptions {
   kMapped = 0x00000000,
   kBypassed = 0x00000001,
   kNonCoherent = 0x00000002,
   kTypeMask = 0x0000000f,
   kNoCacheStore = 0x00000010, // Memory in descriptor
   kOnChip = 0x00000020, // Indicates DMA is on South Bridge
   kIterateOnly = 0x00000040 // DMACommand will be used as a cursor only
};
```

## Topics

### Constants
- [kNonCoherent](iodmacommand/mappingoptions/knoncoherent.md)
- [kMapped](iodmacommand/mappingoptions/kmapped.md)
- [kBypassed](iodmacommand/mappingoptions/kbypassed.md)
- [kMaxMappingOptions](iodmacommand/mappingoptions/kmaxmappingoptions.md)

## See Also

- [withSpecification](iodmacommand/1811330-withspecification.md)
  Creates and initializes a DMA command in one operation.
- [+ withSpecification](iodmacommand/1547758-withspecification.md)
  Creates and initializes an DMA command in one operation.
- [+ withSpecification](iodmacommand/3516452-withspecification.md)
  Creates and initializes an DMA command in one operation.
- [initWithSpecification](iodmacommand/1811207-initwithspecification.md)
  Primary initializer for the DMA command object.
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
- [SynchronizeOptions](iodmacommand/synchronizeoptions.md)
  Options for the synchronize method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/mappingoptions)*