# releaseAGPMemory

**Framework**: Kernel  
**Kind**: instm

Releases memory addressable by AGP transactions.

## Declaration

```swift
virtual IOReturn releaseAGPMemory(
 IOMemoryDescriptor *memory, 
 IOByteCount agpOffset, 
 IOOptionBits options = 0 );
```

#### Return_value

Returns an IOReturn code indicating success or failure.

#### Overview

Makes the memory described by the IOMemoryDescriptor object unaddressable by AGP by removing its pages from the GART array, given an offset into AGP space supplied by the caller (usually allocated by the AGP range allocator). It is the caller's responsibility to complete non-kernel pageable memory before calling this method, with IOMemoryDescriptor::complete.

## Parameters

- `memory`: A IOMemoryDescriptor object describing the memory to remove from the GART.
- `agpOffset`: An offset into AGP space that the caller has allocated - usually allocated by the AGP range allocator.
- `options`: Pass kIOAGPGartInvalidate if the AGP target should invalidate any GART TLB.

## See Also

- [commitAGPMemory](ioagpdevice/1811820-commitagpmemory.md)
  Makes memory addressable by AGP transactions.
- [createAGPSpace](ioagpdevice/1811842-createagpspace.md)
  Allocates the AGP space, and enables AGP transactions on the primary and secondary.
- [destroyAGPSpace](ioagpdevice/1811870-destroyagpspace.md)
  Destroys the AGP space, and disables AGP transactions on the primary and secondary.
- [getAGPRangeAllocator](ioagpdevice/1811894-getagprangeallocator.md)
  Accessor to obtain the AGP range allocator.
- [getAGPSpace](ioagpdevice/1811914-getagpspace.md)
  Returns the allocated AGP space.
- [getAGPStatus](ioagpdevice/1811928-getagpstatus.md)
  Returns the current state of the AGP bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioagpdevice/1811943-releaseagpmemory)*