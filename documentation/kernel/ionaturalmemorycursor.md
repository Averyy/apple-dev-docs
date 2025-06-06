# IONaturalMemoryCursor

**Framework**: Kernel  
**Kind**: cl

An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the natural byte orientation for the CPU.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IONaturalMemoryCursor : IOMemoryCursor
```

#### Overview

The IONaturalMemoryCursor would be used when it is too difficult to safely describe a SegmentFunction that is more appropriate for your hardware. This cursor just outputs an array of PhysicalSegments.

## Topics

### Miscellaneous
- [getPhysicalSegments](ionaturalmemorycursor/1813076-getphysicalsegments.md)
  Generates a CPU natural physical scatter/gather list given a memory descriptor.
- [initWithSpecification](ionaturalmemorycursor/1813089-initwithspecification.md)
  Primary initializer for the IONaturalMemoryCursor class.
- [outputSegment](ionaturalmemorycursor/1813100-outputsegment.md)
  Outputs the given segment into the output segments array in natural byte order.
- [withSpecification](ionaturalmemorycursor/1813112-withspecification.md)
  Creates and initializes an IONaturalMemoryCursor in one operation.
### Constants
- [Miscellaneous Defines](ionaturalmemorycursor/miscellaneous_defines.md)
### Instance Methods
- [- getMetaClass](ionaturalmemorycursor/1401014-getmetaclass.md)
- [- getPhysicalSegments](ionaturalmemorycursor/1400988-getphysicalsegments.md)
- [- initWithSpecification](ionaturalmemorycursor/1401018-initwithspecification.md)
### Type Methods
- [+ outputSegment](ionaturalmemorycursor/1400992-outputsegment.md)
- [+ withSpecification](ionaturalmemorycursor/1400990-withspecification.md)

## Relationships

### Inherits From
- [IOMemoryCursor](iomemorycursor.md)

## See Also

- [IOBigMemoryCursor](iobigmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the big endian byte order.
- [IOLittleMemoryCursor](iolittlememorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the little endian byte order.
- [IOMemoryCursor](iomemorycursor.md)
  A mechanism to convert memory references to physical addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionaturalmemorycursor)*