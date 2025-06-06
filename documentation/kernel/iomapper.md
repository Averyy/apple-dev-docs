# IOMapper

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOMapper : IOService
```

## Topics

### Creating a Mapper Object
- [+ copyMapperForDevice](iomapper/1532972-copymapperfordevice.md)
- [+ copyMapperForDeviceWithIndex](iomapper/1532964-copymapperfordevicewithindex.md)
- [- initHardware](iomapper/1532965-inithardware.md)
- [- start](iomapper/1532981-start.md)
- [- free](iomapper/1532982-free.md)
### Mapping Memory Addresses
- [- mapToPhysicalAddress](iomapper/1532966-maptophysicaladdress.md)
- [- iovmMapMemory](iomapper/1532977-iovmmapmemory.md)
- [- iovmUnmapMemory](iomapper/1532968-iovmunmapmemory.md)
- [- iovmInsert](iomapper/1532983-iovminsert.md)
### Determining the Mapper's Availability
- [+ checkForSystemMapper](iomapper/1532973-checkforsystemmapper.md)
- [+ setMapperRequired](iomapper/1532989-setmapperrequired.md)
- [+ waitForSystemMapper](iomapper/1532985-waitforsystemmapper.md)
### Getting Configuration Details
- [- getMetaClass](iomapper/1532963-getmetaclass.md)
- [- getPageSize](iomapper/1532979-getpagesize.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

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
- [IOFlushProcessorCache](1575308-ioflushprocessorcache.md)
  Flushes the processor cache for mapped memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomapper)*