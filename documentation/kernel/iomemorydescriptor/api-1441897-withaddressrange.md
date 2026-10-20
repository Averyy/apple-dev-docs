# withAddressRange

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Creates an IOMemoryDescriptor to describe one virtual range of the specified map.

**Availability**:
- macOS 10.11.4+

## Declaration

```c
static OSPtr<IOMemoryDescriptor> withAddressRange(mach_vm_address_t address, mach_vm_size_t length, IOOptionBits options, task_t task);
```

#### Return Value

The created IOMemoryDescriptor on success, to be released by the caller, or zero on failure.

#### Discussion

This method creates and initializes an IOMemoryDescriptor for memory consisting of a single virtual memory range mapped into the specified map. This memory descriptor needs to be prepared before it can be used to extract data from the memory described.

## Parameters

- `address`: The virtual address of the first byte in the memory.
- `length`: The length of memory.
- `options`: kIOMemoryDirectionMask (options:direction) This nibble indicates the I/O direction to be associated with the descriptor, which may affect the operation of the prepare and complete methods on some architectures.
- `task`: The task the virtual ranges are mapped into. Note that unlike IOMemoryDescriptor::withAddress(), kernel_task memory must be explicitly prepared when passed to this api. The task argument may be NULL to specify memory by physical address.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441897-withaddressrange)*