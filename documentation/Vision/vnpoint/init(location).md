# init(location:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a point object from the specified Core Graphics point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(location: CGPoint)
```

```objc
- (instancetype) initWithLocation:(CGPoint) location;
```

## Parameters

- `location`: The Core Graphics point.

## See Also

### Creating a Point
- [init(x: Double, y: Double)](./init%28x,y%29.md)
  Creates a point object with the specified coordinates.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class func apply(VNVector, to: VNPoint) -> VNPoint](./apply%28_,to%29.md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.
- [class var zero: VNPoint](./zero.md)
  A point object that represents the origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/init(location:))*