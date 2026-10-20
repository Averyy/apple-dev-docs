# init(byMultiplying:byScalar:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new vector by multiplying the specified vector’s x-axis and y-axis projections by the scalar value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(byMultiplying vector: VNVector, byScalar scalar: Double)
```

```objc
+ (VNVector *) vectorByMultiplyingVector:(VNVector *) vector byScalar:(double) scalar;
```

## Parameters

- `vector`: The vector.
- `scalar`: The scalar value by which to multiply the x-axis and y-axis projections.

## See Also

### Creating a Vector
- [init(byAdding: VNVector, to: VNVector)](./init%28byadding,to%29.md)
  Creates a new vector by adding the specified vectors.
- [init(byAddingVector: VNVector, toVector: VNVector)](./init%28byaddingvector,tovector%29.md)
- [init(bySubtracting: VNVector, from: VNVector)](./init%28bysubtracting,from%29.md)
  Creates a new vector by subtracting the first vector from the second vector.
- [init(bySubtractingVector: VNVector, fromVector: VNVector)](./init%28bysubtractingvector,fromvector%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvector/init(bymultiplying:byscalar:))*