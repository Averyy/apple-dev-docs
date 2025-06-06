# IOMemoryCursor

**Framework**: Kernel  
**Kind**: cl

A mechanism to convert memory references to physical addresses.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOMemoryCursor : OSObject
```

#### Overview

The IOMemoryCursor declares the super class that all specific memory cursors must inherit from, but a memory cursor can be created without a specific format subclass by just providing a segment function to the initializers. This class does the difficult stuff of dividing a memory descriptor into a physical scatter/gather list appropriate for the target hardware.

A driver is expected to create a memory cursor and configure it to the limitations of its DMA hardware; for instance the memory cursor used by the FireWire SBP-2 protocol has a maximum physical segment size of 2^16 - 1 but the actual transfer size is unlimited. Thus it would create a cursor with a maxSegmentSize of 65535 and a maxTransfer size of UINT_MAX. It would also provide a SegmentFunction that can output a pagelist entry.

Below is the simplest example of a SegmentFunction:

void IONaturalMemoryCursor::outputSegment(PhysicalSegment segment,

void * outSegments,

UInt32 outSegmentIndex)

{

((PhysicalSegment *) outSegments)[outSegmentIndex] = segment;

}

## Topics

### Miscellaneous
- [genPhysicalSegments](iomemorycursor/1812441-genphysicalsegments.md)
  Generates a physical scatter/gather list given a memory descriptor.
- [initWithSpecification](iomemorycursor/1812445-initwithspecification.md)
  Primary initializer for the IOMemoryCursor class.
- [withSpecification](iomemorycursor/1812453-withspecification.md)
  Creates and initializes an IOMemoryCursor in one operation.
### Callbacks
- [SegmentFunction](iodmacommand/segmentfunction.md)
  A C function that translates a 64-bit segment and outputs a single desired segment to the specified array. 
### Constants
- [Miscellaneous Defines](iomemorycursor/miscellaneous_defines.md)
### DataTypes
- [PhysicalSegment](iomemorycursor/physicalsegment.md)
### Instance Variables
- [outSeg](iomemorycursor/outseg.md)
- [maxTransferSize](iomemorycursor/maxtransfersize.md)
- [maxSegmentSize](iomemorycursor/maxsegmentsize.md)
- [alignMask](iomemorycursor/alignmask.md)
### Instance Methods
- [- genPhysicalSegments](iomemorycursor/1400980-genphysicalsegments.md)
- [- getMetaClass](iomemorycursor/1401008-getmetaclass.md)
- [- initWithSpecification](iomemorycursor/1401022-initwithspecification.md)
### Type Methods
- [+ withSpecification](iomemorycursor/1400994-withspecification.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOBigMemoryCursor](iobigmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the big endian byte order.
- [IOLittleMemoryCursor](iolittlememorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the little endian byte order.
- [IONaturalMemoryCursor](ionaturalmemorycursor.md)
  An IOMemoryCursor subclass that outputs a vector of PhysicalSegments in the natural byte orientation for the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorycursor)*