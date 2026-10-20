# length

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The length, or absolute value, of the vector.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var length: Double { get }
```

```objc
@property (readonly) double length;
```

## See Also

### Inspecting a Vector
- [var r: Double](./r.md)
  The radius, absolute value, or length of the vector.
- [var theta: Double](./theta.md)
  The angle between the vector direction and the positive direction of the x-axis.
- [var squaredLength: Double](./squaredlength.md)
  The squared length of the vector.
- [var x: Double](./x.md)
  A signed projection that indicates the vector’s direction on the x-axis.
- [var y: Double](./y.md)
  A signed projection that indicates the vector’s direction on the y-axis.
- [class func dotProduct(of: VNVector, vector: VNVector) -> Double](./dotproduct%28of,vector%29.md)
  Caclulates the dot product of two vectors.
- [class func unitVector(for: VNVector) -> VNVector](./unitvector%28for%29.md)
  Calculates a vector that’s normalized by preserving its direction, so that the vector length equals 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector/length)*