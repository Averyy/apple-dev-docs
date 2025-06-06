# IOMallocContiguous

**Framework**: Kernel  
**Kind**: func

Deprecated - use IOBufferMemoryDescriptor. Allocates wired memory in the kernel map, with an alignment restriction and physically contiguous.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```swift
void * IOMallocContiguous(vm_size_t size, vm_size_t alignment, IOPhysicalAddress *physicalAddress);
```

#### Return_value

Virtual address of the allocated memory, or zero on failure.

#### Discussion

This is a utility to allocate memory in the kernel, with an alignment restriction which is specified as a byte count, and will allocate only physically contiguous memory. The request may fail if memory is fragmented, and may cause large amounts of paging activity. This function may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `size`: Size of the memory requested.
- `alignment`: Byte count of the alignment for the memory. For example, pass 256 to get memory allocated at an address with bits 0-7 zero.
- `physicalAddress`: IOMallocContiguous returns the physical address of the allocated memory here, if physicalAddress is a non-zero pointer. The physicalAddress argument is deprecated and should be passed as NULL. To obtain the physical address for a memory buffer, use the IODMACommand class in conjunction with the IOMemoryDescriptor or IOBufferMemoryDescriptor classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575289-iomalloccontiguous)*