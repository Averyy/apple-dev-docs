# cloneCommand

**Framework**: Kernel  
**Kind**: instm

Creates a new command based on the specification of the current one.

## Declaration

```swift
virtual IODMACommand *cloneCommand(
 void *refCon = 0);
```

#### Return_value

Returns a new memory cursor if successfully created and initialised, 0 otherwise.

#### Overview

Factory function to create and initialise an IODMACommand in one operation. The current command's specification will be duplicated in the new object, but however none of its state will be duplicated. This means that it is safe to clone a command even if it is currently active and running, however you must be certain that the command to be duplicated does have a valid reference for the duration.

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
- [- cloneCommand](iodmacommand/1547732-clonecommand.md)
  Creates a new command based on the specification of the current one.
- [- init](../driverkit/iodmacommand/3645796-init.md)
- [- free](iodmacommand/1547725-free.md)
- [MappingOptions](iodmacommand/mappingoptions.md)
  Mapping types to indicate the desired mapper type for translating memory descriptors into I/O DMA Bus addresses.
- [SynchronizeOptions](iodmacommand/synchronizeoptions.md)
  Options for the synchronize method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811059-clonecommand)*