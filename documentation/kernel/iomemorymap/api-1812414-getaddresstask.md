# getAddressTask

**Framework**: Kernel  
**Kind**: instm

Accessor to the task of the mapping.

## Declaration

```cpp
virtual task_t getAddressTask();
```

#### Return Value

A mach task_t.

#### Overview

This method returns the mach task the mapping exists in.

## See Also

### Miscellaneous
- [getAddress()](./api-1812407-getaddress.md)
  Accessor to the length of the mapping.
- [getLength](./api-1812419-getlength.md)
  Accessor to the length of the mapping.
- [getMapOptions](./api-1812423-getmapoptions.md)
  Accessor to the options the mapping was created with.
- [getMemoryDescriptor](./api-1812429-getmemorydescriptor.md)
  Accessor to the IOMemoryDescriptor the mapping was created from.
- [getPhysicalAddress](./api-1812435-getphysicaladdress.md)
  Return the physical address of the first byte in the mapping.
- [getPhysicalSegment](./api-1812443-getphysicalsegment.md)
  Break a mapping into its physically contiguous segments.
- [getSize()](./api-1812448-getsize.md)
  Accessor to the length of the mapping.
- [getVirtualAddress](./api-1812459-getvirtualaddress.md)
  Accessor to the virtual address of the first byte in the mapping.
- [redirect](./api-1812465-redirect.md)
  Replace the memory mapped in a process with new backing memory.
- [unmap](./api-1812474-unmap.md)
  Force the IOMemoryMap to unmap, without destroying the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/1812414-getaddresstask)*