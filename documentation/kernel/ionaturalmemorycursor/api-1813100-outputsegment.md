# outputSegment

**Framework**: Kernel  
**Kind**: instm

Outputs the given segment into the output segments array in natural byte order.

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

- [getPhysicalSegments](ionaturalmemorycursor/1813076-getphysicalsegments.md)
  Generates a CPU natural physical scatter/gather list given a memory descriptor.
- [initWithSpecification](ionaturalmemorycursor/1813089-initwithspecification.md)
  Primary initializer for the IONaturalMemoryCursor class.
- [withSpecification](ionaturalmemorycursor/1813112-withspecification.md)
  Creates and initializes an IONaturalMemoryCursor in one operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionaturalmemorycursor/1813100-outputsegment)*