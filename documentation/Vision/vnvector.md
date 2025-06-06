# VNVector

**Framework**: Vision  
**Kind**: class

An immutable 2D vector represented by its x-axis and y-axis projections.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNVector
```

## Topics

### Creating a Vector
- [init(byAdding: VNVector, to: VNVector)](vnvector/init(byadding:to:).md)
  Creates a new vector by adding the specified vectors.
- [init(bySubtracting: VNVector, from: VNVector)](vnvector/init(bysubtracting:from:).md)
  Creates a new vector by subtracting the first vector from the second vector.
- [init(byMultiplying: VNVector, byScalar: Double)](vnvector/init(bymultiplying:byscalar:).md)
  Creates a new vector by multiplying the specified vector’s x-axis and y-axis projections by the scalar value.
- [convenience init(r: Double, theta: Double)](vnvector/init(r:theta:).md)
  Creates a new vector in polar coordinate space.
- [convenience init(vectorHead: VNPoint, tail: VNPoint)](vnvector/init(vectorhead:tail:).md)
  Creates a new vector in Cartesian coordinate space.
- [init(xComponent: Double, yComponent: Double)](vnvector/init(xcomponent:ycomponent:).md)
  Creates a new vector in Cartesian coordinate space, based on its x-axis and y-axis projections.
- [class var zero: VNVector](vnvector/zero.md)
  A vector object with zero length.
### Inspecting a Vector
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
- [class func unitVector(for: VNVector) -> VNVector](vnvector/unitvector(for:).md)
  Calculates a vector that’s normalized by preserving its direction, so that the vector length equals 1.0.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class VNCircle](vncircle.md)
  An immutable 2D circle represented by its center point and radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector)*