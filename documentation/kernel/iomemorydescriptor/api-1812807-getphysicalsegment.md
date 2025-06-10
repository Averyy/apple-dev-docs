# getPhysicalSegment

**Framework**: Kernel  
**Kind**: instm

Break a memory descriptor into its physically contiguous segments.

## Declaration

```swift
#ifdef __LP64__
 virtual addr64_t getPhysicalSegment(
 IOByteCount offset, 
 IOByteCount *length, 
 IOOptionBits options = 0 ) = 0; 
#else /* !__LP64__ */
virtual addr64_t getPhysicalSegment(
 IOByteCount offset, 
 IOByteCount *length, 
 IOOptionBits options ); 
#endif 
/* !__LP64__ */
```

#### Return_value

A physical address, or zero if the offset is beyond the length of the memory.

#### Overview

This method returns the physical address of the byte at the given offset into the memory, and optionally the length of the physically contiguous segment from that offset.

## Parameters

- `offset`: A byte offset into the memory whose physical address to return.
- `length`: If non-zero, getPhysicalSegment will store here the length of the physically contiguous segement at the given offset.
- `options`: Additional options.

## See Also

- [getPageCounts](iomemorydescriptor/1812787-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [- getPageCounts](iomemorydescriptor/1441992-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [getPhysicalAddress](iomemorydescriptor/1812795-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [- getPhysicalAddress](iomemorydescriptor/1441916-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [- getPhysicalSegment](iomemorydescriptor/1442068-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812807-getphysicalsegment)*