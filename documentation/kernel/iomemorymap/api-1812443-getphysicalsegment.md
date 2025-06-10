# getPhysicalSegment

**Framework**: Kernel  
**Kind**: instm

Break a mapping into its physically contiguous segments.

## Declaration

```swift
#ifdef __LP64__
 virtual IOPhysicalAddress getPhysicalSegment(
 IOByteCount offset, 
 IOByteCount *length, 
 IOOptionBits options = 0); 
#else /* !__LP64__ */
virtual IOPhysicalAddress getPhysicalSegment(
 IOByteCount offset, 
 IOByteCount *length); 
#endif 
/* !__LP64__ */
```

#### Return_value

A physical address, or zero if the offset is beyond the length of the mapping.

#### Overview

This method returns the physical address of the byte at the given offset into the mapping, and optionally the length of the physically contiguous segment from that offset. It functions similarly to IOMemoryDescriptor::getPhysicalSegment.

## Parameters

- `offset`: A byte offset into the mapping whose physical address to return.
- `length`: If non-zero, getPhysicalSegment will store here the length of the physically contiguous segement at the given offset.

## See Also

- [getAddress()](iomemorymap/1812407-getaddress.md)
  Accessor to the length of the mapping.
- [getAddressTask](iomemorymap/1812414-getaddresstask.md)
  Accessor to the task of the mapping.
- [getLength](iomemorymap/1812419-getlength.md)
  Accessor to the length of the mapping.
- [getMapOptions](iomemorymap/1812423-getmapoptions.md)
  Accessor to the options the mapping was created with.
- [getMemoryDescriptor](iomemorymap/1812429-getmemorydescriptor.md)
  Accessor to the IOMemoryDescriptor the mapping was created from.
- [getPhysicalAddress](iomemorymap/1812435-getphysicaladdress.md)
  Return the physical address of the first byte in the mapping.
- [getSize()](iomemorymap/1812448-getsize.md)
  Accessor to the length of the mapping.
- [getVirtualAddress](iomemorymap/1812459-getvirtualaddress.md)
  Accessor to the virtual address of the first byte in the mapping.
- [redirect](iomemorymap/1812465-redirect.md)
  Replace the memory mapped in a process with new backing memory.
- [unmap](iomemorymap/1812474-unmap.md)
  Force the IOMemoryMap to unmap, without destroying the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/1812443-getphysicalsegment)*