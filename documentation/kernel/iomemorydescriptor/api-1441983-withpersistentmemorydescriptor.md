# withPersistentMemoryDescriptor

**Framework**: Kernel  
**Kind**: clm

Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static OSPtr<IOMemoryDescriptor> withPersistentMemoryDescriptor(IOMemoryDescriptor *originalMD);
```

#### Return_value

Either the original memory descriptor with an additional retain or a new memory descriptor, 0 for a bad original memory descriptor or some other resource shortage.

#### Discussion

If the original memory descriptor's address and length is still backed by the same real memory, i.e. the user hasn't deallocated and the reallocated memory at the same address then the original memory descriptor is returned with a additional reference. Otherwise we build a totally new memory descriptor with the same characteristics as the previous one but with a new view of the vm. Note not legal to call this function with anything except an IOGeneralMemoryDescriptor that was created with the kIOMemoryPersistent option.

## Parameters

- `originalMD`: The memory descriptor to be duplicated.

## See Also

- [initWithOptions](iomemorydescriptor/1812826-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [- initWithOptions](iomemorydescriptor/1441969-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [withOptions](iomemorydescriptor/1812897-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [+ withOptions](iomemorydescriptor/1441825-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [withAddress](iomemorydescriptor/1812881-withaddress.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.
- [+ withAddress](iomemorydescriptor/1442032-withaddress.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.
- [withAddressRange](iomemorydescriptor/1812885-withaddressrange.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the specified map.
- [+ withAddressRange](iomemorydescriptor/1441897-withaddressrange.md)
  Creates an IOMemoryDescriptor to describe one virtual range of the specified map.
- [withAddressRanges](iomemorydescriptor/1812892-withaddressranges.md)
  Creates an IOMemoryDescriptor to describe one or more virtual ranges.
- [+ withAddressRanges](iomemorydescriptor/1441794-withaddressranges.md)
  Creates an IOMemoryDescriptor to describe one or more virtual ranges.
- [withPersistentMemoryDescriptor](iomemorydescriptor/1812901-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [withPhysicalAddress](iomemorydescriptor/1812908-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [+ withPhysicalAddress](iomemorydescriptor/1441877-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [- free](../driverkit/iomemorydescriptor/free.md)
  Performs any final cleanup for the memory descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441983-withpersistentmemorydescriptor)*