# createCopyBuffer

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual OSPtr<IOBufferMemoryDescriptor> createCopyBuffer(IODirection direction, UInt64 length);
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547729-createcopybuffer)*