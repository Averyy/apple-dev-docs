# IOMemoryMap

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

A class defining common methods for describing a memory mapping.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOMemoryMap : OSObject
```

#### Overview

The IOMemoryMap object represents a mapped range of memory, described by a IOMemoryDescriptor. The mapping may be in the kernel or a non-kernel task and has processor cache mode attributes. IOMemoryMap instances are created by IOMemoryDescriptor when it creates mappings in its map method, and returned to the caller.

## Topics

### Miscellaneous
- [getAddress()](./iomemorymap/api-1812407-getaddress.md)
  Accessor to the length of the mapping.
- [getAddressTask](./iomemorymap/api-1812414-getaddresstask.md)
  Accessor to the task of the mapping.
- [getLength](./iomemorymap/api-1812419-getlength.md)
  Accessor to the length of the mapping.
- [getMapOptions](./iomemorymap/api-1812423-getmapoptions.md)
  Accessor to the options the mapping was created with.
- [getMemoryDescriptor](./iomemorymap/api-1812429-getmemorydescriptor.md)
  Accessor to the IOMemoryDescriptor the mapping was created from.
- [getPhysicalAddress](./iomemorymap/api-1812435-getphysicaladdress.md)
  Return the physical address of the first byte in the mapping.
- [getPhysicalSegment](./iomemorymap/api-1812443-getphysicalsegment.md)
  Break a mapping into its physically contiguous segments.
- [getSize()](./iomemorymap/api-1812448-getsize.md)
  Accessor to the length of the mapping.
- [getVirtualAddress](./iomemorymap/api-1812459-getvirtualaddress.md)
  Accessor to the virtual address of the first byte in the mapping.
- [redirect](./iomemorymap/api-1812465-redirect.md)
  Replace the memory mapped in a process with new backing memory.
- [unmap](./iomemorymap/api-1812474-unmap.md)
  Force the IOMemoryMap to unmap, without destroying the object.
### Instance Methods
- [- getAddress](./api-1441813-getaddress.md)
- [- getSize](./api-1441811-getsize.md)
- [- Dispatch](./iomemorymap/api-3180655-dispatch.md)
- [- GetAddress](./iomemorymap/api-3180656-getaddress.md)
  Returns the address of the memory block.
- [- GetLength](./iomemorymap/api-3180657-getlength.md)
  Returns the length of the memory block in bytes.
- [- GetOffset](./iomemorymap/api-3438204-getoffset.md)
  Returns the offset from the original start of the memory block.
- [- free](./iomemorymap/api-3180658-free.md)
  Performs any final cleanup for the memory map object.
- [- getAddressTask](./iomemorymap/api-1441809-getaddresstask.md)
- [- getLength](./iomemorymap/api-1441789-getlength.md)
- [- getMapOptions](./iomemorymap/api-1441764-getmapoptions.md)
- [- getMemoryDescriptor](./iomemorymap/api-1441766-getmemorydescriptor.md)
- [- getMetaClass](./iomemorymap/api-1441792-getmetaclass.md)
- [- getPhysicalAddress](./iomemorymap/api-1441758-getphysicaladdress.md)
- [- getPhysicalSegment](./iomemorymap/api-1441817-getphysicalsegment.md)
- [- getVirtualAddress](./iomemorymap/api-1441843-getvirtualaddress.md)
- [- redirect](./iomemorymap/api-1442054-redirect.md)
- [- taggedRelease](./iomemorymap/api-1442001-taggedrelease.md)
- [- taskDied](./iomemorymap/api-1442092-taskdied.md)
- [- unmap](./iomemorymap/api-1441805-unmap.md)
- [- wireRange](./iomemorymap/api-1442050-wirerange.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

## See Also

### Mapped Memory
- [IOMapper](./iomapper.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap)*