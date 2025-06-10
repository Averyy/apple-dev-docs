# prepare

**Framework**: Kernel  
**Kind**: instm

Prepare the memory for an I/O transfer.

## Declaration

```swift
virtual IOReturn prepare(
 IODirection forDirection = forDirection);
```

#### Return_value

An IOReturn code.

#### Overview

This involves paging in the memory, if necessary, and wiring it down for the duration of the transfer. The complete() method completes the processing of the memory after the I/O transfer finishes. This method need not called for non-pageable memory.

## Parameters

- `forDirection`: The direction of the I/O to be performed, or kIODirectionNone for the direction specified by the memory descriptor.

## See Also

- [clearMemoryDescriptors](iointerleavedmemorydescriptor/1812566-clearmemorydescriptors.md)
  Clear all of the IOMemoryDescriptors currently contained in and reset the IOInterleavedMemoryDescriptor.
- [complete](iointerleavedmemorydescriptor/1812579-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [getPhysicalSegment](iointerleavedmemorydescriptor/1812587-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [initWithCapacity](iointerleavedmemorydescriptor/1812598-initwithcapacity.md)
  Initialize an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [setMemoryDescriptor](iointerleavedmemorydescriptor/1812618-setmemorydescriptor.md)
  Add a portion of an IOMemoryDescriptor to the IOInterleavedMemoryDescriptor.
- [withCapacity](iointerleavedmemorydescriptor/1812626-withcapacity.md)
  Create an IOInterleavedMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerleavedmemorydescriptor/1812608-prepare)*