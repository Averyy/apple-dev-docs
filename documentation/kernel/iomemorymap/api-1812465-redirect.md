# redirect

**Framework**: Kernel  
**Kind**: instm

Replace the memory mapped in a process with new backing memory.

## Declaration

```swift
#ifndef __LP64__
 virtual IOReturn redirect(
 IOMemoryDescriptor *newBackingMemory, 
 IOOptionBits options, 
 IOByteCount offset = 0); 
#endif
```

#### Return_value

An IOReturn code.

#### Overview

An IOMemoryMap created with the kIOMapUnique option to IOMemoryDescriptor::map() can remapped to a new IOMemoryDescriptor backing object. If the new IOMemoryDescriptor is specified as NULL, client access to the memory map is blocked until a new backing object has been set. By blocking access and copying data, the caller can create atomic copies of the memory while the client is potentially reading or writing the memory.

## Parameters

- `newBackingMemory`: The IOMemoryDescriptor that represents the physical memory that is to be now mapped in the virtual range the IOMemoryMap represents. If newBackingMemory is NULL, any access to the mapping will hang (in vm_fault()) until access has been restored by a new call to redirect() with non-NULL newBackingMemory argument.
- `options`: Mapping options are defined in IOTypes.h, and are documented in IOMemoryDescriptor::map()
- `offset`: As with IOMemoryDescriptor::map(), a beginning offset into the IOMemoryDescriptor's memory where the mapping starts. Zero is the default.

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
- [getSize()](iomemorymap/1812448-getsize.md)
  Accessor to the length of the mapping.
- [getVirtualAddress](iomemorymap/1812459-getvirtualaddress.md)
  Accessor to the virtual address of the first byte in the mapping.
- [unmap](iomemorymap/1812474-unmap.md)
  Force the IOMemoryMap to unmap, without destroying the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/1812465-redirect)*