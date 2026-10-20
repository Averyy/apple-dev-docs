# IOGeneralMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOGeneralMemoryDescriptor : IOMemoryDescriptor
```

## Topics

### Instance Methods
- [- complete](./iogeneralmemorydescriptor/api-1441780-complete.md)
- [- dmaCommandOperation](./iogeneralmemorydescriptor/api-1442088-dmacommandoperation.md)
- [- doMap](./iogeneralmemorydescriptor/api-1442080-domap.md)
- [- doUnmap](./iogeneralmemorydescriptor/api-1441833-dounmap.md)
- [- free](./iogeneralmemorydescriptor/api-1441867-free.md)
- [- getMetaClass](./iogeneralmemorydescriptor/api-1441800-getmetaclass.md)
- [- getPhysicalSegment](./iogeneralmemorydescriptor/api-1441769-getphysicalsegment.md)
- [- getPreparationID](./iogeneralmemorydescriptor/api-1441919-getpreparationid.md)
- [- initWithOptions](./iogeneralmemorydescriptor/api-1441853-initwithoptions.md)
- [- makeMapping](./iogeneralmemorydescriptor/api-4411034-makemapping.md)
- [- makeMapping](./iogeneralmemorydescriptor/api-4411035-makemapping.md)
- [- memoryReferenceCreateOptions](./iogeneralmemorydescriptor/api-4411036-memoryreferencecreateoptions.md)
- [- prepare](./iogeneralmemorydescriptor/api-1441875-prepare.md)
- [- serialize](./iogeneralmemorydescriptor/api-1441957-serialize.md)
- [- setOwnership](./iogeneralmemorydescriptor/api-3142951-setownership.md)
- [- setPurgeable](./iogeneralmemorydescriptor/api-1442059-setpurgeable.md)
### Type Methods
- [+ withPersistentMemoryDescriptor](./iogeneralmemorydescriptor/api-1441857-withpersistentmemorydescriptor.md)

## Relationships

### Inherits From
- [IOMemoryDescriptor](./iomemorydescriptor.md)

## See Also

### Descriptors
- [IOBufferMemoryDescriptor](./iobuffermemorydescriptor.md)
  A simple memory descriptor that allocates its own buffer memory.
- [IODeviceMemory](./iodevicememory.md)
  An IOMemoryDescriptor used for device physical memory ranges.
- [IOInterleavedMemoryDescriptor](./iointerleavedmemorydescriptor.md)
  The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.
- [IOMultiMemoryDescriptor](./iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](./iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](./iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogeneralmemorydescriptor)*