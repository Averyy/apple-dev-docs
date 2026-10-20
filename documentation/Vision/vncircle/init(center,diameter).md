# init(center:diameter:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a circle with the specified center and diameter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(center: VNPoint, diameter: Double)
```

```objc
- (instancetype) initWithCenter:(VNPoint *) center diameter:(double) diameter;
```

## Parameters

- `center`: The circle center.
- `diameter`: The circle diameter.

## See Also

### Creating a Circle
- [init(center: VNPoint, radius: Double)](./init%28center,radius%29.md)
  Creates a circle with the specified center and radius.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var zero: VNCircle](./zero.md)
  A circle object centered at the origin, with a radius of zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle/init(center:diameter:))*