# unitVector(for:)

**Framework**: Vision  
**Kind**: method

Calculates a vector that’s normalized by preserving its direction, so that the vector length equals 1.0.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func unitVector(for vector: VNVector) -> VNVector
```

#### Return Value

The unit vector.

## Parameters

- `vector`: The vector whose unit vector you want to calculate.

## See Also

- [var length: Double](vnvector/length.md)
  The length, or absolute value, of the vector.
- [var r: Double](vnvector/r.md)
  The radius, absolute value, or length of the vector.
- [var theta: Double](vnvector/theta.md)
  The angle between the vector direction and the positive direction of the x-axis.
- [var squaredLength: Double](vnvector/squaredlength.md)
  The squared length of the vector.
- [var x: Double](vnvector/x.md)
  A signed projection that indicates the vector’s direction on the x-axis.
- [var y: Double](vnvector/y.md)
  A signed projection that indicates the vector’s direction on the y-axis.
- [class func dotProduct(of: VNVector, vector: VNVector) -> Double](vnvector/dotproduct(of:vector:).md)
  Caclulates the dot product of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector/unitvector(for:))*