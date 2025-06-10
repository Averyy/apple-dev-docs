# withSpecification

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an IONaturalMemoryCursor in one operation.

## Declaration

```swift
static IONaturalMemoryCursor * withSpecification(
 IOPhysicalLength maxSegmentSize, 
 IOPhysicalLength maxTransferSize, 
 IOPhysicalLength alignment = 1);
```

#### Return_value

Returns a new memory cursor if successfully created and initialized, 0 otherwise.

#### Overview

Factory function to create and initialize an IONaturalMemoryCursor in one operation. For more information, see IONaturalMemoryCursor::initWithSpecification.

## Parameters

- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restrictions on output physical addresses. Not currently implemented. Defaults to single byte alignment.

## See Also

- [getPhysicalSegments](ionaturalmemorycursor/1813076-getphysicalsegments.md)
  Generates a CPU natural physical scatter/gather list given a memory descriptor.
- [initWithSpecification](ionaturalmemorycursor/1813089-initwithspecification.md)
  Primary initializer for the IONaturalMemoryCursor class.
- [outputSegment](ionaturalmemorycursor/1813100-outputsegment.md)
  Outputs the given segment into the output segments array in natural byte order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionaturalmemorycursor/1813112-withspecification)*