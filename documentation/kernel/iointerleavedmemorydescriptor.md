# IOInterleavedMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.

**Availability**:
- macOS 10.5+

## Declaration

```cpp
class IOInterleavedMemoryDescriptor : IOMemoryDescriptor
```

## Overview

The IOInterleavedMemoryDescriptor object represents interleaved ranges of memory, specified as an ordered list of portions of individual IOMemoryDescriptors. The portions are chained end-to-end to make up a single contiguous buffer.

## Topics

### Miscellaneous
- [clearMemoryDescriptors](./iointerleavedmemorydescriptor/api-1812566-clearmemorydescriptors.md)
  Clear all of the IOMemoryDescriptors currently contained in and reset the IOInterleavedMemoryDescriptor.
- [complete](./iointerleavedmemorydescriptor/api-1812579-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](./iointerleavedmemorydescriptor/api-1812587-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithCapacity](./iointerleavedmemorydescriptor/api-1812598-initwithcapacity.md)
  Initialize an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](./iointerleavedmemorydescriptor/api-1812608-prepare.md)
  Prepare the memory for an I/O transfer.
- [setMemoryDescriptor](./iointerleavedmemorydescriptor/api-1812618-setmemorydescriptor.md)
  Add a portion of an IOMemoryDescriptor to the IOInterleavedMemoryDescriptor.
- [withCapacity](./iointerleavedmemorydescriptor/api-1812626-withcapacity.md)
  Create an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
### Instance Methods
- [- clearMemoryDescriptors](./iointerleavedmemorydescriptor/api-1496079-clearmemorydescriptors.md)
- [- complete](./iointerleavedmemorydescriptor/api-1496082-complete.md)
- [- free](./iointerleavedmemorydescriptor/api-1496091-free.md)
- [- getMetaClass](./iointerleavedmemorydescriptor/api-1496080-getmetaclass.md)
- [- getPhysicalSegment](./iointerleavedmemorydescriptor/api-1496075-getphysicalsegment.md)
- [- initWithCapacity](./iointerleavedmemorydescriptor/api-1496089-initwithcapacity.md)
- [- prepare](./iointerleavedmemorydescriptor/api-1496087-prepare.md)
- [- setMemoryDescriptor](./iointerleavedmemorydescriptor/api-1496084-setmemorydescriptor.md)
### Type Methods
- [+ withCapacity](./iointerleavedmemorydescriptor/api-1496077-withcapacity.md)

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
- [IOMultiMemoryDescriptor](./iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](./iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](./iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerleavedmemorydescriptor)*