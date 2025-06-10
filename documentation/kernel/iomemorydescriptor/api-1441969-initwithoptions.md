# initWithOptions

**Framework**: Kernel  
**Kind**: instm

Primary initializer for all variants of memory descriptors. 

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual bool initWithOptions(void *buffers, UInt32 count, UInt32 offset, task_t task, IOOptionBits options, IOMapper *mapper);
```

#### Return_value

true on success, false on failure.

#### Discussion

For a more complete description see IOMemoryDescriptor::withOptions. Note this function can be used to re-init a previously created memory descriptor.

## See Also

- [initWithOptions](iomemorydescriptor/1812826-initwithoptions.md)
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
- [+ withPersistentMemoryDescriptor](iomemorydescriptor/1441983-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [withPhysicalAddress](iomemorydescriptor/1812908-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [+ withPhysicalAddress](iomemorydescriptor/1441877-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [- free](../driverkit/iomemorydescriptor/free.md)
  Performs any final cleanup for the memory descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441969-initwithoptions)*