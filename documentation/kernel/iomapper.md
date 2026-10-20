# IOMapper

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.2+

## Declaration

```cpp
class IOMapper : IOService
```

## Topics

### Creating a Mapper Object
- [+ copyMapperForDevice](./iomapper/api-1532972-copymapperfordevice.md)
- [+ copyMapperForDeviceWithIndex](./iomapper/api-1532964-copymapperfordevicewithindex.md)
- [- initHardware](./iomapper/api-1532965-inithardware.md)
- [- start](./iomapper/api-1532981-start.md)
- [- free](./iomapper/api-1532982-free.md)
### Mapping Memory Addresses
- [- mapToPhysicalAddress](./iomapper/api-1532966-maptophysicaladdress.md)
- [- iovmMapMemory](./iomapper/api-1532977-iovmmapmemory.md)
- [- iovmUnmapMemory](./iomapper/api-1532968-iovmunmapmemory.md)
- [- iovmInsert](./iomapper/api-1532983-iovminsert.md)
### Determining the Mapper's Availability
- [+ checkForSystemMapper](./iomapper/api-1532973-checkforsystemmapper.md)
- [+ setMapperRequired](./iomapper/api-1532989-setmapperrequired.md)
- [+ waitForSystemMapper](./iomapper/api-1532985-waitforsystemmapper.md)
### Getting Configuration Details
- [- getMetaClass](./iomapper/api-1532963-getmetaclass.md)
- [- getPageSize](./iomapper/api-1532979-getpagesize.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Mapped Memory
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper)*