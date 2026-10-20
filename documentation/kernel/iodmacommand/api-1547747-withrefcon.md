# withRefCon

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 10.11.4+

## Declaration

```c
static OSPtr<IODMACommand> withRefCon(void *refCon);
```

## See Also

### Creating a DMA Command
- [withSpecification](./api-1811330-withspecification.md)
  Creates and initializes a DMA command in one operation.
- [+ withSpecification](./api-1547758-withspecification.md)
  Creates and initializes an DMA command in one operation.
- [+ withSpecification](./api-3516452-withspecification.md)
  Creates and initializes an DMA command in one operation.
- [initWithSpecification](./api-1811207-initwithspecification.md)
  Primary initializer for the DMA command object.
- [- initWithSpecification](./api-1547748-initwithspecification.md)
  Primary initializer for the DMA command object.
- [- initWithSpecification](./api-3516450-initwithspecification.md)
  Primary initializer for the DMA command object.
- [weakWithSpecification](./api-1811323-weakwithspecification.md)
  Creates and initializes an DMA command object in one operation if this version of the operating system supports it.
- [- initWithRefCon](./api-1547754-initwithrefcon.md)
- [cloneCommand](./api-1811059-clonecommand.md)
  Creates a new command based on the specification of the current one.
- [- cloneCommand](./api-1547732-clonecommand.md)
  Creates a new command based on the specification of the current one.
- [- init](../../DriverKit/iodmacommand/init.md)
- [- free](./api-1547725-free.md)
- [MappingOptions](./mappingoptions.md)
  Mapping types to indicate the desired mapper type for translating memory descriptors into I/O DMA Bus addresses.
- [SynchronizeOptions](./synchronizeoptions.md)
  Options for the synchronize method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547747-withrefcon)*