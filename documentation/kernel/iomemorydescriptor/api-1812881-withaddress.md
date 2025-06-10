# withAddress

**Framework**: Kernel  
**Kind**: instm

Creates an IOMemoryDescriptor to describe one virtual range of the kernel task.

## Declaration

```swift
static IOMemoryDescriptor * withAddress(
 void *address, 
 IOByteCountwithLength, 
 IODirectionwithDirection);
```

#### Return_value

The created IOMemoryDescriptor on success, to be released by the caller, or zero on failure.

#### Overview

This method creates and initializes an IOMemoryDescriptor for memory consisting of a single virtual memory range mapped into the kernel map. This memory descriptor needs to be prepared before it can be used to extract data from the memory described.

## Parameters

- `address`: The virtual address of the first byte in the memory.
- `withLength`: The length of memory.
- `withDirection`: An I/O direction to be associated with the descriptor, which may affect the operation of the prepare and complete methods on some architectures.

## See Also

- [initWithOptions](iomemorydescriptor/1812826-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [- initWithOptions](iomemorydescriptor/1441969-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [withOptions](iomemorydescriptor/1812897-withoptions.md)
  Primary initializer for all variants of memory descriptors.
- [+ withOptions](iomemorydescriptor/1441825-withoptions.md)
  Primary initializer for all variants of memory descriptors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812881-withaddress)*