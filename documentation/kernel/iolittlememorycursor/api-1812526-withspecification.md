# withSpecification

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an IOLittleMemoryCursor in one operation.

## Declaration

```swift
static IOLittleMemoryCursor * withSpecification(
 IOPhysicalLength maxSegmentSize, 
 IOPhysicalLength maxTransferSize, 
 IOPhysicalLength alignment = 1);
```

#### Return_value

Returns a new memory cursor if successfully created and initialized, 0 otherwise.

#### Overview

Factory function to create and initialize an IOLittleMemoryCursor in one operation. See also IOLittleMemoryCursor::initWithSpecification.

## Parameters

- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restrictions on output physical addresses. Not currently implemented. Defaults to single byte alignment.

## See Also

- [getPhysicalSegments](iolittlememorycursor/1812505-getphysicalsegments.md)
  Generates a little endian physical scatter/gather list given a memory descriptor.
- [initWithSpecification](iolittlememorycursor/1812512-initwithspecification.md)
  Primary initializer for the IOLittleMemoryCursor class.
- [outputSegment](iolittlememorycursor/1812519-outputsegment.md)
  Outputs the given segment into the output segments array in little endian byte order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iolittlememorycursor/1812526-withspecification)*