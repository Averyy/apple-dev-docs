# performOperation

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Perform an operation on the memory descriptor's memory.

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn performOperation(IOOptionBits options, IOByteCount offset, IOByteCount length);
```

#### Return Value

An IOReturn code.

#### Discussion

This method performs some operation on a range of the memory descriptor's memory. When a memory descriptor's memory is not mapped, it should be more efficient to use this method than mapping the memory to perform the operation virtually.

## Parameters

- `options`: The operation to perform on the memory:

  kIOMemoryIncoherentIOFlush - pass this option to store to memory and flush any data in the processor cache for the memory range, with synchronization to ensure the data has passed through all levels of processor cache. It may not be supported on all architectures. This type of flush may be used for non-coherent I/O such as AGP - it is NOT required for PCI coherent operations. The memory descriptor must have been previously prepared.

  kIOMemoryIncoherentIOStore - pass this option to store to memory any data in the processor cache for the memory range, with synchronization to ensure the data has passed through all levels of processor cache. It may not be supported on all architectures. This type of flush may be used for non-coherent I/O such as AGP - it is NOT required for PCI coherent operations. The memory descriptor must have been previously prepared.
- `offset`: A byte offset into the memory descriptor's memory.
- `length`: The length of the data range.

## See Also

### Operating on the Memory
- [performOperation](./api-1812840-performoperation.md)
  Perform an operation on the memory descriptor's memory.
- [- dmaCommandOperation](./api-1442040-dmacommandoperation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441761-performoperation)*