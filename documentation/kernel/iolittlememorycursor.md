# IOLittleMemoryCursor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the little endian byte order.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOLittleMemoryCursor : IOMemoryCursor
```

## Overview

The IOLittleMemoryCursor would be used when the DMA hardware requires a little endian address and length pair. This cursor outputs an array of PhysicalSegments that are encoded in little endian format.

## Topics

### Miscellaneous
- [getPhysicalSegments](./iolittlememorycursor/api-1812505-getphysicalsegments.md)
  Generates a little endian physical scatter/gather list given a memory descriptor.
- [initWithSpecification](./iolittlememorycursor/api-1812512-initwithspecification.md)
  Primary initializer for the IOLittleMemoryCursor class.
- [outputSegment](./iolittlememorycursor/api-1812519-outputsegment.md)
  Outputs the given segment into the output segments array in little endian byte order.
- [withSpecification](./iolittlememorycursor/api-1812526-withspecification.md)
  Creates and initializes an IOLittleMemoryCursor in one operation.
### Constants
- [Miscellaneous Defines](./iolittlememorycursor/miscellaneous_defines.md)
### Instance Methods
- [- getMetaClass](./iolittlememorycursor/api-1400982-getmetaclass.md)
- [- getPhysicalSegments](./iolittlememorycursor/api-1401010-getphysicalsegments.md)
- [- initWithSpecification](./iolittlememorycursor/api-1401004-initwithspecification.md)
### Type Methods
- [+ outputSegment](./iolittlememorycursor/api-1400967-outputsegment.md)
- [+ withSpecification](./iolittlememorycursor/api-1400996-withspecification.md)

## Relationships

### Inherits From
- [IOMemoryCursor](./iomemorycursor.md)

## See Also

### Cursors
- [IOBigMemoryCursor](./iobigmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the big endian byte order.
- [IONaturalMemoryCursor](./ionaturalmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the natural byte orientation for the CPU.
- [IOMemoryCursor](./iomemorycursor.md)
  A mechanism to convert memory references to physical addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iolittlememorycursor)*