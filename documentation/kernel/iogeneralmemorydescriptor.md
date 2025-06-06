# IOGeneralMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOGeneralMemoryDescriptor : IOMemoryDescriptor
```

## Topics

### Instance Methods
- [- complete](iogeneralmemorydescriptor/1441780-complete.md)
- [- dmaCommandOperation](iogeneralmemorydescriptor/1442088-dmacommandoperation.md)
- [- doMap](iogeneralmemorydescriptor/1442080-domap.md)
- [- doUnmap](iogeneralmemorydescriptor/1441833-dounmap.md)
- [- free](iogeneralmemorydescriptor/1441867-free.md)
- [- getMetaClass](iogeneralmemorydescriptor/1441800-getmetaclass.md)
- [- getPhysicalSegment](iogeneralmemorydescriptor/1441769-getphysicalsegment.md)
- [- getPreparationID](iogeneralmemorydescriptor/1441919-getpreparationid.md)
- [- initWithOptions](iogeneralmemorydescriptor/1441853-initwithoptions.md)
- [- makeMapping](iogeneralmemorydescriptor/4411034-makemapping.md)
- [- makeMapping](iogeneralmemorydescriptor/4411035-makemapping.md)
- [- memoryReferenceCreateOptions](iogeneralmemorydescriptor/4411036-memoryreferencecreateoptions.md)
- [- prepare](iogeneralmemorydescriptor/1441875-prepare.md)
- [- serialize](iogeneralmemorydescriptor/1441957-serialize.md)
- [- setOwnership](iogeneralmemorydescriptor/3142951-setownership.md)
- [- setPurgeable](iogeneralmemorydescriptor/1442059-setpurgeable.md)
### Type Methods
- [+ withPersistentMemoryDescriptor](iogeneralmemorydescriptor/1441857-withpersistentmemorydescriptor.md)

## Relationships

### Inherits From
- [IOMemoryDescriptor](iomemorydescriptor.md)

## See Also

- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A simple memory descriptor that allocates its own buffer memory.
- [IODeviceMemory](iodevicememory.md)
  An IOMemoryDescriptor used for device physical memory ranges.
- [IOInterleavedMemoryDescriptor](iointerleavedmemorydescriptor.md)
  The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.
- [IOMultiMemoryDescriptor](iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogeneralmemorydescriptor)*