# synchronize

**Framework**: Kernel  
**Kind**: instm

Bring IOMemoryDescriptor and IODMACommand buffers into sync.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn synchronize(IOOptionBits options);
```

#### Return_value

kIOReturnNotReady if not prepared, kIOReturnBadArgument if invalid options are passed, kIOReturnSuccess otherwise.

#### Discussion

This method should not be called unless a prepare was previously issued. If needed a caller may synchronize any IODMACommand buffers with the original IOMemoryDescriptor buffers.

## Parameters

- `options`: Specifies the direction of the copy: kIODirectionOut copy IOMemoryDesciptor memory to any IODMACommand buffers. By default this action takes place automatically at prepare(). kIODirectionIn copy any IODMACommand buffers back to the IOMemoryDescriptor. By default this action takes place automatically at complete(). kForceDoubleBuffer copy the entire prepared range to a new page aligned buffer.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodmacommand/1547719-synchronize)*