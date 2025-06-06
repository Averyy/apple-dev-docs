# VNGeometryUtils

**Framework**: Vision  
**Kind**: class

Utility methods to determine the geometries of various Vision types.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNGeometryUtils
```

## Topics

### Calculating Bounding Circles
- [class func boundingCircle(for: VNContour) throws -> VNCircle](vngeometryutils/boundingcircle(for:)-423ll.md)
  Calculates a bounding circle for the specified contour object.
- [class func boundingCircle(for: [VNPoint]) throws -> VNCircle](vngeometryutils/boundingcircle(for:)-9dggv.md)
  Calculates a bounding circle for the specified array of points.
- [class func boundingCircle(forSIMDPoints: UnsafePointer<simd_float2>, pointCount: Int) throws -> VNCircle](vngeometryutils/boundingcircle(forsimdpoints:pointcount:).md)
  Calculates a bounding circle for the specified points.
### Calculating Area and Perimeter
- [class func calculateArea(UnsafeMutablePointer<Double>, for: VNContour, orientedArea: Bool) throws](vngeometryutils/calculatearea(_:for:orientedarea:).md)
  Calculates the area for the specified contour.
- [class func calculatePerimeter(UnsafeMutablePointer<Double>, for: VNContour) throws](vngeometryutils/calculateperimeter(_:for:).md)
  Calculates the perimeter of a closed contour.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct VNComputeStage](vncomputestage.md)
  Types that represent the compute stage.
- [class VNVideoProcessor](vnvideoprocessor.md)
  An object that performs offline analysis of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeometryutils)*