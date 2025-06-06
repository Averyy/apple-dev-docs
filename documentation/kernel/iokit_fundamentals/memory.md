# Memory

**Framework**: Kernel

Allocate, map, free, and manage memory in the kernel. 

## Topics

### Descriptors
- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A simple memory descriptor that allocates its own buffer memory.
- [IODeviceMemory](iodevicememory.md)
  An IOMemoryDescriptor used for device physical memory ranges.
- [IOGeneralMemoryDescriptor](iogeneralmemorydescriptor.md)
- [IOInterleavedMemoryDescriptor](iointerleavedmemorydescriptor.md)
  The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.
- [IOMultiMemoryDescriptor](iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.
### Direct Memory Access (DMA)
- [IODMACommand](iodmacommand.md)
  An object that converts memory references to I/O bus addresses.
- [IODMAController](iodmacontroller.md)
- [IODMAEventSource](iodmaeventsource.md)
### Deallocation
- [IOFree](1575290-iofree.md)
  Frees memory allocated with IOMalloc.
- [IOFreeAligned](1575330-iofreealigned.md)
  Frees memory allocated with IOMallocAligned.
- [IOFreePageable](1575300-iofreepageable.md)
  Frees memory allocated with IOMallocPageable.
### Allocation
- [IOMalloc](1575326-iomalloc.md)
  Allocates general purpose, wired memory in the kernel map.
- [IOMallocAligned](1575291-iomallocaligned.md)
  Allocates wired memory in the kernel map, with an alignment restriction.
- [IOMallocPageable](1575327-iomallocpageable.md)
  Allocates pageable memory in the kernel map.
- [IOMallocZero](3074962-iomalloczero.md)
- [IORangeAllocator](iorangeallocator.md)
  A utility class to manage allocations from a range.
### Mapped Memory
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
- [IOFlushProcessorCache](1575308-ioflushprocessorcache.md)
  Flushes the processor cache for mapped memory.
### Cursors
- [IOBigMemoryCursor](iobigmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the big endian byte order.
- [IOLittleMemoryCursor](iolittlememorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the little endian byte order.
- [IONaturalMemoryCursor](ionaturalmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the natural byte orientation for the CPU.
- [IOMemoryCursor](iomemorycursor.md)
  A mechanism to convert memory references to physical addresses.

## See Also

- [Workflow and Control](iokit_fundamentals/workflow_and_control.md)
- [Locks](iokit_fundamentals/locks.md)
- [Data Types](libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokit_fundamentals/memory)*