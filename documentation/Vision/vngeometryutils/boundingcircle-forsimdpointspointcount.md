# boundingCircle(forSIMDPoints:pointCount:)

**Framework**: Vision  
**Kind**: method

Calculates a bounding circle for the specified points.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func boundingCircle(forSIMDPoints points: UnsafePointer<simd_float2>, pointCount: Int) throws -> VNCircle
```

#### Return Value

The bounding [`VNCircle`](vncircle.md) object.

## Parameters

- `points`: A collection of points around which to calculate the bounding circle.
- `pointCount`: The number of points in the   argument.

## See Also

- [class func boundingCircle(for: VNContour) throws -> VNCircle](vngeometryutils/boundingcircle(for:)-423ll.md)
  Calculates a bounding circle for the specified contour object.
- [class func boundingCircle(for: [VNPoint]) throws -> VNCircle](vngeometryutils/boundingcircle(for:)-9dggv.md)
  Calculates a bounding circle for the specified array of points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeometryutils/boundingcircle(forsimdpoints:pointcount:))*