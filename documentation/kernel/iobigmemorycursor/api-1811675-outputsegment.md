# outputSegment

**Framework**: Kernel  
**Kind**: instm

Outputs the given segment into the output segments array in big endian byte order.

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

- [getPhysicalSegments](iobigmemorycursor/1811632-getphysicalsegments.md)
  Generates a big endian physical scatter/gather list given a memory descriptor.
- [initWithSpecification](iobigmemorycursor/1811657-initwithspecification.md)
  Primary initializer for the IOBigMemoryCursor class.
- [withSpecification](iobigmemorycursor/1811699-withspecification.md)
  Creates and initializes an IOBigMemoryCursor in one operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobigmemorycursor/1811675-outputsegment)*