# IODMACommand

**Framework**: Kernel  
**Kind**: cl

An object that converts memory references to I/O bus addresses.

**Availability**:
- DriverKit 20.0+
- macOS 10.4+

## Declaration

```swift
class IODMACommand : IOCommand
```

#### Overview

The [`IODMACommand`](iodmacommand.md) class supersedes [`IOMemoryCursor`](iomemorycursor.md) and greatly enhances the functionality and power of it. The command can be specified to output 64 bit physical addresses and also allows driver writers to bypass mapping hardware or get addresses suitable for non-snooped DMA.

The command is designed to be very easily subclassable. Most driver writers need to associate some DMA operations with their memory descriptor, and usually use a C structure for that purpose. This structure is often kept in a linked list. This [`IODMACommand`](iodmacommand.md) has built-in `<kern/queue.h>` linkage and can be derived and 'public:' variables added, giving the developer a structure that can associate a memory descriptor with a particular DMA command but will also allow the developer to generate that command and keep the state necessary for tracking it.

Create a pool of [`IODMACommand`](iodmacommand.md) objects at driver initialization, and keep each command in an [`IOCommandPool`](iocommandpool.md) when not in use. You may also maintain your own free list of objects if preferred. See the `<kern/queue.h>` and `<xnu/iokit/Kernel/IOCommandPool>` for sample code on manipulating the command's doubly linked list entries.

You can use an [`IODMACommand`](iodmacommand.md) object in a 'weak-linked' manner. To do this you must avoid using any static member functions. Use the much slower, but safe, [`weakWithSpecification`](1547721-weakwithspecification.md) function. On success, the function returns a DMA command object, which you can use to clone as many commands as needed.

## Topics

### Creating a DMA Command
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
- [MappingOptions](iodmacommand/mappingoptions.md)
  Mapping types to indicate the desired mapper type for translating memory descriptors into I/O DMA Bus addresses.
- [SynchronizeOptions](iodmacommand/synchronizeoptions.md)
  Options for the synchronize method.
### Configuring the Memory Descriptor
- [setMemoryDescriptor](iodmacommand/1811308-setmemorydescriptor.md)
  Sets and resets the DMACommand's current memory descriptor
- [- setMemoryDescriptor](iodmacommand/1547727-setmemorydescriptor.md)
  Sets and resets the DMACommand's current memory descriptor
- [clearMemoryDescriptor](iodmacommand/1811032-clearmemorydescriptor.md)
  Clears the DMACommand's current memory descriptor
- [- clearMemoryDescriptor](iodmacommand/1547715-clearmemorydescriptor.md)
  Clears the DMACommand's current memory descriptor
- [getMemoryDescriptor](iodmacommand/1811175-getmemorydescriptor.md)
  Get the current memory descriptor
- [- getMemoryDescriptor](iodmacommand/1547753-getmemorydescriptor.md)
  Get the current memory descriptor
- [- getIOMemoryDescriptor](iodmacommand/1547736-getiomemorydescriptor.md)
- [getPreparedOffsetAndLength](iodmacommand/1811194-getpreparedoffsetandlength.md)
  Returns the offset and length into the target IOMemoryDescriptor of a prepared IODDMACommand.
- [- getPreparedOffsetAndLength](iodmacommand/1547765-getpreparedoffsetandlength.md)
  Returns the offset and length into the target IOMemoryDescriptor of a prepared IODDMACommand.
- [genIOVMSegments](iodmacommand/1811150-geniovmsegments.md)
  Generates a physical scatter/gather for the current DMA command
- [- genIOVMSegments](iodmacommand/1547720-geniovmsegments.md)
  Generates a physical scatter/gather for the current DMA command
- [gen32IOVMSegments](iodmacommand/1811104-gen32iovmsegments.md)
  Helper function for a type checked call to genIOVMSegments(qv), for use with an IODMACommand set up with the output function kIODMACommandOutputHost32, kIODMACommandOutputBig32, or kIODMACommandOutputLittle32. If the output function of the IODMACommand is not a 32 bit function, results will be incorrect.
- [- gen32IOVMSegments](iodmacommand/1547749-gen32iovmsegments.md)
- [gen64IOVMSegments](iodmacommand/1811126-gen64iovmsegments.md)
  Helper function for a type checked call to genIOVMSegments(qv), for use with an IODMACommand set up with the output function kIODMACommandOutputHost64, kIODMACommandOutputBig64, or kIODMACommandOutputLittle64. If the output function of the IODMACommand is not a 64 bit function, results will be incorrect.
- [- gen64IOVMSegments](iodmacommand/1547722-gen64iovmsegments.md)
- [- createCopyBuffer](iodmacommand/1547729-createcopybuffer.md)
### Preparing the Transfer Operation
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
- [complete](iodmacommand/1811081-complete.md)
  Complete processing of DMA mappings after an I/O transfer is finished.
- [- complete](iodmacommand/1547730-complete.md)
  Complete processing of DMA mappings after an I/O transfer is finished.
- [synchronize](iodmacommand/1811316-synchronize.md)
  Bring IOMemoryDescriptor and IODMACommand buffers into sync.
- [- synchronize](iodmacommand/1547719-synchronize.md)
  Bring IOMemoryDescriptor and IODMACommand buffers into sync.
### Transferring Data
- [readBytes](iodmacommand/1811301-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [- readBytes](iodmacommand/1547724-readbytes.md)
  Copy data from the IODMACommand's buffer to the specified buffer.
- [writeBytes](iodmacommand/1811341-writebytes.md)
  Copy data to the IODMACommand's buffer from the specified buffer.
- [- writeBytes](iodmacommand/1547742-writebytes.md)
  Copy data to the IODMACommand's buffer from the specified buffer.
### Managing Memory Segments
- [Segment32](iodmacommand/segment32.md)
  A 32 bit I/O bus address/length pair.
- [Segment64](iodmacommand/segment64.md)
  A 64 bit I/O bus address/length pair.
- [SegmentFunction](iodmacommand/segmentfunction.md)
  A C function that translates a 64-bit segment and outputs a single desired segment to the specified array. 
- [kIODMACommandOutputBig32](kiodmacommandoutputbig32.md)
  Output big-endian Segment32 output segment function.
- [OutputBig32](iodmacommand/1811221-outputbig32.md)
  Output big-endian Segment32 output segment function.
- [+ OutputBig32](iodmacommand/1547743-outputbig32.md)
  Output big-endian Segment32 output segment function.
- [kIODMACommandOutputBig64](kiodmacommandoutputbig64.md)
  Output big-endian Segment64 output segment function.
- [OutputBig64](iodmacommand/1811234-outputbig64.md)
  Output big-endian Segment64 output segment function.
- [+ OutputBig64](iodmacommand/1547757-outputbig64.md)
  Output big-endian Segment64 output segment function.
- [kIODMACommandOutputHost32](kiodmacommandoutputhost32.md)
  Output host natural Segment32 output segment function.
- [OutputHost32](iodmacommand/1811245-outputhost32.md)
  Output host natural Segment32 output segment function.
- [+ OutputHost32](iodmacommand/1547726-outputhost32.md)
  Output host natural Segment32 output segment function.
- [kIODMACommandOutputHost64](kiodmacommandoutputhost64.md)
  Output host natural Segment64 output segment function.
- [OutputHost64](iodmacommand/1811257-outputhost64.md)
  Output host natural Segment64 output segment function.
- [+ OutputHost64](iodmacommand/1547750-outputhost64.md)
  Output host natural Segment64 output segment function.
- [kIODMACommandOutputLittle32](kiodmacommandoutputlittle32.md)
  Output little-endian Segment32 output segment function.
- [OutputLittle32](iodmacommand/1811267-outputlittle32.md)
  Output little-endian Segment32 output segment function.
- [+ OutputLittle32](iodmacommand/1547744-outputlittle32.md)
  Output little-endian Segment32 output segment function.
- [kIODMACommandOutputLittle64](kiodmacommandoutputlittle64.md)
  Output little-endian Segment64 output segment function.
- [OutputLittle64](iodmacommand/1811275-outputlittle64.md)
  Output little-endian Segment64 output segment function.
- [+ OutputLittle64](iodmacommand/1547764-outputlittle64.md)
  Output little-endian Segment64 output segment function.
### Getting Configuration Details
- [- getAlignment](iodmacommand/1547755-getalignment.md)
- [- getAlignmentInternalSegments](iodmacommand/1547737-getalignmentinternalsegments.md)
- [- getAlignmentLength](iodmacommand/1547731-getalignmentlength.md)
- [- getMetaClass](iodmacommand/1547717-getmetaclass.md)
- [- getNumAddressBits](iodmacommand/1547735-getnumaddressbits.md)
- [- setSpecification](iodmacommand/1547759-setspecification.md)
### Performing Internal Operations
- [Private Accessors](iodmacommand/private_accessors.md)
### Type Methods
- [+ weakWithSpecification](1547721-weakwithspecification.md)

## Relationships

### Inherits From
- [IOCommand](iocommand.md)
- [OSObject](../driverkit/osobject.md)

## See Also

- [IODMAController](iodmacontroller.md)
- [IODMAEventSource](iodmaeventsource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand)*