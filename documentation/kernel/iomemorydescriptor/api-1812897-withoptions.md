# withOptions

**Framework**: Kernel  
**Kind**: instm

Primary initializer for all variants of memory descriptors.

## Declaration

```swift
static IOMemoryDescriptor *withOptions(
 void *buffers, 
 UInt32count, 
 UInt32offset, 
 task_ttask, 
 IOOptionBitsoptions, 
 IOMapper *mapper = mapper);
```

#### Return_value

The created IOMemoryDescriptor on success, to be released by the caller, or zero on failure.

#### Overview

This method creates and initializes an IOMemoryDescriptor for memory it has three main variants: Virtual, Physical & mach UPL. These variants are selected with the options parameter, see below. This memory descriptor needs to be prepared before it can be used to extract data from the memory described.

## Parameters

- `buffers`: A pointer to an array of IOAddressRange when options:type is kIOMemoryTypeVirtual64 or kIOMemoryTypePhysical64 or a 64bit kernel. For type UPL it is a upl_t returned by the mach/memory_object_types.h apis, primarily used internally by the UBC. IOVirtualRanges or IOPhysicalRanges are 32 bit only types for use when options:type is kIOMemoryTypeVirtual or kIOMemoryTypePhysical on 32bit kernels.
- `count`: options:type = Virtual or Physical count contains a count of the number of entires in the buffers array. For options:type = UPL this field contains a total length.
- `offset`: Only used when options:type = UPL, in which case this field contains an offset for the memory within the buffers upl.
- `task`: Only used options:type = Virtual, The task each of the virtual ranges are mapped into.
- `options`: kIOMemoryDirectionMask (options:direction) This nibble indicates the I/O direction to be associated with the descriptor, which may affect the operation of the prepare and complete methods on some architectures. kIOMemoryTypeMask (options:type) kIOMemoryTypeVirtual64, kIOMemoryTypeVirtual, kIOMemoryTypePhysical64, kIOMemoryTypePhysical, kIOMemoryTypeUPL Indicates that what type of memory basic memory descriptor to use. This sub-field also controls the interpretation of the buffers, count, offset & task parameters. kIOMemoryAsReference For options:type = Virtual or Physical this indicate that the memory descriptor need not copy the ranges array into local memory. This is an optimisation to try to minimise unnecessary allocations. kIOMemoryBufferPageable Only used by the IOBufferMemoryDescriptor as an indication that the kernel virtual memory is in fact pageable and we need to use the kernel pageable submap rather than the default map.
- `mapper`: Which IOMapper should be used to map the in-memory physical addresses into I/O space addresses. Defaults to 0 which indicates that the system mapper is to be used, if present.

## See Also

- [initWithOptions](iomemorydescriptor/1812826-initwithoptions.md)
  Primary initializer for all variants of memory descriptors. 
- [- initWithOptions](iomemorydescriptor/1441969-initwithoptions.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812897-withoptions)*