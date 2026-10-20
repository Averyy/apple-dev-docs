# VNVector

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNVector : NSObject
```

## Topics

### Creating a Vector
- [init(byAdding: VNVector, to: VNVector)](./vnvector/init%28byadding,to%29.md)
  Creates a new vector by adding the specified vectors.
- [init(byAddingVector: VNVector, toVector: VNVector)](./vnvector/init%28byaddingvector,tovector%29.md)
- [init(bySubtracting: VNVector, from: VNVector)](./vnvector/init%28bysubtracting,from%29.md)
  Creates a new vector by subtracting the first vector from the second vector.
- [init(bySubtractingVector: VNVector, fromVector: VNVector)](./vnvector/init%28bysubtractingvector,fromvector%29.md)
- [init(byMultiplying: VNVector, byScalar: Double)](./vnvector/init%28bymultiplying,byscalar%29.md)
  Creates a new vector by multiplying the specified vector’s x-axis and y-axis projections by the scalar value.
- [init(byMultiplyingVector: VNVector, byScalar: Double)](./vnvector/init%28bymultiplyingvector,byscalar%29.md)
- [convenience init(r: Double, theta: Double)](./vnvector/init%28r,theta%29.md)
  Creates a new vector in polar coordinate space.
- [convenience init(vectorHead: VNPoint, tail: VNPoint)](./vnvector/init%28vectorhead,tail%29.md)
  Creates a new vector in Cartesian coordinate space.
- [init(XComponent: Double, yComponent: Double)](./vnvector/init%28xcomponent,ycomponent%29-231pv.md)
- [init(xComponent: Double, yComponent: Double)](./vnvector/init%28xcomponent,ycomponent%29-3p5k3.md)
  Creates a new vector in Cartesian coordinate space, based on its x-axis and y-axis projections.
- [init?(coder: NSCoder)](./vnvector/init%28coder%29.md)
- [class var zero: VNVector](./vnvector/zero.md)
  A vector object with zero length.
### Inspecting a Vector
- [var length: Double](./vnvector/length.md)
  The length, or absolute value, of the vector.
- [var r: Double](./vnvector/r.md)
  The radius, absolute value, or length of the vector.
- [var theta: Double](./vnvector/theta.md)
  The angle between the vector direction and the positive direction of the x-axis.
- [var squaredLength: Double](./vnvector/squaredlength.md)
  The squared length of the vector.
- [var x: Double](./vnvector/x.md)
  A signed projection that indicates the vector’s direction on the x-axis.
- [var y: Double](./vnvector/y.md)
  A signed projection that indicates the vector’s direction on the y-axis.
- [class func dotProduct(of: VNVector, vector: VNVector) -> Double](./vnvector/dotproduct%28of,vector%29.md)
  Caclulates the dot product of two vectors.
- [class func unitVector(for: VNVector) -> VNVector](./vnvector/unitvector%28for%29.md)
  Calculates a vector that’s normalized by preserving its direction, so that the vector length equals 1.0.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Common data types
- [class VNCircle](./vncircle.md)
  An immutable 2D circle represented by its center point and radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector)*