# boundingCircle(for:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Calculates a bounding circle for the specified array of points.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func boundingCircle(for points: [VNPoint]) throws -> VNCircle
```

```objc
+ (VNCircle *) boundingCircleForPoints:(NSArray<VNPoint *> *) points error:(NSError **) error;
```

#### Return Value

The bounding [`VNCircle`](../vncircle.md) object.

## Parameters

- `points`: A collection of points around which to calculate the bounding circle.

## See Also

### Calculating Bounding Circles
- [class func boundingCircle(for: VNContour) throws -> VNCircle](./boundingcircle%28for%29-423ll.md)
  Calculates a bounding circle for the specified contour object.
- [class func boundingCircle(forSIMDPoints: UnsafePointer<simd_float2>, pointCount: Int) throws -> VNCircle](./boundingcircle%28forsimdpoints,pointcount%29.md)
  Calculates a bounding circle for the specified points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeometryutils/boundingcircle(for:)-9dggv)*