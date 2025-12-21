# MPSIntegerDivisionParams

**Framework**: Metal Performance Shaders  
**Kind**: struct

Parameters that define the parts of a division operation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSIntegerDivisionParams
```

## Topics

### Initializers
- [init()](mpsintegerdivisionparams/init.md)
- [init(divisor: UInt16, recip: UInt16, addend: UInt16, shift: UInt16)](mpsintegerdivisionparams/init(divisor:recip:addend:shift:).md)
### Instance Properties
- [var addend: UInt16](mpsintegerdivisionparams/addend.md)
- [var divisor: UInt16](mpsintegerdivisionparams/divisor.md)
- [var recip: UInt16](mpsintegerdivisionparams/recip.md)
- [var shift: UInt16](mpsintegerdivisionparams/shift.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MPSCustomKernelArgumentCount](mpscustomkernelargumentcount.md)
  A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.
- [struct MPSCustomKernelInfo](mpscustomkernelinfo.md)
- [struct MPSCustomKernelSourceInfo](mpscustomkernelsourceinfo.md)
- [struct MPSDimensionSlice](mpsdimensionslice.md)
- [struct MPSImageCoordinate](mpsimagecoordinate.md)
- [struct MPSImageRegion](mpsimageregion.md)
- [struct MPSIntersectionDistance](mpsintersectiondistance.md)
  An intersection result that contains the distance from the ray origin to the intersection point.
- [struct MPSIntersectionDistancePrimitiveIndex](mpsintersectiondistanceprimitiveindex.md)
  An intersection result that contains the distance from the ray origin to the intersection point, and the index of the intersected primitive.
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndex](mpsintersectiondistanceprimitiveindexbufferindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexCoordinates](mpsintersectiondistanceprimitiveindexbufferindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndex](mpsintersectiondistanceprimitiveindexbufferindexinstanceindex.md)
- [struct MPSIntersectionDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates](mpsintersectiondistanceprimitiveindexbufferindexinstanceindexcoordinates.md)
- [struct MPSIntersectionDistancePrimitiveIndexCoordinates](mpsintersectiondistanceprimitiveindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive index, and intersection point coordinates.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndex](mpsintersectiondistanceprimitiveindexinstanceindex.md)
  An intersection result that contains the origin-intersection distance, and intersected primitive and instance indices.
- [struct MPSIntersectionDistancePrimitiveIndexInstanceIndexCoordinates](mpsintersectiondistanceprimitiveindexinstanceindexcoordinates.md)
  An intersection result that contains the origin-intersection distance, intersected primitive and instance indices, and intersection point coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsintegerdivisionparams)*