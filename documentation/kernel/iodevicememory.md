# IODeviceMemory

**Framework**: Kernel  
**Kind**: cl

An IOMemoryDescriptor used for device physical memory ranges.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IODeviceMemory : IOMemoryDescriptor
```

#### Overview

The IODeviceMemory class is a simple subclass of IOMemoryDescriptor that uses its methods to describe a single range of physical memory on a device. IODeviceMemory objects are usually looked up with IOService or IOPCIDevice accessors, and are created by memory-mapped bus families. IODeviceMemory implements only some factory methods in addition to the methods of IOMemoryDescriptor.

## Topics

### Miscellaneous
- [arrayFromList](iodevicememory/1811066-arrayfromlist.md)
  Constructs an OSArray of IODeviceMemory instances, each describing one physical range, and a tag value.
- [withRange](iodevicememory/1811085-withrange.md)
  Constructs an IODeviceMemory instance, describing one physical range.
- [withSubRange](iodevicememory/1811112-withsubrange.md)
  Constructs an IODeviceMemory instance, describing a subset of an existing IODeviceMemory range.
### DataTypes
- [InitElement](iodevicememory/initelement.md)
### Instance Methods
- [- getMetaClass](iodevicememory/1392267-getmetaclass.md)
### Type Methods
- [+ arrayFromList](iodevicememory/1392273-arrayfromlist.md)
- [+ withRange](iodevicememory/1392276-withrange.md)
- [+ withSubRange](iodevicememory/1392269-withsubrange.md)

## Relationships

### Inherits From
- [IOMemoryDescriptor](iomemorydescriptor.md)

## See Also

- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A simple memory descriptor that allocates its own buffer memory.
- [IOGeneralMemoryDescriptor](iogeneralmemorydescriptor.md)
- [IOInterleavedMemoryDescriptor](iointerleavedmemorydescriptor.md)
  The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.
- [IOMultiMemoryDescriptor](iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodevicememory)*