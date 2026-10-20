# IOMappedRead32

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Read four bytes from the desired "Physical" IOSpace address.

**Availability**:
- macOS 10.2+

## Declaration

```c
UInt32 IOMappedRead32(IOPhysicalAddress address);
```

#### Return Value

Data contained at that location

#### Discussion

Read four bytes from the desired "Physical" IOSpace address. This function allows the developer to read an address returned from any memory descriptor's getPhysicalSegment routine. It can then be used by segmenting a physical page slightly to tag the physical page with its kernel space virtual address.

## Parameters

- `address`: The desired address, as returned by IOMemoryDescriptor::getPhysicalSegment.

## See Also

### Mapped Memory
- [IOMapper](./iomapper.md)
- [IOMemoryMap](./iomemorymap.md)
  A class defining common methods for describing a memory mapping.
- [IOMappedRead16](./api-1575322-iomappedread16.md)
  Read two bytes from the desired "Physical" IOSpace address.
- [IOMappedRead64](./api-1575301-iomappedread64.md)
  Read eight bytes from the desired "Physical" IOSpace address.
- [IOMappedRead8](./api-1575317-iomappedread8.md)
  Read one byte from the desired "Physical" IOSpace address.
- [IOMappedWrite16](./api-1575315-iomappedwrite16.md)
  Write two bytes to the desired "Physical" IOSpace address.
- [IOMappedWrite32](./api-1575310-iomappedwrite32.md)
  Write four bytes to the desired "Physical" IOSpace address.
- [IOMappedWrite64](./api-1575313-iomappedwrite64.md)
  Write eight bytes to the desired "Physical" IOSpace address.
- [IOMappedWrite8](./api-1575318-iomappedwrite8.md)
  Write one byte to the desired "Physical" IOSpace address.
- [IOMapperIOVMAlloc](./api-1532986-iomapperiovmalloc.md)
- [IOMapperIOVMFree](./api-1532978-iomapperiovmfree.md)
- [IOMapperInsertPage](./api-1532970-iomapperinsertpage.md)
- [IOFlushProcessorCache](./api-1575308-ioflushprocessorcache.md)
  Flushes the processor cache for mapped memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575311-iomappedread32)*