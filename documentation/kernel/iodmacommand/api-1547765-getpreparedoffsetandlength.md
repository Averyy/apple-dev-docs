# getPreparedOffsetAndLength

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the offset and length into the target IOMemoryDescriptor of a prepared IODDMACommand.

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn getPreparedOffsetAndLength(UInt64 *offset, UInt64 *length);
```

## Return Value

An IOReturn code. kIOReturnNotReady if the IODMACommand is not prepared.

## Discussion

If successfully prepared, returns the offset and length into the IOMemoryDescriptor. Will fail for an unprepared IODMACommand.

## Parameters

- `offset`: returns the starting offset in the memory descriptor the DMA command was prepared with. Pass NULL for don't care.
- `length`: returns the length in the memory descriptor the DMA command was prepared with. Pass NULL for don't care.

## See Also

### Configuring the Memory Descriptor
- [setMemoryDescriptor](./api-1811308-setmemorydescriptor.md)
  Sets and resets the DMACommand's current memory descriptor
- [- setMemoryDescriptor](./api-1547727-setmemorydescriptor.md)
  Sets and resets the DMACommand's current memory descriptor
- [clearMemoryDescriptor](./api-1811032-clearmemorydescriptor.md)
  Clears the DMACommand's current memory descriptor
- [- clearMemoryDescriptor](./api-1547715-clearmemorydescriptor.md)
  Clears the DMACommand's current memory descriptor
- [getMemoryDescriptor](./api-1811175-getmemorydescriptor.md)
  Get the current memory descriptor
- [- getMemoryDescriptor](./api-1547753-getmemorydescriptor.md)
  Get the current memory descriptor
- [- getIOMemoryDescriptor](./api-1547736-getiomemorydescriptor.md)
- [getPreparedOffsetAndLength](./api-1811194-getpreparedoffsetandlength.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547765-getpreparedoffsetandlength)*