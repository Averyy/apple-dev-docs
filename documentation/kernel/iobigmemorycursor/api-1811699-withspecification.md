# withSpecification

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an IOBigMemoryCursor in one operation.

## Declaration

```c
static IOBigMemoryCursor * withSpecification(
 IOPhysicalLength maxSegmentSize, 
 IOPhysicalLength maxTransferSize, 
 IOPhysicalLength alignment = 1);
```

## Return Value

Returns a new memory cursor if successfully created and initialized, 0 otherwise.

## Overview

Factory function to create and initialize an IOBigMemoryCursor in one operation. See also IOBigMemoryCursor::initWithSpecification.

## Parameters

- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restrictions on output physical addresses. Not currently implemented. Defaults to single byte alignment.

## See Also

### Miscellaneous
- [getPhysicalSegments](./api-1811632-getphysicalsegments.md)
  Generates a big endian physical scatter/gather list given a memory descriptor.
- [initWithSpecification](./api-1811657-initwithspecification.md)
  Primary initializer for the IOBigMemoryCursor class.
- [outputSegment](./api-1811675-outputsegment.md)
  Outputs the given segment into the output segments array in big endian byte order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobigmemorycursor/1811699-withspecification)*