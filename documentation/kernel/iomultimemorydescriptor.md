# IOMultiMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOMultiMemoryDescriptor : IOMemoryDescriptor
```

#### Overview

The IOMultiMemoryDescriptor object represents multiple ranges of memory, specified as an ordered list of IOMemoryDescriptors. The descriptors are chained end-to-end to make up a single contiguous buffer.

## Topics

### Miscellaneous
- [complete](./iomultimemorydescriptor/api-1812588-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](./iomultimemorydescriptor/api-1812610-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithDescriptors](./iomultimemorydescriptor/api-1812635-initwithdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](./iomultimemorydescriptor/api-1812660-prepare.md)
  Prepare the memory for an I/O transfer.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](./iomultimemorydescriptor/api-1812685-withdescriptors.md)
  Create an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](./iomultimemorydescriptor/api-1812714-withdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
### Instance Methods
- [- complete](./iomultimemorydescriptor/api-1553768-complete.md)
- [- doMap](./iomultimemorydescriptor/api-1553767-domap.md)
- [- free](./iomultimemorydescriptor/api-1553773-free.md)
- [- getMetaClass](./iomultimemorydescriptor/api-1553769-getmetaclass.md)
- [- getPageCounts](./iomultimemorydescriptor/api-1553777-getpagecounts.md)
- [- getPhysicalSegment](./iomultimemorydescriptor/api-1553770-getphysicalsegment.md)
- [- getPreparationID](./iomultimemorydescriptor/api-2967274-getpreparationid.md)
- [- initWithDescriptors](./iomultimemorydescriptor/api-1553772-initwithdescriptors.md)
- [- prepare](./iomultimemorydescriptor/api-1553771-prepare.md)
- [- setOwnership](./iomultimemorydescriptor/api-3142953-setownership.md)
- [- setPurgeable](./iomultimemorydescriptor/api-1553775-setpurgeable.md)
### Type Methods
- [+ withDescriptors](./iomultimemorydescriptor/api-1553774-withdescriptors.md)

## Relationships

### Inherits From
- [IOMemoryDescriptor](./iomemorydescriptor.md)

## See Also

### Descriptors
- [IOBufferMemoryDescriptor](./iobuffermemorydescriptor.md)
  A simple memory descriptor that allocates its own buffer memory.
- [IODeviceMemory](./iodevicememory.md)
  An IOMemoryDescriptor used for device physical memory ranges.
- [IOGeneralMemoryDescriptor](./iogeneralmemorydescriptor.md)
- [IOInterleavedMemoryDescriptor](./iointerleavedmemorydescriptor.md)
  The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](./iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](./iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomultimemorydescriptor)*