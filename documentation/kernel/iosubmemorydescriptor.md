# IOSubMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOSubMemoryDescriptor : IOMemoryDescriptor
```

#### Overview

The IOSubMemoryDescriptor object represents a subrange of memory, specified as a portion of another IOMemoryDescriptor.

## Topics

### Miscellaneous
- [withSubRange](./iosubmemorydescriptor/api-1810054-withsubrange.md)
  Create an IOMemoryDescriptor to describe a subrange of an existing descriptor.
### Instance Methods
- [- complete](./iosubmemorydescriptor/api-1571786-complete.md)
- [- free](./iosubmemorydescriptor/api-1571785-free.md)
- [- getMetaClass](./iosubmemorydescriptor/api-1571787-getmetaclass.md)
- [- getPageCounts](./iosubmemorydescriptor/api-1571789-getpagecounts.md)
- [- getPhysicalSegment](./iosubmemorydescriptor/api-1571791-getphysicalsegment.md)
- [- getPreparationID](./iosubmemorydescriptor/api-1571793-getpreparationid.md)
- [- initSubRange](./iosubmemorydescriptor/api-1571781-initsubrange.md)
- [- makeMapping](./iosubmemorydescriptor/api-1571790-makemapping.md)
- [- prepare](./iosubmemorydescriptor/api-1571784-prepare.md)
- [- redirect](./iosubmemorydescriptor/api-1571788-redirect.md)
- [- setOwnership](./iosubmemorydescriptor/api-3142956-setownership.md)
- [- setPurgeable](./iosubmemorydescriptor/api-1571792-setpurgeable.md)
### Type Methods
- [+ withSubRange](./iosubmemorydescriptor/api-1571783-withsubrange.md)

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
- [IOMultiMemoryDescriptor](./iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOMemoryDescriptor](./iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iosubmemorydescriptor)*