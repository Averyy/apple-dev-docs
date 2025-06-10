# complete

**Framework**: Kernel  
**Kind**: instm

Complete processing of the memory after an I/O transfer finishes.

## Declaration

```swift
virtual IOReturn complete(
 IODirection forDirection = forDirection);
```

#### Return_value

An IOReturn code.

#### Overview

This method should not be called unless a prepare was previously issued; the prepare() and complete() must occur in pairs, before and after an I/O transfer involving pageable memory.

## Parameters

- `forDirection`: The direction of the I/O just completed, or kIODirectionNone for the direction specified by the memory descriptor.

## See Also

- [clearMemoryDescriptors](iointerleavedmemorydescriptor/1812566-clearmemorydescriptors.md)
  Clear all of the IOMemoryDescriptors currently contained in and reset the IOInterleavedMemoryDescriptor.
- [getPhysicalSegment](iointerleavedmemorydescriptor/1812587-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithCapacity](iointerleavedmemorydescriptor/1812598-initwithcapacity.md)
  Initialize an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](iointerleavedmemorydescriptor/1812608-prepare.md)
  Prepare the memory for an I/O transfer.
- [setMemoryDescriptor](iointerleavedmemorydescriptor/1812618-setmemorydescriptor.md)
  Add a portion of an IOMemoryDescriptor to the IOInterleavedMemoryDescriptor.
- [withCapacity](iointerleavedmemorydescriptor/1812626-withcapacity.md)
  Create an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerleavedmemorydescriptor/1812579-complete)*