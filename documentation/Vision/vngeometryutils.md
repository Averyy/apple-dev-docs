# VNGeometryUtils

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNGeometryUtils : NSObject
```

## Topics

### Calculating Bounding Circles
- [class func boundingCircle(for: VNContour) throws -> VNCircle](./vngeometryutils/boundingcircle%28for%29-423ll.md)
  Calculates a bounding circle for the specified contour object.
- [class func boundingCircle(for: [VNPoint]) throws -> VNCircle](./vngeometryutils/boundingcircle%28for%29-9dggv.md)
  Calculates a bounding circle for the specified array of points.
- [class func boundingCircle(forSIMDPoints: UnsafePointer<simd_float2>, pointCount: Int) throws -> VNCircle](./vngeometryutils/boundingcircle%28forsimdpoints,pointcount%29.md)
  Calculates a bounding circle for the specified points.
### Calculating Area and Perimeter
- [class func calculateArea(UnsafeMutablePointer<Double>, for: VNContour, orientedArea: Bool) throws](./vngeometryutils/calculatearea%28_,for,orientedarea%29.md)
  Calculates the area for the specified contour.
- [class func calculatePerimeter(UnsafeMutablePointer<Double>, for: VNContour) throws](./vngeometryutils/calculateperimeter%28_,for%29.md)
  Calculates the perimeter of a closed contour.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Utilities
- [struct VNComputeStage](./vncomputestage.md)
  Types that represent the compute stage.
- [class VNVideoProcessor](./vnvideoprocessor.md)
  An object that performs offline analysis of video content.
- [struct VNVideoProcessingOption](./vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeometryutils)*