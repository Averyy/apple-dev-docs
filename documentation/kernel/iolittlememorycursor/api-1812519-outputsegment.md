# outputSegment

**Framework**: Kernel  
**Kind**: instm

Outputs the given segment into the output segments array in little endian byte order.

## Declaration

```swift
static void outputSegment(
 PhysicalSegmentsegment, 
 void *segments, 
 UInt32segmentIndex);
```

## Parameters

- `segment`: The physical address and length that is next to be output.
- `segments`: Base of the output vector of DMA address length pairs.
- `segmentIndex`: Index to output 'segment' in the 'segments' array.

## See Also

- [getPhysicalSegments](iolittlememorycursor/1812505-getphysicalsegments.md)
  Generates a little endian physical scatter/gather list given a memory descriptor.
- [initWithSpecification](iolittlememorycursor/1812512-initwithspecification.md)
  Primary initializer for the IOLittleMemoryCursor class.
- [withSpecification](iolittlememorycursor/1812526-withspecification.md)
  Creates and initializes an IOLittleMemoryCursor in one operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iolittlememorycursor/1812519-outputsegment)*