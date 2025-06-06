# init(r:theta:)

**Framework**: Vision  
**Kind**: init

Creates a new vector in polar coordinate space.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(r: Double, theta: Double)
```

## Parameters

- `r`: The length of the vector.
- `theta`: The angle that the vector forms with the positive direction of the x-axis.

## See Also

- [init(byAdding: VNVector, to: VNVector)](vnvector/init(byadding:to:).md)
  Creates a new vector by adding the specified vectors.
- [init(bySubtracting: VNVector, from: VNVector)](vnvector/init(bysubtracting:from:).md)
  Creates a new vector by subtracting the first vector from the second vector.
- [init(byMultiplying: VNVector, byScalar: Double)](vnvector/init(bymultiplying:byscalar:).md)
  Creates a new vector by multiplying the specified vector’s x-axis and y-axis projections by the scalar value.
- [convenience init(vectorHead: VNPoint, tail: VNPoint)](vnvector/init(vectorhead:tail:).md)
  Creates a new vector in Cartesian coordinate space.
- [init(xComponent: Double, yComponent: Double)](vnvector/init(xcomponent:ycomponent:).md)
  Creates a new vector in Cartesian coordinate space, based on its x-axis and y-axis projections.
- [class var zero: VNVector](vnvector/zero.md)
  A vector object with zero length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector/init(r:theta:))*