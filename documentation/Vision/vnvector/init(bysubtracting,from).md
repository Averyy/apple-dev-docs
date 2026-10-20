# init(bySubtracting:from:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new vector by subtracting the first vector from the second vector.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(bySubtracting v1: VNVector, from v2: VNVector)
```

```objc
+ (VNVector *) vectorBySubtractingVector:(VNVector *) v1 fromVector:(VNVector *) v2;
```

## Parameters

- `v1`: The first vector.
- `v2`: The second vector.

## See Also

### Creating a Vector
- [init(byAdding: VNVector, to: VNVector)](./init%28byadding,to%29.md)
  Creates a new vector by adding the specified vectors.
- [init(byAddingVector: VNVector, toVector: VNVector)](./init%28byaddingvector,tovector%29.md)
- [init(bySubtractingVector: VNVector, fromVector: VNVector)](./init%28bysubtractingvector,fromvector%29.md)
- [init(byMultiplying: VNVector, byScalar: Double)](./init%28bymultiplying,byscalar%29.md)
  Creates a new vector by multiplying the specified vector’s x-axis and y-axis projections by the scalar value.
- [init(byMultiplyingVector: VNVector, byScalar: Double)](./init%28bymultiplyingvector,byscalar%29.md)
- [convenience init(r: Double, theta: Double)](./init%28r,theta%29.md)
  Creates a new vector in polar coordinate space.
- [convenience init(vectorHead: VNPoint, tail: VNPoint)](./init%28vectorhead,tail%29.md)
  Creates a new vector in Cartesian coordinate space.
- [init(XComponent: Double, yComponent: Double)](./init%28xcomponent,ycomponent%29-231pv.md)
- [init(xComponent: Double, yComponent: Double)](./init%28xcomponent,ycomponent%29-3p5k3.md)
  Creates a new vector in Cartesian coordinate space, based on its x-axis and y-axis projections.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var zero: VNVector](./zero.md)
  A vector object with zero length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector/init(bysubtracting:from:))*