# initWithSpecification

**Framework**: Kernel  
**Kind**: instm

Primary initializer for the IOMemoryCursor class.

## Declaration

```swift
virtual bool initWithSpecification(
 SegmentFunction outSegFunc, 
 IOPhysicalLength maxSegmentSize = 0, 
 IOPhysicalLength maxTransferSize = 0, 
 IOPhysicalLength alignment = 1);
```

#### Return_value

Returns true if the inherited classes and this instance initialize successfully.

## Parameters

- `outSegFunc`: SegmentFunction to call to output one physical segment.
- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restrictions on output physical addresses. Not currently implemented. Defaults to single byte alignment.

## See Also

- [genPhysicalSegments](iomemorycursor/1812441-genphysicalsegments.md)
  Generates a physical scatter/gather list given a memory descriptor.
- [withSpecification](iomemorycursor/1812453-withspecification.md)
  Creates and initializes an IOMemoryCursor in one operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorycursor/1812445-initwithspecification)*