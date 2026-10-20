# initWithOptions

**Framework**: Kernel  
**Kind**: instm

Primary initializer for all variants of memory descriptors. 

## Declaration

```cpp
virtual bool initWithOptions(
 void *buffers, 
 UInt32 count, 
 UInt32 offset, 
 task_t task, 
 IOOptionBits options, 
 IOMapper *mapper = kIOMapperSystem);
```

#### Return Value

true on success, false on failure.

#### Overview

Note this function can be used to re-init a previously created memory descriptor. For a more complete description see [`withOptions`](./api-1441825-withoptions.md).

## See Also

### Creating the Memory Buffer
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
- [withPersistentMemoryDescriptor](./api-1812901-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [+ withPersistentMemoryDescriptor](./api-1441983-withpersistentmemorydescriptor.md)
  Copy constructor that generates a new memory descriptor if the backing memory for the same task's virtual address and length has changed.
- [withPhysicalAddress](./api-1812908-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [+ withPhysicalAddress](./api-1441877-withphysicaladdress.md)
  Creates an IOMemoryDescriptor to describe one physical range.
- [- free](./api-3180646-free.md)
  Performs any final cleanup for the memory descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812826-initwithoptions)*