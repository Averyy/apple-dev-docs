# IOFlushProcessorCache

**Framework**: Kernel  
**Kind**: func

Flushes the processor cache for mapped memory.

**Availability**:
- macOS 10.0+

## Declaration

```swift
IOReturn IOFlushProcessorCache(task_t task, IOVirtualAddress address, IOByteCount length);
```

#### Return_value

An IOReturn code.

#### Discussion

This function flushes the processor cache of an already mapped memory range. Note in most cases it is preferable to use IOMemoryDescriptor::prepare and complete to manage cache coherency since they are aware of the architecture's requirements. Flushing the processor cache is not required for coherency in most situations.

## Parameters

- `task`: Task the memory is mapped into.
- `address`: Virtual address of the memory.
- `length`: Length of the range to set.

## See Also

- [IOMapper](iomapper.md)
- [IOMemoryMap](iomemorymap.md)
  A class defining common methods for describing a memory mapping.
- [IOMappedRead16](1575322-iomappedread16.md)
  Read two bytes from the desired "Physical" IOSpace address.
- [IOMappedRead32](1575311-iomappedread32.md)
  Read four bytes from the desired "Physical" IOSpace address.
- [IOMappedRead64](1575301-iomappedread64.md)
  Read eight bytes from the desired "Physical" IOSpace address.
- [IOMappedRead8](1575317-iomappedread8.md)
  Read one byte from the desired "Physical" IOSpace address.
- [IOMappedWrite16](1575315-iomappedwrite16.md)
  Write two bytes to the desired "Physical" IOSpace address.
- [IOMappedWrite32](1575310-iomappedwrite32.md)
  Write four bytes to the desired "Physical" IOSpace address.
- [IOMappedWrite64](1575313-iomappedwrite64.md)
  Write eight bytes to the desired "Physical" IOSpace address.
- [IOMappedWrite8](1575318-iomappedwrite8.md)
  Write one byte to the desired "Physical" IOSpace address.
- [IOMapperIOVMAlloc](1532986-iomapperiovmalloc.md)
- [IOMapperIOVMFree](1532978-iomapperiovmfree.md)
- [IOMapperInsertPage](1532970-iomapperinsertpage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575308-ioflushprocessorcache)*