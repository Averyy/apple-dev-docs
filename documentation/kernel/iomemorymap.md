# IOMemoryMap

**Framework**: Kernel  
**Kind**: cl

A class defining common methods for describing a memory mapping.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOMemoryMap : OSObject
```

#### Overview

The IOMemoryMap object represents a mapped range of memory, described by a IOMemoryDescriptor. The mapping may be in the kernel or a non-kernel task and has processor cache mode attributes. IOMemoryMap instances are created by IOMemoryDescriptor when it creates mappings in its map method, and returned to the caller.

## Topics

### Miscellaneous
- [getAddress()](iomemorymap/1812407-getaddress.md)
  Accessor to the length of the mapping.
- [getAddressTask](iomemorymap/1812414-getaddresstask.md)
  Accessor to the task of the mapping.
- [getLength](iomemorymap/1812419-getlength.md)
  Accessor to the length of the mapping.
- [getMapOptions](iomemorymap/1812423-getmapoptions.md)
  Accessor to the options the mapping was created with.
- [getMemoryDescriptor](iomemorymap/1812429-getmemorydescriptor.md)
  Accessor to the IOMemoryDescriptor the mapping was created from.
- [getPhysicalAddress](iomemorymap/1812435-getphysicaladdress.md)
  Return the physical address of the first byte in the mapping.
- [getPhysicalSegment](iomemorymap/1812443-getphysicalsegment.md)
  Break a mapping into its physically contiguous segments.
- [getSize()](iomemorymap/1812448-getsize.md)
  Accessor to the length of the mapping.
- [getVirtualAddress](iomemorymap/1812459-getvirtualaddress.md)
  Accessor to the virtual address of the first byte in the mapping.
- [redirect](iomemorymap/1812465-redirect.md)
  Replace the memory mapped in a process with new backing memory.
- [unmap](iomemorymap/1812474-unmap.md)
  Force the IOMemoryMap to unmap, without destroying the object.
### Instance Methods
- [- getAddress](1441813-getaddress.md)
- [- getSize](1441811-getsize.md)
- [- Dispatch](iomemorymap/3180655-dispatch.md)
- [- GetAddress](../driverkit/iomemorymap/getaddress.md)
  Returns the address of the memory block.
- [- GetLength](../driverkit/iomemorymap/getlength.md)
  Returns the length of the memory block in bytes.
- [- GetOffset](iomemorymap/3438204-getoffset.md)
  Returns the offset from the original start of the memory block.
- [- free](../driverkit/iomemorymap/free.md)
  Performs any final cleanup for the memory map object.
- [- getAddressTask](iomemorymap/1441809-getaddresstask.md)
- [- getLength](iomemorymap/1441789-getlength.md)
- [- getMapOptions](iomemorymap/1441764-getmapoptions.md)
- [- getMemoryDescriptor](iomemorymap/1441766-getmemorydescriptor.md)
- [- getMetaClass](iomemorymap/1441792-getmetaclass.md)
- [- getPhysicalAddress](iomemorymap/1441758-getphysicaladdress.md)
- [- getPhysicalSegment](iomemorymap/1441817-getphysicalsegment.md)
- [- getVirtualAddress](iomemorymap/1441843-getvirtualaddress.md)
- [- redirect](iomemorymap/1442054-redirect.md)
- [- taggedRelease](iomemorymap/1442001-taggedrelease.md)
- [- taskDied](iomemorymap/1442092-taskdied.md)
- [- unmap](iomemorymap/1441805-unmap.md)
- [- wireRange](iomemorymap/1442050-wirerange.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOMapper](iomapper.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap)*