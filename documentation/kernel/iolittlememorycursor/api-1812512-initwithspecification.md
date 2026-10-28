# initWithSpecification

**Framework**: Kernel  
**Kind**: instm

Primary initializer for the IOLittleMemoryCursor class.

## Declaration

```cpp
virtual bool initWithSpecification(
 IOPhysicalLength maxSegmentSize, 
 IOPhysicalLength maxTransferSize, 
 IOPhysicalLength alignment = 1);
```

## Return Value

Returns true if the inherited classes and this instance initialize successfully.

## Parameters

- `maxSegmentSize`: Maximum allowable size for one segment. Defaults to 0.
- `maxTransferSize`: Maximum size of an entire transfer. Defaults to 0 indicating no maximum.
- `alignment`: Alignment restrictions on output physical addresses. Not currently implemented. Defaults to single byte alignment.

## See Also

### Miscellaneous
- [getPhysicalSegments](./api-1812505-getphysicalsegments.md)
  Generates a little endian physical scatter/gather list given a memory descriptor.
- [outputSegment](./api-1812519-outputsegment.md)
  Outputs the given segment into the output segments array in little endian byte order.
- [withSpecification](./api-1812526-withspecification.md)
  Creates and initializes an IOLittleMemoryCursor in one operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iolittlememorycursor/1812512-initwithspecification)*