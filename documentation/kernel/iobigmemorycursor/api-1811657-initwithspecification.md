# initWithSpecification

**Framework**: Kernel  
**Kind**: instm

Primary initializer for the IOBigMemoryCursor class.

## Declaration

```swift
virtual bool initWithSpecification(
 IOPhysicalLength maxSegmentSize, 
 IOPhysicalLength maxTransferSize, 
 IOPhysicalLength alignment = 1);
```

#### Return_value

Returns true if the inherited classes and this instance initialize successfully.

## Parameters

- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restrictions on output physical addresses. Not currently implemented. Defaults to single byte alignment.

## See Also

- [getPhysicalSegments](iobigmemorycursor/1811632-getphysicalsegments.md)
  Generates a big endian physical scatter/gather list given a memory descriptor.
- [outputSegment](iobigmemorycursor/1811675-outputsegment.md)
  Outputs the given segment into the output segments array in big endian byte order.
- [withSpecification](iobigmemorycursor/1811699-withspecification.md)
  Creates and initializes an IOBigMemoryCursor in one operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobigmemorycursor/1811657-initwithspecification)*