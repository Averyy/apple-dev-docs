# withPersistentMemoryDescriptor

**Framework**: Kernel  
**Kind**: instm

Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.

## Declaration

```c
static IOMemoryDescriptor * withPersistentMemoryDescriptor(
 IOMemoryDescriptor *originalMD);
```

#### Return Value

Either the original memory descriptor with an additional retain or a new memory descriptor, 0 for a bad original memory descriptor or some other resource shortage.

#### Overview

If the original memory descriptor's address and length is still backed by the same real memory, i.e. the user hasn't deallocated and the reallocated memory at the same address then the original memory descriptor is returned with a additional reference. Otherwise we build a totally new memory descriptor with the same characteristics as the previous one but with a new view of the vm. Note not legal to call this function with anything except an IOGeneralMemoryDescriptor that was created with the kIOMemoryPersistent option.

## Parameters

- `originalMD`: The memory descriptor to be duplicated.

## See Also

### Creating the Memory Buffer
- [initWithOptions](./api-1812826-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [- initWithOptions](./api-1441969-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [withOptions](./api-1812897-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [+ withOptions](./api-1441825-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [withAddress](./api-1812881-withaddress.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.
- [+ withAddress](./api-1442032-withaddress.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.
- [withAddressRange](./api-1812885-withaddressrange.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the specified map.
- [+ withAddressRange](./api-1441897-withaddressrange.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the specified map.
- [withAddressRanges](./api-1812892-withaddressranges.md)
  Creates an IOMemoryDescriptor to describe one or more virtual ranges.
- [+ withAddressRanges](./api-1441794-withaddressranges.md)
  Creates an IOMemoryDescriptor to describe one or more virtual ranges.
- [+ withPersistentMemoryDescriptor](./api-1441983-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [withPhysicalAddress](./api-1812908-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [+ withPhysicalAddress](./api-1441877-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [- free](./api-3180646-free.md)
  Performs any final cleanup for the memory descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812901-withpersistentmemorydescriptor)*