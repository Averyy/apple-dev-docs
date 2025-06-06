# init(vectorHead:tail:)

**Framework**: Vision  
**Kind**: init

Creates a new vector in Cartesian coordinate space.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(vectorHead head: VNPoint, tail: VNPoint)
```

## Parameters

- `head`: The vector’s head point.
- `tail`: The vector’s tail point.

## See Also

- [init(byAdding: VNVector, to: VNVector)](vnvector/init(byadding:to:).md)
  Creates a new vector by adding the specified vectors.
- [init(bySubtracting: VNVector, from: VNVector)](vnvector/init(bysubtracting:from:).md)
  Creates a new vector by subtracting the first vector from the second vector.
- [init(byMultiplying: VNVector, byScalar: Double)](vnvector/init(bymultiplying:byscalar:).md)
  Creates a new vector by multiplying the specified vector’s x-axis and y-axis projections by the scalar value.
- [convenience init(r: Double, theta: Double)](vnvector/init(r:theta:).md)
  Creates a new vector in polar coordinate space.
- [init(xComponent: Double, yComponent: Double)](vnvector/init(xcomponent:ycomponent:).md)
  Creates a new vector in Cartesian coordinate space, based on its x-axis and y-axis projections.
- [class var zero: VNVector](vnvector/zero.md)
  A vector object with zero length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector/init(vectorhead:tail:))*