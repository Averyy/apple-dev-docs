# getPageCounts

**Framework**: Kernel  
**Kind**: instm

Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
IOReturn getPageCounts(IOByteCount *residentPageCount, IOByteCount *dirtyPageCount);
```

#### Return_value

An IOReturn code.

#### Discussion

This method returns the number of resident and/or dirty pages encompassed by an IOMemoryDescriptor.

## Parameters

- `residentPageCount`: - If non-null, a pointer to a byte count that will return the number of resident pages encompassed by this IOMemoryDescriptor.
- `dirtyPageCount`: - If non-null, a pointer to a byte count that will return the number of dirty pages encompassed by this IOMemoryDescriptor.

## See Also

- [getPageCounts](iomemorydescriptor/1812787-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [getPhysicalAddress](iomemorydescriptor/1812795-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [- getPhysicalAddress](iomemorydescriptor/1441916-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [getPhysicalSegment](iomemorydescriptor/1812807-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [- getPhysicalSegment](iomemorydescriptor/1442068-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441992-getpagecounts)*