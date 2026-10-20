# virtualToPhysical

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
IOReturn virtualToPhysical(IOVirtualRange ranges[], unsigned int rangeCount, IOMemoryCursor::IOMemoryCursor::PhysicalSegment outSegments[], unsigned int & outPhysicalSegmentCount, unsigned int maxSegments);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodclprogram/1563449-virtualtophysical)*