# clearMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

Clears the DMACommand's current memory descriptor

## Declaration

```cpp
virtual IOReturn clearMemoryDescriptor(
 bool autoComplete = true);
```

## Overview

completes and invalidates the cache if the DMA command is currently active, copies all data from bounce buffers if necessary and releases all resources acquired during setMemoryDescriptor.

## Parameters

- `autoComplete`: An optional boolean variable that will call the complete() function automatically before the memory descriptor is processed. Defaults to true.

## See Also

### Configuring the Memory Descriptor
- [setMemoryDescriptor](./api-1811308-setmemorydescriptor.md)
  Sets and resets the DMACommand's current memory descriptor
- [- setMemoryDescriptor](./api-1547727-setmemorydescriptor.md)
  Sets and resets the DMACommand's current memory descriptor
- [- clearMemoryDescriptor](./api-1547715-clearmemorydescriptor.md)
  Clears the DMACommand's current memory descriptor
- [getMemoryDescriptor](./api-1811175-getmemorydescriptor.md)
  Get the current memory descriptor
- [- getMemoryDescriptor](./api-1547753-getmemorydescriptor.md)
  Get the current memory descriptor
- [- getIOMemoryDescriptor](./api-1547736-getiomemorydescriptor.md)
- [getPreparedOffsetAndLength](./api-1811194-getpreparedoffsetandlength.md)
  Returns the offset and length into the target IOMemoryDescriptor of a prepared IODDMACommand.
- [- getPreparedOffsetAndLength](./api-1547765-getpreparedoffsetandlength.md)
  Returns the offset and length into the target IOMemoryDescriptor of a prepared IODDMACommand.
- [genIOVMSegments](./api-1811150-geniovmsegments.md)
  Generates a physical scatter/gather for the current DMA command
- [- genIOVMSegments](./api-1547720-geniovmsegments.md)
  Generates a physical scatter/gather for the current DMA command
- [gen32IOVMSegments](./api-1811104-gen32iovmsegments.md)
  Helper function for a type checked call to genIOVMSegments(qv), for use with an IODMACommand set up with the output function kIODMACommandOutputHost32, kIODMACommandOutputBig32, or kIODMACommandOutputLittle32. If the output function of the IODMACommand is not a 32 bit function, results will be incorrect.
- [- gen32IOVMSegments](./api-1547749-gen32iovmsegments.md)
- [gen64IOVMSegments](./api-1811126-gen64iovmsegments.md)
  Helper function for a type checked call to genIOVMSegments(qv), for use with an IODMACommand set up with the output function kIODMACommandOutputHost64, kIODMACommandOutputBig64, or kIODMACommandOutputLittle64. If the output function of the IODMACommand is not a 64 bit function, results will be incorrect.
- [- gen64IOVMSegments](./api-1547722-gen64iovmsegments.md)
- [- createCopyBuffer](./api-1547729-createcopybuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1811032-clearmemorydescriptor)*