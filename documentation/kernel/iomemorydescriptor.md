# IOMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An abstract base class that defines common methods for describing physical or virtual memory.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOMemoryDescriptor : OSObject
```

## Overview

An [`IOMemoryDescriptor`](./iomemorydescriptor.md) object represents a buffer or range of memory, specified as one or more physical or virtual address ranges. It contains methods to return the memory's physically contiguous segments (fragments), for use with the [`IOMemoryCursor`](./iomemorycursor.md), and methods to map the memory into any address space with caching and placed mapping options.

## Topics

### Creating the Memory Buffer
- [initWithOptions](./iomemorydescriptor/api-1812826-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [- initWithOptions](./iomemorydescriptor/api-1441969-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [withOptions](./iomemorydescriptor/api-1812897-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [+ withOptions](./iomemorydescriptor/api-1441825-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [withAddress](./iomemorydescriptor/api-1812881-withaddress.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.
- [+ withAddress](./iomemorydescriptor/api-1442032-withaddress.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.
- [withAddressRange](./iomemorydescriptor/api-1812885-withaddressrange.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the specified map.
- [+ withAddressRange](./iomemorydescriptor/api-1441897-withaddressrange.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the specified map.
- [withAddressRanges](./iomemorydescriptor/api-1812892-withaddressranges.md)
  Creates an IOMemoryDescriptor to describe one or more virtual ranges.
- [+ withAddressRanges](./iomemorydescriptor/api-1441794-withaddressranges.md)
  Creates an IOMemoryDescriptor to describe one or more virtual ranges.
- [withPersistentMemoryDescriptor](./iomemorydescriptor/api-1812901-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [+ withPersistentMemoryDescriptor](./iomemorydescriptor/api-1441983-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [withPhysicalAddress](./iomemorydescriptor/api-1812908-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [+ withPhysicalAddress](./iomemorydescriptor/api-1441877-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [- free](./iomemorydescriptor/api-3180646-free.md)
  Performs any final cleanup for the memory descriptor object.
### Configuring the Descriptor
- [- setOwnership](./iomemorydescriptor/api-3142952-setownership.md)
  Set the task that owns the descriptor’s memory. 
- [setPurgeable](./iomemorydescriptor/api-1812865-setpurgeable.md)
  Control the purgeable status of a memory descriptors memory.
- [- setPurgeable](./iomemorydescriptor/api-1442065-setpurgeable.md)
  Control the purgeable status of a memory descriptors memory.
### Preparing the Buffer
- [prepare](./iomemorydescriptor/api-1812845-prepare.md)
  Prepare the memory for an I/O transfer.
- [- prepare](./iomemorydescriptor/api-1442024-prepare.md)
  Prepare the memory for an I/O transfer.
- [complete](./iomemorydescriptor/api-1812740-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [- complete](./iomemorydescriptor/api-1442043-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [- getPreparationID](./iomemorydescriptor/api-1441964-getpreparationid.md)
- [- setPreparationID](./iomemorydescriptor/api-1442011-setpreparationid.md)
### Reading and Writing Buffer Data
- [readBytes](./iomemorydescriptor/api-1812854-readbytes.md)
  Copy data from the memory descriptor's buffer to the specified buffer.
- [- readBytes](./iomemorydescriptor/api-1441823-readbytes.md)
  Copy data from the memory descriptor's buffer to the specified buffer.
- [writeBytes](./iomemorydescriptor/api-1812910-writebytes.md)
  Copy data to the memory descriptor's buffer from the specified buffer.
- [- writeBytes](./iomemorydescriptor/api-1442038-writebytes.md)
  Copy data to the memory descriptor's buffer from the specified buffer.
### Mapping to the Other Address Spaces
- [createMappingInTask](./iomemorydescriptor/api-1812752-createmappingintask.md)
  Maps an IOMemoryDescriptor into a task.
- [- createMappingInTask](./iomemorydescriptor/api-1441859-createmappingintask.md)
  Maps an IOMemoryDescriptor into a task.
- [map](./iomemorydescriptor/api-1812830-map.md)
  Maps an IOMemoryDescriptor into the kernel map.
- [- map](./iomemorydescriptor/api-1441908-map.md)
  Maps an IOMemoryDescriptor into the kernel map.
- [setMapping](./iomemorydescriptor/api-1812859-setmapping.md)
  Establishes an already existing mapping.
- [- setMapping](./iomemorydescriptor/api-1441948-setmapping.md)
  Establishes an already existing mapping.
### Getting the Memory Pages
- [getPageCounts](./iomemorydescriptor/api-1812787-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [- getPageCounts](./iomemorydescriptor/api-1441992-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [getPhysicalAddress](./iomemorydescriptor/api-1812795-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [- getPhysicalAddress](./iomemorydescriptor/api-1441916-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [getPhysicalSegment](./iomemorydescriptor/api-1812807-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [- getPhysicalSegment](./iomemorydescriptor/api-1442068-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
### Getting the Descriptor Information
- [getDirection](./iomemorydescriptor/api-1812765-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [- getDirection](./iomemorydescriptor/api-1441925-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [getLength](./iomemorydescriptor/api-1812776-getlength.md)
  Accessor to get the length of the memory descriptor (over all its ranges).
- [- getLength](./iomemorydescriptor/api-1442036-getlength.md)
  Accessor to get the length of the memory descriptor (over all its ranges).
- [- GetLength](./iomemorydescriptor/api-3180642-getlength.md)
  Returns the length of the memory block represented by this object.
- [- getDMAMapLength](./iomemorydescriptor/api-3553361-getdmamaplength.md)
- [- getFlags](./iomemorydescriptor/api-2870265-getflags.md)
  Returns the options used to create the memory descriptor.
- [- getMetaClass](./iomemorydescriptor/api-1442096-getmetaclass.md)
### Accessing the Buffer's Tag
- [getTag](./iomemorydescriptor/api-1812815-gettag.md)
  Accessor to the retrieve the tag for the memory descriptor.
- [- getTag](./iomemorydescriptor/api-1442070-gettag.md)
  Accessor to the retrieve the tag for the memory descriptor.
- [setTag](./iomemorydescriptor/api-1812873-settag.md)
  Set the tag for the memory descriptor.
- [- setTag](./iomemorydescriptor/api-1441787-settag.md)
  Set the tag for the memory descriptor.
- [- getVMTag](./iomemorydescriptor/api-3131493-getvmtag.md)
- [- setVMTags](./iomemorydescriptor/api-3131494-setvmtags.md)
### Operating on the Memory
- [performOperation](./iomemorydescriptor/api-1812840-performoperation.md)
  Perform an operation on the memory descriptor's memory.
- [- performOperation](./iomemorydescriptor/api-1441761-performoperation.md)
  Perform an operation on the memory descriptor's memory.
- [- dmaCommandOperation](./iomemorydescriptor/api-1442040-dmacommandoperation.md)
### Managing Internal Structures
- [reserved](./iomemorydescriptor/reserved.md)
- [+ initialize](./iomemorydescriptor/api-1441798-initialize.md)
- [- Dispatch](./iomemorydescriptor/api-3180641-dispatch.md)
- [+ CreateMapping_Invoke](./iomemorydescriptor/api-3174976-createmapping_invoke.md)
- [- populateDevicePager](./iomemorydescriptor/api-1442017-populatedevicepager.md)
- [- CreateMapping](./iomemorydescriptor/api-3174974-createmapping.md)
- [- CreateMapping_Impl](./iomemorydescriptor/api-3174975-createmapping_impl.md)
- [- Map](./iomemorydescriptor/api-3180643-map.md)
  Maps memory internally. 
- [- addMapping](./iomemorydescriptor/api-1442013-addmapping.md)
- [- removeMapping](./iomemorydescriptor/api-1441778-removemapping.md)
- [- makeMapping](./iomemorydescriptor/api-1441923-makemapping.md)
- [- doMap](./iomemorydescriptor/api-1441941-domap.md)
- [- doUnmap](./iomemorydescriptor/api-1441883-dounmap.md)
- [- handleFault](./iomemorydescriptor/api-1441782-handlefault.md)
- [- redirect](./iomemorydescriptor/api-1441871-redirect.md)
### Instance Methods
- [- getMapperOptions](./iomemorydescriptor/api-3917633-getmapperoptions.md)
- [- setMapperOptions](./iomemorydescriptor/api-3917634-setmapperoptions.md)
### Type Methods
- [+ CreateSubMemoryDescriptor](./iomemorydescriptor/api-3674611-createsubmemorydescriptor.md)
- [+ CreateSubMemoryDescriptor_Impl](./iomemorydescriptor/api-3674612-createsubmemorydescriptor_impl.md)
- [+ CreateSubMemoryDescriptor_Invoke](./iomemorydescriptor/api-3674613-createsubmemorydescriptor_invoke.md)
- [+ CreateWithMemoryDescriptors](./iomemorydescriptor/api-3674614-createwithmemorydescriptors.md)
- [+ CreateWithMemoryDescriptors_Impl](./iomemorydescriptor/api-3674615-createwithmemorydescriptors_impl.md)
- [+ CreateWithMemoryDescriptors_Invoke](./iomemorydescriptor/api-3674616-createwithmemorydescriptors_invo.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

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
- [IOSubMemoryDescriptor](./iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor)*