# zero

**Framework**: Vision  
**Kind**: property  
**Role**: Type Property

A point object that represents the origin.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var zero: VNPoint { get }
```

```objc
@property (class, strong, readonly) VNPoint * zeroPoint;
```

## Discussion

The origin point is (0.0, 0.0).

## See Also

### Creating a Point
- [init(x: Double, y: Double)](./init%28x,y%29.md)
  Creates a point object with the specified coordinates.
- [convenience init(location: CGPoint)](./init%28location%29.md)
  Creates a point object from the specified Core Graphics point.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class func apply(VNVector, to: VNPoint) -> VNPoint](./apply%28_,to%29.md)
  Creates a point object that’s shifted by the X and Y offsets of the specified vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnpoint/zero)*