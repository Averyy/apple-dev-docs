# setMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

Sets and resets the DMACommand's current memory descriptor

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn setMemoryDescriptor(const IOMemoryDescriptor *mem, bool autoPrepare);
```

#### Return_value

Returns kIOReturnSuccess, kIOReturnBusy if currently prepared, kIOReturnNoSpace if the length(mem) >= Maximum Transfer Size or the error codes returned by prepare() (qv).

#### Discussion

The DMA command will configure itself based on the information that it finds in the memory descriptor. It looks for things like the direction of the memory descriptor and whether the current memory descriptor is already mapped into some IOMMU. As a programmer convenience it can also prepare the DMA command immediately. See prepare(). Note the IODMACommand is designed to used multiple times with a succession of memory descriptors, making the pooling of commands possible. It is an error though to attempt to reset a currently prepared() DMA command. Warning: This routine may block so never try to autoprepare an IODMACommand while in a gated context, i.e. one of the WorkLoops action call outs.

## Parameters

- `mem`: A pointer to the current I/Os memory descriptor.
- `autoPrepare`: An optional boolean variable that will call the prepare() function automatically after the memory descriptor is processed. Defaults to true.

## See Also

- [setMemoryDescriptor](iodmacommand/1811308-setmemorydescriptor.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547727-setmemorydescriptor)*