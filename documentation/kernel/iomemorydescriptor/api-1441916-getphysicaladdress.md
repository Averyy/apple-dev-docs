# getPhysicalAddress

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Return the physical address of the first byte in the memory.

**Availability**:
- macOS 10.11.4+

## Declaration

```c
IOPhysicalAddress getPhysicalAddress(void);
```

#### Return Value

A physical address.

#### Discussion

This method returns the physical address of the first byte in the memory. It is most useful on memory known to be physically contiguous.

## See Also

### Getting the Memory Pages
- [getPageCounts](./api-1812787-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [- getPageCounts](./api-1441992-getpagecounts.md)
  Retrieve the number of resident and/or dirty pages encompassed by a memory descriptor.
- [getPhysicalAddress](./api-1812795-getphysicaladdress.md)
  Return the physical address of the first byte in the memory.
- [getPhysicalSegment](./api-1812807-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.
- [- getPhysicalSegment](./api-1442068-getphysicalsegment.md)
  Break a memory descriptor into its physically contiguous segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441916-getphysicaladdress)*