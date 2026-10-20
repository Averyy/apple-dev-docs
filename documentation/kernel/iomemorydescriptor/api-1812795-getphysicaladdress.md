# getPhysicalAddress

**Framework**: Kernel  
**Kind**: instm

Return the physical address of the first byte in the memory.

## Declaration

```c
IOPhysicalAddress getPhysicalAddress();
```

#### Return Value

A physical address.

#### Overview

This method returns the physical address of the first byte in the memory. It is most useful on memory known to be physically contiguous.

## See Also

### Getting the Memory Pages
- [getPageCounts](./api-1812787-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [- getPageCounts](./api-1441992-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [- getPhysicalAddress](./api-1441916-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [getPhysicalSegment](./api-1812807-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [- getPhysicalSegment](./api-1442068-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1812795-getphysicaladdress)*