# getPhysicalSegment

**Framework**: Kernel  
**Kind**: instm

Break a memory descriptor into its physically contiguous segments.

## Declaration

```swift
virtual addr64_t getPhysicalSegment(
 IOByteCountoffset, 
 IOByteCount *length, 
 IOOptionBits options = 0 );
```

#### Return_value

A physical address, or zero if the offset is beyond the length of the memory.

#### Overview

This method returns the physical address of the byte at the given offset into the memory, and optionally the length of the physically contiguous segment from that offset.

## Parameters

- `offset`: A byte offset into the memory whose physical address to return.
- `length`: If non-zero, getPhysicalSegment will store here the length of the physically contiguous segement at the given offset.

## See Also

- [complete](iomultimemorydescriptor/1812588-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [initWithDescriptors](iomultimemorydescriptor/1812635-initwithdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [prepare](iomultimemorydescriptor/1812660-prepare.md)
  Prepare the memory for an I/O transfer.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](iomultimemorydescriptor/1812685-withdescriptors.md)
  Create an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.
- [withDescriptors(IOMemoryDescriptor **, UInt32, IODirection, bool)](iomultimemorydescriptor/1812714-withdescriptors.md)
  Initialize an IOMultiMemoryDescriptor to describe a memory area made up of several other IOMemoryDescriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomultimemorydescriptor/1812610-getphysicalsegment)*