# IOBigMemoryCursor

**Framework**: Kernel  
**Kind**: cl

An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the big endian byte order.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOBigMemoryCursor : IOMemoryCursor
```

#### Overview

The IOBigMemoryCursor would be used when the DMA hardware requires a big endian address and length pair. This cursor outputs an array of PhysicalSegments that are encoded in big-endian format.

## Topics

### Miscellaneous
- [getPhysicalSegments](iobigmemorycursor/1811632-getphysicalsegments.md)
  Generates a big endian physical scatter/gather list given a memory descriptor.
- [initWithSpecification](iobigmemorycursor/1811657-initwithspecification.md)
  Primary initializer for the IOBigMemoryCursor class.
- [outputSegment](iobigmemorycursor/1811675-outputsegment.md)
  Outputs the given segment into the output segments array in big endian byte order.
- [withSpecification](iobigmemorycursor/1811699-withspecification.md)
  Creates and initializes an IOBigMemoryCursor in one operation.
### Constants
- [Miscellaneous Defines](iobigmemorycursor/miscellaneous_defines.md)
### Instance Methods
- [- getMetaClass](iobigmemorycursor/1400969-getmetaclass.md)
- [- getPhysicalSegments](iobigmemorycursor/1400973-getphysicalsegments.md)
- [- initWithSpecification](iobigmemorycursor/1401016-initwithspecification.md)
### Type Methods
- [+ outputSegment](iobigmemorycursor/1401020-outputsegment.md)
- [+ withSpecification](iobigmemorycursor/1401012-withspecification.md)

## Relationships

### Inherits From
- [IOMemoryCursor](iomemorycursor.md)

## See Also

- [IOLittleMemoryCursor](iolittlememorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the little endian byte order.
- [IONaturalMemoryCursor](ionaturalmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the natural byte orientation for the CPU.
- [IOMemoryCursor](iomemorycursor.md)
  A mechanism to convert memory references to physical addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobigmemorycursor)*