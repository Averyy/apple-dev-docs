# init(x:y:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a point object with the specified coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(x: Double, y: Double)
```

```objc
- (instancetype) initWithX:(double) x y:(double) y;
```

## Parameters

- `x`: The x-coordinate value.
- `y`: The y-coordinate value.

## See Also

### Creating a Point
- [convenience init(location: CGPoint)](./init%28location%29.md)
  Creates a point object from the specified Core Graphics point.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class func apply(VNVector, to: VNPoint) -> VNPoint](./apply%28_,to%29.md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.
- [class var zero: VNPoint](./zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/init(x:y:))*