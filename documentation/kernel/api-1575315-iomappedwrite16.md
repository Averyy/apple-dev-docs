# IOMappedWrite16

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Write two bytes to the desired "Physical" IOSpace address.

**Availability**:
- macOS 10.2+

## Declaration

```c
void IOMappedWrite16(IOPhysicalAddress address, UInt16 value);
```

## Discussion

Write two bytes to the desired "Physical" IOSpace address. This function allows the developer to write to an address returned from any memory descriptor's getPhysicalSegment routine.

## Parameters

- `address`: The desired address, as returned by IOMemoryDescriptor::getPhysicalSegment.
- `value`: Data to be writen to the desired location

## See Also

### Mapped Memory
- [IOMapper](./iomapper.md)
- [IOMemoryMap](./iomemorymap.md)
  A class defining common methods for describing a memory mapping.
- [IOMappedRead16](./api-1575322-iomappedread16.md)
  Read two bytes from the desired "Physical" IOSpace address.
- [IOMappedRead32](./api-1575311-iomappedread32.md)
  Read four bytes from the desired "Physical" IOSpace address.
- [IOMappedRead64](./api-1575301-iomappedread64.md)
  Read eight bytes from the desired "Physical" IOSpace address.
- [IOMappedRead8](./api-1575317-iomappedread8.md)
  Read one byte from the desired "Physical" IOSpace address.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575315-iomappedwrite16)*