# getSize()

**Framework**: Kernel  
**Kind**: instm

Accessor to the length of the mapping.

## Declaration

```swift
virtual mach_vm_address_t getAddress();
```

#### Return_value

A byte count.

#### Overview

This method returns the length of the mapping.

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
- [getPhysicalSegment](iomemorymap/1812443-getphysicalsegment.md)
  Break a mapping into its physically contiguous segments.
- [getVirtualAddress](iomemorymap/1812459-getvirtualaddress.md)
  Accessor to the virtual address of the first byte in the mapping.
- [redirect](iomemorymap/1812465-redirect.md)
  Replace the memory mapped in a process with new backing memory.
- [unmap](iomemorymap/1812474-unmap.md)
  Force the IOMemoryMap to unmap, without destroying the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/1812448-getsize)*