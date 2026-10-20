# init(center:radius:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a circle with the specified center and radius.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(center: VNPoint, radius: Double)
```

```objc
- (instancetype) initWithCenter:(VNPoint *) center radius:(double) radius;
```

## Parameters

- `center`: The circle center.
- `radius`: The circle radius.

## See Also

### Creating a Circle
- [convenience init(center: VNPoint, diameter: Double)](./init%28center,diameter%29.md)
  Creates a circle with the specified center and diameter.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var zero: VNCircle](./zero.md)
  A circle object centered at the origin, with a radius of zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle/init(center:radius:))*